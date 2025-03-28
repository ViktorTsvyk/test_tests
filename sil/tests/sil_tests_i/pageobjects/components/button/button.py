import time

from PIL.Image import Image
from pathlib import Path
from sil_test_i.Core.image_manager.image_manager import convert_img_to_np_array, convert_np_array_to_img, text_recognition, \
    get_image_via_np_array_by_path, get_text_center_coordinates, create_and_apply_mask, is_image_contains_sub_image, \
    convert_to_bgr, preprocess_image, preprocess_image2
from sil_test_i.Core.wait_manager.wait_manager import apply_waiter


@apply_waiter(lambda result: result is True)
def is_button_present(screen_image: Image, button_name):
    actual_image_np_array = convert_img_to_np_array(screen_image)
    actual_text = text_recognition(actual_image_np_array)
    return actual_text.find(button_name) != -1


@apply_waiter(lambda result: result is True)
def is_button_selected(screen_image: Image, button_name):
    path   = Path(__file__).parent / "button_selected_example.png"
    example_button_image_np_array = get_image_via_np_array_by_path(path)
    actual_image_np_array = convert_to_bgr(convert_img_to_np_array(screen_image))
    example_button_image_np_array = preprocess_image2(example_button_image_np_array)
    actual_image_np_array = preprocess_image2(actual_image_np_array)
    try:
        selected_button_in_current_screen_center_coords = get_text_center_coordinates(actual_image_np_array, button_name)
    except Exception as e:
        return False

    selected_button_in_current_screen = create_and_apply_mask(actual_image_np_array, screen_image.height, screen_image.width,
                                                  selected_button_in_current_screen_center_coords[0] - 160,
                                                  selected_button_in_current_screen_center_coords[0] + 160,
                                                  selected_button_in_current_screen_center_coords[1] - 30,
                                                  selected_button_in_current_screen_center_coords[1] + 30,
                                                  True)

    selected_button_in_current_screen = create_and_apply_mask(selected_button_in_current_screen, screen_image.height, screen_image.width,
                                                  selected_button_in_current_screen_center_coords[0] - 140,
                                                  selected_button_in_current_screen_center_coords[0] + 140,
                                                  selected_button_in_current_screen_center_coords[1] - 20,
                                                  selected_button_in_current_screen_center_coords[1] + 20,
                                                  False)


    # example_button_center_coords = get_text_center_coordinates(example_button_image_np_array, text_recognition(example_button_image_np_array))
    example_button_center_coords = (156, 30)
    """
    result of method:
    get_text_center_coordinates(example_button_image_np_array, text_recognition(example_button_image_np_array))
    data is set manually to reduce the execution time of the method
    """


    example_selected_button_image_with_mask = create_and_apply_mask(example_button_image_np_array,
                                                          example_button_image_np_array.shape[0],
                                                          example_button_image_np_array.shape[1],
                                                  example_button_center_coords[0] - 140,
                                                  example_button_center_coords[0] + 140,
                                                  example_button_center_coords[1] - 20,
                                                  example_button_center_coords[1] + 20,
                                                  False)

    result =  is_image_contains_sub_image(selected_button_in_current_screen, example_selected_button_image_with_mask)
    return result