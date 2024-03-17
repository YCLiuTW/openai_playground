from typing import Awaitable, Callable, Dict, List
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionChunk
from utils import LLMType, APIDict


async def stream_openai_reponse(
    messages: List[ChatCompletionMessageParam],
    api_key: str,
    model_type: str,
    timeout: int = 600,
    max_token: int = 4096,
) -> str:
    client = AsyncOpenAI(api_key=api_key)

    # setting up AsyncOpenai payload
    model_type = LLMType.get_regular_model_type(model_type)
    params = APIDict(
        model=model_type,
        messages=messages,
        stream=True,
        timeout=timeout,
        max_tokens=max_token,
        temperature=0,
    ).dict()
    stream = await client.chat.completions.create(**params)
    full_response: str = ""
    async for chunk in stream:  # type: ignore
        assert isinstance(chunk, ChatCompletionChunk)
        content = chunk.choices[0].delta.content or ""
        full_response += content

    await client.close()
    return full_response
