import xml.etree.ElementTree as ET
import sys
import csv

from pathlib import Path

def openXMLFile(path):
    tree = ET.parse(path)
    return tree.getroot()

if __name__ == "__main__":
    path = Path(sys.argv[1])
    root = openXMLFile(path)

    with open(path.with_suffix('.csv').name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for child in root:
            writer.writerow([child.attrib['name'], child.text])