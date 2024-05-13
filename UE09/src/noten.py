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

def read_xml_file(file_path):
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
    df = pd.DataFrame(data, columns=['Nummer', 'Anrede', 'Vorname', 'Nachname', 'Geburtsdatum', 'Verhalten'])
    return df

def main():
    parser = argparse.ArgumentParser(description='Read XML file and save as pandas DataFrame.')
    parser.add_argument('xml_file', type=str, help='Path to the XML file')

    args = parser.parse_args()

    try:
        df = read_xml_file(args.xml_file)
        print(df)
    except Exception as e:
        print("Error:", e, file=sys.stderr)

if __name__ == "__main__":
    main()
