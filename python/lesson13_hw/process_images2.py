"""Module with class ProcessImage"""
import concurrent.futures
import os
import shutil
from typing import Tuple, Set

from PIL import Image


class ProcessImage:
    """
    A class for processing images, such as resizing them in a given directory.
    """

    def __init__(self, image_dir: str) -> None:
        """
        Initializes the ProcessImage class with a specified image directory.

        :param image_dir: Path to the directory containing images to be
        processed.
        :raises FileNotFoundError: If the specified directory does not exist.
        """
        if not os.path.exists(image_dir):
            raise FileNotFoundError(f"{image_dir} does not exist")
        self.image_dir = image_dir

    def resize_image(self, image_name: str, output_folder: str,
                     new_size: Tuple[int, int]) -> int:
        """
        Resizes a single image and saves it to the output folder.

        :param image_name: Name of the image file to resize.
        :param output_folder: Directory where the resized image will be saved.
        :param new_size: Target dimensions (width, height) for resizing.
        :return: The process ID (PID) of the worker handling the image.
        """
        print(f"[PID {os.getpid()}] Processing: {image_name}")

        # Ensure output directory exists
        os.makedirs(output_folder, exist_ok=True)

        if image_name.lower().endswith(("png", "jpg", "jpeg")):
            try:
                image_path = os.path.join(self.image_dir, image_name)
                image = Image.open(image_path)
                image = image.resize(new_size)
                image.save(os.path.join(output_folder, image_name))
                os.remove(image_path)  # Remove original image after processing
            except Exception as error:
                print(f"Error processing {image_name}: {error}")

        return os.getpid()

    def resize_images_in_folder(self, output_folder: str,
                                new_size: Tuple[int, int]) -> None:
        """
        Processes all images in the specified directory concurrently.

        :param output_folder: Directory where resized images will be saved.
        :param new_size: Target dimensions (width, height) for resizing.
        """
        images = [img for img in os.listdir(self.image_dir) if
                  img.lower().endswith(("png", "jpg", "jpeg"))]

        # Process images using multiple processes
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(self.resize_image, images,
                                   [output_folder] * len(images),
                                   [new_size] * len(images))

        # Collect unique process IDs used in the execution
        unique_pids: Set[int] = set(results)
        print(f"Processed {len(images)} images.")
        print(f"Used processes: {unique_pids} (Total: {len(unique_pids)})\n")


if __name__ == "__main__":
    # Define input and output directories
    ORIGIN_DIR: str = os.path.join("images", "images_origin")
    IMAGES_IN_DIR: str = os.path.join("images", "images_in")
    IMAGES_OUT_DIR: str = os.path.join("images", "images_out")

    # Ensure the input directory exists
    os.makedirs(IMAGES_IN_DIR, exist_ok=True)

    # Copy images from ORIGIN_DIR to IMAGES_IN_DIR if they do not already exist
    for file_name in os.listdir(ORIGIN_DIR):
        source_path: str = os.path.join(ORIGIN_DIR, file_name)
        destination_path: str = os.path.join(IMAGES_IN_DIR, file_name)

        if os.path.isfile(source_path) and not os.path.exists(
                destination_path):
            shutil.copy2(source_path, destination_path)

    # Create an instance of ProcessImage and start processing
    proc_img = ProcessImage(IMAGES_IN_DIR)
    proc_img.resize_images_in_folder(IMAGES_OUT_DIR, (300, 300))
