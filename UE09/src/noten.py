import argparse
import pandas as pd
import sys
import re


def build_regex_tag(line):
    # Extract the tag name from the line
    tag = re.search(r'<(.*?)>', line).group(1)
    # Build a regex pattern for the tag
    regex_pattern = fr'<{tag}>(.*?)<\/{tag}>'
    return regex_pattern, tag


def read_xml_file(file_path) -> pd.DataFrame:
    with open(file_path, 'r') as f:
        xml_data = f.read()

    # Extract data from the XML
    data = {tag: [] for tag in set(re.findall(r'<(.*?)>', xml_data))}
    for line in xml_data.splitlines():
        regex_pattern, tag = build_regex_tag(line)
        matches = re.findall(regex_pattern, line)
        if matches:
            data[tag].extend(matches)

    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=['Nummer', 'Anrede', 'Vorname', 'Nachname', 'Geburtsdatum'], dtype=str)
    return df


# eine Regex Methode wäre es
# auch überprüfen auf datei
def read_csv_file(file_path) -> pd.DataFrame:
    df = pd.read_csv(file_path, sep=';', dtype=str)
    return df


# Eine Methode die zwei DataFrames zusammenführt am index 0


def main():
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
                # Überprüfen, ob der angegebene Gegenstand in den Spalten der CSV-Datei vorhanden ist
                if args.f not in df_csv.columns:
                    raise ValueError(f"Gegenstand '{args.f}' nicht in den Spalten der CSV-Datei gefunden.")
                # Filtern der CSV-Daten nach dem angegebenen Gegenstand
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
        if not args.quiet:
            print("Fehler:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
