import os
from utils import encode_image, check_file_exist, WebDict

OPENAI_KEY = "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"


def main():
    image_path = os.path.join('test_image', 'tight_jeans.png')
    check_file_exist(image_path)
    base64_image: str = encode_image(image_path=image_path)

    header_dict = WebDict.get_headers_dict(OPENAI_KEY)
    json_load = WebDict.get_payload(base64_image=base64_image)
    print(header_dict)
    print(json_load)


if __name__ == '__main__':
    main()
