import base64
from PIL import Image
from io import BytesIO


def decode_base64_to_PIL(base64_image_str: str):
    image = Image.open(BytesIO(base64.b64decode(base64_image_str)))
    return image


def encode_PIL_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    base64_img_code = base64.b64encode(buffered.getvalue())
    return base64_img_code
