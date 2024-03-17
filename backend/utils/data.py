from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel
from typing import Dict, Literal, List


ANALYSIS_IMAGE_PROMPT = """
Asume you are a fashion designer, be in charge give some opinions from clothes from image.
- When color of cloth is bright, you consider CLOTH_COLOR is light, otherwise CLOTH_COLOR is dark.
- When cloth looks tight on person, you consider CLOTH_SIZE is tight, otherwise CLOTH_SIZE is loose.

Return only the dictionary in format {"cloth_color": CLOTH_COLOR, "cloth_size": CLOTH_SIZE} .
"""


class LLMType:
    @staticmethod
    def get_regular_model_type(model_type: str) -> str:
        """
        Get regular llm model name that OpenAI support!
        """
        models = {
            "GPT4": "gpt-4",
            "GPT4_PREVIEW": "gpt-4-turbo-preview",
            "GPT4_TURBO_PREVIEW": "gpt-4-turbo-preview",
            "GPT4_IMAGE_PREVIEW": "gpt-4-vision-preview",
        }
        if model_type not in models:
            raise NotImplementedError(f"Model type : {model_type} is not support!")
        return models[model_type]


class Prompt:
    prompt_dict = {"analysis_image": ANALYSIS_IMAGE_PROMPT}

    def get_prompt(self, prompt_type: str) -> str:
        """
        Get prompt with simple Factory-pattern in design-pattern.
        """
        # checking prompt type is support.
        if prompt_type not in self.prompt_dict:
            raise NotImplementedError(f"Prompt type {prompt_type} is not support!")
        prompt = self.prompt_dict[prompt_type]
        return prompt


class APIDict(BaseModel):
    model: str
    messages: List[ChatCompletionMessageParam]
    stream: bool
    timeout: int
    max_tokens: int
    temperature: int


class ClothAttributesReponse(BaseModel):
    cloth_color: str
    cloth_size: str
    state: int
    message: str


class DBReponse(BaseModel):
    cloth_color: str
    cloth_size: str
    similar_cloth: str
    cloth_popularity: float
    state: int
    message: str


class SimpleQAReponse(BaseModel):
    answer: str
    state: int
    message: str
