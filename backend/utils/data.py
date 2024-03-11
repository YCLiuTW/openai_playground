from typing import Literal, TypedDict


ANALYSIS_IMAGE_PROMPT = """
Asume you are a fashion designer, be in charge give some opinions from clothes from image.
- When color of cloth is bright, you consider CLOTH_COLOR is light, otherwise CLOTH_COLOR is dark.
- When cloth looks tight on person, you consider CLOTH_SIZE is tight, otherwise CLOTH_SIZE is loose.

Return only the dictionary in format { 'cloth_color' : CLOTH_COLOR, 'cloth_size': CLOTH_SIZE} .
"""


class Prompt:
    prompt_dict = {'analysis_image': ANALYSIS_IMAGE_PROMPT}

    def get_prompt(self, prompt_type: str) -> str:
        """
        Get prompt with simple Factory-pattern in design-pattern.
        """
        # checking prompt type is support.
        if prompt_type not in self.prompt_dict:
            raise NotImplementedError(f'Prompt type {prompt_type} is not support!')
        prompt = self.prompt_dict[prompt_type]
        return prompt


class WebDict:

    @staticmethod
    def get_headers_dict(open_api_key: str):
        header = {"Content-Type": "application/json", "Authorization": f"Bearer {open_api_key}"}
        return header

    @staticmethod
    def get_payload(base64_image: str, prompt: str = "What’s in this image?"):

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                        },
                    ],
                }
            ],
            "max_tokens": 300,
        }
        return payload
