"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "2.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Ready to Review"
"""
import argparse
import pandas as pd
import sys
import re


def build_regex_tag(line: str):
    """
    Extract a tag name from a line and build a regex pattern for it.
    :param line: input line
    :return: Regex for pattern and tag name
    >>> build_regex_tag('<Nummer>123</Nummer>')
    ('<Nummer>(.*?)<\\\/Nummer>', 'Nummer')
    """
    tag = re.search(r'<(.*?)>', line).group(1)
    regex_pattern = fr'<{tag}>(.*?)<\/{tag}>'
    return regex_pattern, tag


def read_xml_file(file_path: str) -> pd.DataFrame:
    """
    Read an XML file and convert it to a DataFrame. Uses build_regex_tag.
    :param file_path: Path to .xml
    :return: DataFrame with extracted data
    >>> df_xml = read_xml_file('test_data_xml.xml')
    >>> print(df_xml.to_string(index=False))
    Nummer Anrede Vorname Nachname Geburtsdatum
      4774   Frau   Emily   Sommer   2006-10-05
    """
    with open(file_path, 'r') as f:
        xml_data = f.read()

    data = {tag: [] for tag in set(re.findall(r'<(.*?)>', xml_data))}
    for line in xml_data.splitlines():
        regex_pattern, tag = build_regex_tag(line)
        matches = re.findall(regex_pattern, line)
        if matches:
            data[tag].extend(matches)

    df = pd.DataFrame(data, columns=['Nummer', 'Anrede', 'Vorname', 'Nachname', 'Geburtsdatum'], dtype=str)
    return df


def read_csv_file(file_path: str) -> pd.DataFrame:
    """
    Read a CSV file and convert it to a DataFrame.
    :param file_path: Path to .csv
    :return: DataFrame with extracted data
    >>> df_csv = read_csv_file('test_data_csv.csv')
    >>> print(df_csv.to_string(index=False))
    Nummer Verhalten ue  e RK D E GGP WIR BSP AM NW SEW ITP INSI NWT
      4774        SZ  0 40  1 2 1   1   1   1  1  1   1   1    1   1
    """
    df = pd.read_csv(file_path, sep=';', dtype=str)
    return df

def main():
    """
    Main function which provides argparser and calls the other functions (read_csv_file, read_xml_file, build_regex_tag)
    :return: None
    """
    parser = argparse.ArgumentParser(description='noten.py by Max Mustermann / HTL Rennweg')
    parser.add_argument('outfile', type=str, help='Ausgabedatei (z.B. result.csv)')
    parser.add_argument('-n', type=str, help='csv-Datei mit den Noten')
    parser.add_argument('-s', type=str, help='xml-Datei mit den Schülerdaten')
    parser.add_argument('-m', type=str, default='Nummer',
                        help='Name der Spalte, die zu verknüpfen ist (default = Nummer)')
    parser.add_argument('-f', type=str, help='Name des zu filternden Gegenstandes (z.B. SEW)')

    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument('-v', '--verbose', action='store_true', help='Gibt die Daten Kommandozeile aus')
    verbosity_group.add_argument('-q', '--quiet', action='store_true', help='keine Textausgabe')

    args = parser.parse_args()

    try:
        if args.n and args.s:
            df_xml = read_xml_file(args.s)
            df_csv = read_csv_file(args.n)

            if args.f:
                if args.f not in df_csv.columns:
                    raise ValueError(f"Gegenstand '{args.f}' nicht in den Spalten der CSV-Datei gefunden.")
                df_csv = df_csv[['Nummer', args.f]]

            df_xml.set_index(args.m, inplace=True)
            df_csv.set_index(args.m, inplace=True)
            df = df_xml.join(df_csv, on=args.m, how='inner')

            if not args.quiet and not args.verbose:
                print(f"Output-Datei: {args.outfile}")

            if args.verbose:
                print(f"csv-Datei mit den Noten: {args.n}")
                print(f"xml-Datei mit den Schülerdaten: {args.s}")
                print(f"Name der Spalte, die zu verknüpfen ist: {args.m}")
                print(f"Output-Datei: {args.outfile}")

            df.to_csv(args.outfile, sep=';', index=True)
        else:
            if not args.quiet:
                print("Bitte geben Sie sowohl eine CSV- als auch eine XML-Datei an.")
    except Exception as e:
            print("Fehler:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
