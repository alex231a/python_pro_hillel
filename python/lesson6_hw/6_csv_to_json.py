import json
import csv
import xml.etree.ElementTree as ET


class JsonToCsvConvertor:
    """Class that converts json to csv"""

    def __init__(self, file_name: str):
        self.file_name = file_name

    def _convert_json_to_po(self):
        """Loads data from json to python object"""
        with open(self.file_name, "r", encoding="utf-8") as f:
            content = json.load(f)
        return content

    def from_json_to_csv(self, csv_file_name: str):
        """Convert json to csv"""
        content = self._convert_json_to_po()
        with open(csv_file_name, mode='w', newline='',
                  encoding='utf-8') as f:
            fieldnames = content[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(content)


class CsvToJsonConvertor:
    """Class that converts csv to json"""

    def __init__(self, file_name: str):
        self.file_name = file_name

    def _convert_csv_to_po(self):
        """Loads data from CSV to python object"""
        with open(self.file_name, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def from_csv_to_json(self, json_file_name: str):
        """Convert csv to json"""
        content = self._convert_csv_to_po()
        with open(json_file_name, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4)


class XmlJsonConverter:
    """Class XML JSON Convertor"""

    def __init__(self, file_name: str):
        self.file_name = file_name

    def xml_to_json(self):
        """Convert XML to JSON"""
        tree = ET.parse(self.file_name)
        root = tree.getroot()
        products = []
        for product in root.findall("product"):
            product_dict = {}
            for child in product:
                product_dict[child.tag] = child.text
            products.append(product_dict)
        return json.dumps(products, indent=4)

    def json_to_xml(self, json_data: str):
        """Convert JSON to XML"""
        data = json.loads(json_data)
        root = ET.Element("products")
        for product in data:
            product_element = ET.SubElement(root, "product")
            for key, value in product.items():
                child = ET.SubElement(product_element, key)
                child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(self.file_name, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    json_file = "books.json"
    json_reader = JsonToCsvConvertor(file_name=json_file)
    json_reader.from_json_to_csv("new_csv_from_json.csv")

    csv_file = "students.csv"
    csv_reader = CsvToJsonConvertor(file_name=csv_file)
    csv_reader.from_csv_to_json("new_json_from_csv.json")

    xml_file = "products.xml"
    xml_reader = XmlJsonConverter(xml_file)
    print(xml_reader.xml_to_json())
