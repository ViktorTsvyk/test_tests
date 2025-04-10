import logging
import os
from PIL import Image
from types import SimpleNamespace
from devsure.formal import GetFormalReport


logging.getLogger("PIL.PngImagePlugin").setLevel(logging.INFO)

images_dir = os.path.dirname(os.path.abspath(__file__)) + "/Screens"

def load_images():
    images = {}

    for filename in os.listdir(images_dir):
        if filename.lower().endswith(".png"):
            name = os.path.splitext(filename)[0]  # Remove extension for dot access
            path = os.path.join(images_dir, filename)
            images[name] = Image.open(path)

    return SimpleNamespace(**images)  # Convert dictionary to SimpleNamespace

def capture_image(image, suffix = None) -> None:
    capture_image._counter += 1
    fileName = f"captures/img_{capture_image._counter}"
    if suffix:
        fileName += f"_{suffix}"
    image.save(f"{fileName}.png", format="png")
capture_image._counter = 0


def verify_image(actual: Image.Image, expected: Image.Image, mask: Image.Image = None):
    """Compare `actual` and `expected` images using `mask`, and generate a difference image.

    - Matching pixels → White (255, 255, 255)
    - Masked pixels → Black (0, 0, 0)
    - Non-matching pixels → Red (255, 0, 0)

    Args:
        actual: The actual image.
        expected: The expected image.
        mask: The mask image (black = ignore, white = compare).

    Returns:
        Image: The difference image.
    """

    # Ensure all images are in RGB mode
    actual = actual.convert("RGB")
    expected = expected.convert("RGB")

    # Get pixel data
    actual_pixels = actual.load()
    expected_pixels = expected.load()

    width, height = actual.size
    diff_image = Image.new("RGB", (width, height))
    diff_pixels = diff_image.load()

    all_match = True

    if mask:
        mask = mask.convert("L")  # Convert mask to grayscale
        mask_pixels = mask.load()

        for y in range(height):
            for x in range(width):
                if mask_pixels[x, y] == 0:  # Masked area (ignore)
                    diff_pixels[x, y] = (0, 0, 0)  # Black
                elif actual_pixels[x, y] == expected_pixels[x, y]:  # Matching pixels
                    diff_pixels[x, y] = (255, 255, 255)  # White
                else:  # Mismatched pixels
                    diff_pixels[x, y] = (255, 0, 0)  # Red
                    all_match = False
    else:
        for y in range(height):
            for x in range(width):
                if actual_pixels[x, y] == expected_pixels[x, y]:  # Matching pixels
                    diff_pixels[x, y] = (255, 255, 255)  # White
                else:  # Mismatched pixels
                    diff_pixels[x, y] = (255, 0, 0)  # Red
                    all_match = False

    capture_image._counter += 1

    # report_folder = "captures"
    report_folder = os.getenv("DEVSURE_REPORT_FOLDER")
    actual_file = f"img_{capture_image._counter}_actual.png"
    expected_file = f"img_{capture_image._counter}_expected.png"
    diff_file = f"img_{capture_image._counter}_difference.png"

    actual.save(f"{report_folder}/{actual_file}", format="png")
    expected.save(f"{report_folder}/{expected_file}", format="png")
    diff_image.save(f"{report_folder}/{diff_file}", format="png")

    GetFormalReport().register_evidence("image", actual_file, expected_file, diff_file)

    return all_match