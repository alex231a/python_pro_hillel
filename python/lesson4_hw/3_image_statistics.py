from PIL import Image
import os
import csv


class ImageIterator:
    """Class for iterating over an image"""

    def __init__(self, target_dir: str, storage_file: str):
        self.target_dir = target_dir
        self.storage_file = storage_file
        self.image_files = []
        self.index = 0

    def __iter__(self):
        for filename in os.listdir(self.target_dir):
            self.image_files.append(filename)
        return self

    def __next__(self):
        if self.index >= len(self.image_files):
            raise StopIteration
        filename = self.image_files[self.index]
        self.index += 1
        return filename

    def get_metadata_from_image(self, filename: str):
        """Method for getting metadata from an image"""
        image_path = os.path.join(self.target_dir, filename)
        with Image.open(image_path) as img:
            width, height = img.size
            format = img.format
            mode = img.mode
            metadata = {
                'Filename': filename,
                'Width': width,
                'Height': height,
                'Format': format,
                'Mode': mode
            }
            return metadata

    def write_data_to_file(self):
        """Method for writing data to file"""
        with open(self.storage_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file,
                                    fieldnames=['Filename', 'Width', 'Height',
                                                'Format', 'Mode'])
            if file.tell() == 0:
                writer.writeheader()

            for filename in self:
                metadata = self.get_metadata_from_image(filename)
                writer.writerow(metadata)


if __name__ == '__main__':
    discovery = ImageIterator('images', 'images_metadata.csv')
    discovery.write_data_to_file()

