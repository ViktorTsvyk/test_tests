#import pytest
from .tenv import TEnv

from devsure.rpc.test.rpc_to_bpm_emu.tools import PinState
from devsure.time_simulator import SimulatedTimeScope, SimulatedThread
from PIL import Image
import os
from types import SimpleNamespace

# ---------------------------------------
# def rand_pause():
#     pause_sec = random.randint(0, 3)
#     time.sleep(pause_sec)
# ---------------------------------------

def _capture_screen(tenv: TEnv, suffix = None) -> None:
    _capture_screen._counter += 1
    fileName = f"captures/test_001_img_{_capture_screen._counter}"
    if suffix:
        fileName += f"_{suffix}"
    tenv.emulator.screen_image.save(f"{fileName}.png", format="png")
_capture_screen._counter = 0

def verify_image(actual, expected, mask = None):
    """Compare `actual` and `expected` images using `mask`, and generate a difference image.

    - Matching pixels → White (255, 255, 255)
    - Masked pixels → Black (0, 0, 0)
    - Non-matching pixels → Red (255, 0, 0)

    Args:
        actual (Image): The actual image.
        expected (Image): The expected image.
        mask (Image): The mask image (black = ignore, white = compare).

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

    _capture_screen._counter += 1

    # report_folder = "captures"
    report_folder = os.getenv("DEVSURE_REPORT_FOLDER")
    actual.save(f"{report_folder}/test_001_img_{_capture_screen._counter}_actual.png", format="png")
    expected.save(f"{report_folder}/test_001_img_{_capture_screen._counter}_expected.png", format="png")
    diff_image.save(f"{report_folder}/test_001_img_{_capture_screen._counter}_difference.png", format="png")

    assert all_match == True

    return all_match

images_dir = os.path.dirname(os.path.abspath(__file__)) + "/Screens"

def load_images():
    images = {}

    for filename in os.listdir(images_dir):
        if filename.lower().endswith(".png"):
            name = os.path.splitext(filename)[0]  # Remove extension for dot access
            path = os.path.join(images_dir, filename)
            images[name] = Image.open(path)

    return SimpleNamespace(**images)  # Convert dictionary to SimpleNamespace

def test_navigation(tenv: TEnv) -> None:
    images = load_images()

    with SimulatedTimeScope(f"Test Case"):
        SimulatedThread.sleep_ms(100)
        #_capture_screen(tenv) # home
        verify_image(tenv.emulator.screen_image, images.Home)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Menu.Measurement
        verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Measurement
        verify_image(tenv.emulator.screen_image, images.Measurement)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Menu.Measurement
        verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.History
        verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # History
        verify_image(tenv.emulator.screen_image, images.History)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Menu.Measurement
        verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.History
        verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.Visit
        verify_image(tenv.emulator.screen_image, images.Menu_3_Visit, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Visit
        verify_image(tenv.emulator.screen_image, images.Visit)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Menu.Measurement
        verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.History
        verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.Visit
        verify_image(tenv.emulator.screen_image, images.Menu_3_Visit, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.Exit
        verify_image(tenv.emulator.screen_image, images.Menu_4_Exit, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # home
        verify_image(tenv.emulator.screen_image, images.Home)

