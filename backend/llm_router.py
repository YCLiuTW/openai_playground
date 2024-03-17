import json
import os
from utils import (
    encode_image_from_file,
    Prompt,
    ClothAttributesReponse,
    SimpleQAReponse,
    ClothesDatabase,
    DBReponse,
)
from llm_caller import stream_openai_reponse
from fastapi import APIRouter


OPENAI_KEY = "your_openai_keys"
prompt = Prompt()
router = APIRouter()
clothes_db = ClothesDatabase(os.path.join("pants_db"))


@router.post("/simple_qa")
async def simple_QA(message: str) -> SimpleQAReponse:
    messages = [
        {
            "role": "user",
            "content": message,
        }
    ]

    openai_response_message = await stream_openai_reponse(
        messages=messages, api_key=OPENAI_KEY, model_type="GPT4_PREVIEW"
    )

    simple_qa_reponse = SimpleQAReponse(
        answer=openai_response_message, state=200, message="successfully retrive answer"
    )
    return simple_qa_reponse.dict()


@router.post("/cloth_attribute_retrieve")
async def cloth_attributes_retrive(base64_img_str: str) -> ClothAttributesReponse:
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt.get_prompt("analysis_image")},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_img_str}"},
                },
            ],
        }
    ]

    openai_response_message = await stream_openai_reponse(
        messages=messages, api_key=OPENAI_KEY, model_type="GPT4_IMAGE_PREVIEW"
    )

    json_dict = json.loads(openai_response_message)
    cloth_attributes = ClothAttributesReponse(
        cloth_color=json_dict["cloth_color"],
        cloth_size=json_dict["cloth_size"],
        state=200,
        message="Successfully retrive cloth attribute from image.",
    )

    return cloth_attributes.dict()


@router.post("/find_in_db")
async def find_similar_clothes(base64_img_str: str) -> DBReponse:

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt.get_prompt("analysis_image")},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_img_str}"},
                },
            ],
        }
    ]

    openai_response_message = await stream_openai_reponse(
        messages=messages, api_key=OPENAI_KEY, model_type="GPT4_IMAGE_PREVIEW"
    )

    json_dict = json.loads(openai_response_message)
    similar_cloth_path, cloth_popularity = clothes_db.retrieve_like_clothes(
        cloth_attributes={
            "cloth_color": json_dict["cloth_color"],
            "cloth_size": json_dict["cloth_size"],
        }
    )

    similar_cloth = DBReponse(
        cloth_color=json_dict["cloth_color"],
        cloth_size=json_dict["cloth_size"],
        similar_cloth=encode_image_from_file(similar_cloth_path),
        cloth_popularity=cloth_popularity,
        state=200,
        message="Successfully retrive cloth attribute from image.",
    )

    return similar_cloth.dict()


if __name__ == "__main__":
    print("hi")
