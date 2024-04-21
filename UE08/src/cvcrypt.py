import sys
import argparse
import kasiski

def parse_args():
    parser = argparse.ArgumentParser(description="Verschlüsselt oder entschlüsselt eine Datei mit einer Caesar- oder Vigenère-Chiffre.")
    parser.add_argument("infile", type=str, help="Zu verschlüsselnde Datei")
    parser.add_argument("outfile", type=str, nargs='?',  help="Zieldatei")
    parser.add_argument('-c', '--cipher', choices=['caesar', 'c', 'vigenere', 'v'], required=True,
                        help='Zu verwendende Chiffre')
    parser.add_argument('-v', '--verbose', action='store_true', help='Ausführliche Ausgabe')
    parser.add_argument('-q', '--quiet', action='store_true', help='Stiller Modus, unterdrücke Ausgabe')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Entschlüssle die Eingabe')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Verschlüssele die Eingabe')
    parser.add_argument('-k', '--key', type=str, required=True, help='Verschlüsselung-Key')
    return parser.parse_args()

def main():
    args = parse_args()
    cipher = kasiski.Caesar() if args.cipher in ['caesar', 'c'] else kasiski.Vigenere()

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