import sys
import argparse
from Kasiski import Kasiski
from Caesar import Caesar
from Vigenere import Vigenere

def parse_args():
    parser = argparse.ArgumentParser(description="Verschlüsselt oder entschlüsselt eine Datei mit einer Caesar- oder Vigenère-Chiffre.")
    parser.add_argument("infile", type=str, help="Zu verschlüsselnde Datei")
    parser.add_argument("outfile", type=str, nargs='?',  help="Zieldatei")

    output_group = parser.add_mutually_exclusive_group()
    crypto_group = parser.add_mutually_exclusive_group()
    parser.add_argument('-c', '--cipher', choices=['caesar', 'c', 'vigenere', 'v'], required=True,
                        help='Zu verwendende Chiffre')
    output_group.add_argument('-v', '--verbose', action='store_true', help='Ausführliche Ausgabe')
    output_group.add_argument('-q', '--quiet', action='store_true', help='Stiller Modus, unterdrücke Ausgabe')
    crypto_group.add_argument('-d', '--decrypt', action='store_true', help='Entschlüssle die Eingabe')
    crypto_group.add_argument('-e', '--encrypt', action='store_true', help='Verschlüssele die Eingabe')
    parser.add_argument('-k', '--key', type=str, required=True, help='Verschlüsselung-Key')
    return parser.parse_args()

def main():
    args = parse_args()
    cipher = Caesar() if args.cipher in ['caesar', 'c'] else Vigenere()

    try:
        with open(args.infile, 'r') as f:
            plaintext = f.read()
        if args.decrypt:
            crypttext = cipher.decrypt(plaintext, args.key)
        else:
            crypttext = cipher.encrypt(plaintext, args.key)

        with open(args.outfile, 'w') as f:
            f.write(crypttext)

        if args.verbose:
            print(
                f"{'Decrypting' if args.decrypt else 'Encrypting'} {args.cipher.title()} with key = {args.key} from file {args.infile} into file {args.outfile or args.infile}")

    except FileNotFoundError:
        print(f"{args.infile}: No such file or directory", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()