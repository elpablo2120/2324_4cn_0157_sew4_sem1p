"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "1.8"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
import argparse
import sys
import os

from Kasiski import Kasiski
from Caesar import Caesar



def main():
    args = parse_args()
    cipher = Caesar() if args.cipher in ['caesar', 'c'] else Kasiski()

    try:
        with open(args.infile, 'r') as f:
            plaintext = f.read()

        if args.cipher in ['caesar', 'c']:
            key = cipher.crack(plaintext)
            key = ''.join(key)

            if args.verbose:
                print(f"Cracking {args.cipher.title()}-encrypted file {args.infile}: Key = {key}")
            else:
                print(key)

            if args.outfile:
                with open(args.outfile, 'w') as f:
                    f.write(key)
        if args.cipher in ['vigenere', 'v']:
            cipher = Kasiski(plaintext)
            len = cipher.ggt_count([cipher.dist_n_list(plaintext, i) for i in range(3, 10)][0]).most_common(1)[0][0]
            key = cipher.crack_key(len)

            if args.verbose:
                print(f"Cracking {args.cipher.title()}-encrypted file {args.infile}: Key = {key}")
            else:
                print(key)



    except FileNotFoundError:
        print(f"{args.infile}: No such file or directory", file=sys.stderr)
        sys.exit(1)




def parse_args():
    parser = argparse.ArgumentParser(description="Crack Caesar or Vigenere ciphers.")
    parser.add_argument("infile", type=str, help="File to crack")
    parser.add_argument('-c', '--cipher', choices=['caesar', 'c', 'vigenere', 'v'], default='c',
                        help='Cipher to use')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-q', '--quiet', action='store_true', help='Quiet mode, suppress output')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if not os.path.exists(args.infile):
        print(f"{args.infile}: No such file or directory", file=sys.stderr)
        sys.exit(1)
    main()
