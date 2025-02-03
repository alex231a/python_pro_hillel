# import xml.etree.ElementTree as ET
from lxml import etree


class ReadXml:
    """Class has main methods for work with xml files"""

    def __init__(self, file_name: str):
        self.file_name = file_name

    def _get_products(self):
        """Get products collection from xml"""
        tree = etree.parse(self.file_name)
        root = tree.getroot()
        products = root.findall("product")
        return products

    def print_products(self):
        """Print products"""
        products = self._convert_xml_to_list_of_dict()
        print("PRODUCTS: ")
        print(f"===========================================")
        for product in products:
            for k, v in product.items():
                print(f"{k} ===> {v}")
            print(f"===========================================")

    def add_product(self, new_product: dict):
        """Add new product"""
        products = self._convert_xml_to_list_of_dict()
        if not self.check_if_items_exists(new_product["name"], products):
            products.append(new_product)
            self._write_to_xml(products)
            print(f"Product {new_product} was added.")
        else:
            print(f"Product {new_product['name']} already exists")

    def _convert_xml_to_list_of_dict(self):
        """Serialisation"""
        prod_list = []
        products = self._get_products()
        for product in products:
            name = product.find("name")
            price = product.find("price")
            quantity = product.find("quantity")

            prod_dict = {
                "name": name.text if name is not None else "Unknown",
                "price": price.text if price is not None else "0",
                "quantity": quantity.text if quantity is not None else "0"
            }
            prod_list.append(prod_dict)
        return prod_list

    def _write_to_xml(self, product_list: list):
        """convert dict and wright it to xml"""
        products_element = etree.Element("products")
        for product in product_list:
            product_element = etree.SubElement(products_element, "product")
            etree.SubElement(product_element, "name").text = product["name"]
            etree.SubElement(product_element, "price").text = str(
                product["price"])
            etree.SubElement(product_element, "quantity").text = str(
                product["quantity"])

        tree = etree.ElementTree(products_element)
        tree.write(self.file_name, encoding="utf-8", xml_declaration=True,
                   pretty_print=True)

    def change_quantity(self, product_name, new_quantity):
        """method that changes quantity of existing items"""
        products = self._convert_xml_to_list_of_dict()
        try:
            if not self.check_if_items_exists(product_name, products):
                raise ValueError(
                    f'Item {product_name} does not exists. You should add it '
                    f'firstly.')
            for product in products:
                if product['name'] == product_name:
                    product['quantity'] = new_quantity
            self._write_to_xml(products)
        except ValueError as e:
            print(e)
        else:
            print(
                f"Quantity of product {product_name} was changed to "
                f"{new_quantity}.")

    @staticmethod
    def check_if_items_exists(item_name, collection):
        """Check if items with given name exists"""
        check_flag = False
        for item_ex in collection:
            if item_ex["name"] == item_name:
                check_flag = True
        return check_flag


if __name__ == "__main__":
    file_name = "products.xml"
    xml_reader = ReadXml(file_name)
    xml_reader.print_products()
    new_product = {"name": "Brandy", "price": 100, "quantity": 200}
    xml_reader.add_product(new_product)
    xml_reader.print_products()
    xml_reader.change_quantity("Wiskey", '500')
