import time

import cv2
import numpy as np
import easyocr
from PIL import Image


reader = easyocr.Reader(["en"], gpu=False, verbose=False)

def convert_img_to_np_array(img):
    return np.array(img, dtype=np.uint8)


def convert_np_array_to_img(np_array):
    return Image.fromarray(np_array)


def apply_mask(image, mask):
    if image.shape[:2] != mask.shape[:2]:
        raise ValueError(f"Image size {image.shape[:2]} and mask size {mask.shape[:2]} are different")
    if image.ndim == 3 and image.shape[2] == 3:
        mask = mask[:, :, np.newaxis]
    masked_image = image * (mask // 255)
    return masked_image


def create_mask(height, width, start_x, end_x, start_y, end_y, inverted=False):
    mask = np.ones((height, width), dtype=np.uint8) * 255
    if inverted:
        mask[:, :] = 0
        mask[start_y:end_y, start_x:end_x] = 255
    else:
        mask[start_y:end_y, start_x:end_x] = 0
    return mask


def create_and_apply_mask(image, height, width, start_x, end_x, start_y, end_y, inverted=False):
    mask = create_mask(height, width, start_x, end_x, start_y, end_y, inverted)
    return apply_mask(image, mask)

def compare(image_path1, image_path2):
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    if image1 is None or image2 is None:
        raise ValueError("Image not found")

    if image1.shape != image2.shape:
        raise ValueError("Image size not matching")

    difference = cv2.absdiff(image1, image2)
    return not np.any(difference != 0)


def text_recognition(image):
    result = reader.readtext(image, detail=0)
    result = " ".join([item[1] for item in result])
    return result


def resize_image(image, scale=0.5):
    return cv2.resize(image, (0, 0), fx=scale, fy=scale)


def preprocess_image(image: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    return binary


def preprocess_image2(image: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    return gray


def get_text_center_coordinates(image, text):
    data = reader.readtext(image)

    for coordinates, label, confidence in data:
        if label == text:
            center_x = sum(x for x, y in coordinates) // len(coordinates)
            center_y = sum(y for x, y in coordinates) // len(coordinates)
            return center_x, center_y

    raise ValueError(f"Text '{text}' not found in image.")

def is_text_present(image, text):
    data = reader.readtext(convert_img_to_np_array(image))
    for item in data:
        label = item[1]
        if text in label:
            return True
    return False


def get_text(image):
    data = reader.readtext(convert_img_to_np_array(image))
    return [item[1] for item in data]



def get_image_via_np_array_by_path(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR_RGB)
    return image


def resize_image_via_np_array_by_path(image):
    scale_percent = 50  # Reduce by 50%
    new_width = int(image.shape[1] * scale_percent / 100)
    new_height = int(image.shape[0] * scale_percent / 100)
    image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    _, compressed_image = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
    image_bytes = compressed_image.tobytes()
    return image_bytes


def is_image_contains_sub_image(main_image, sub_image):
    if main_image is None or sub_image is None:
        raise ValueError("Error: one of images is None.")
    if len(main_image.shape) == 2:
        main_gray = main_image
    else:
        main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    if len(sub_image.shape) == 2:
        sub_gray = sub_image
    else:
        sub_gray = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
    main_mask = main_gray > 10
    sub_mask = sub_gray > 10
    main_h, main_w = main_gray.shape[:2]
    sub_h, sub_w = sub_gray.shape[:2]
    for y in range(main_h - sub_h + 1):
        for x in range(main_w - sub_w + 1):
            main_patch = main_gray[y:y + sub_h, x:x + sub_w]
            main_patch_mask = main_mask[y:y + sub_h, x:x + sub_w]
            valid_area = np.logical_and(main_patch_mask, sub_mask)
            if np.count_nonzero(valid_area) < 0.5 * np.count_nonzero(sub_mask):
                continue
            if np.all(main_patch[valid_area] == sub_gray[valid_area]):
                return True
    return False


def convert_to_bgr(image):
    if image.shape[2] == 4:
        return cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    return image
