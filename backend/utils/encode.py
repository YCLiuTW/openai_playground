import base64


def encode_image_from_file(image_path) -> str:
    """
    Encode image file to base64 string.
    """
    with open(image_path, "rb") as image_file:
        base64_img_code = base64.b64encode(image_file.read()).decode("utf-8")
    return base64_img_code
