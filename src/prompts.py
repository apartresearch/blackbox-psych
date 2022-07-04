import asyncio
import json
import openai  # type: ignore
from typing import List


def read_json(filename: str) -> dict:
    with open(filename) as f:
        return json.load(f)


def get_api_key(config, keyname: str = "goose_api") -> str:
    """
    Gets the API key from the config file.
    """
    return read_json(config)[keyname]


def authenticate_goose(config) -> None:
    """
    Authenticates with the goose API.
    """
    api_key = get_api_key(config, keyname="goose_api")
    openai.api_key = api_key
    openai.api_base = "https://api.goose.ai/v1"


def generate_prompt(
    prompt: str,
    model_name: str = "gpt-neo-125m",
    max_tokens: int = 75,
    temperature=0.9,
    stop_token=None,
) -> str:
    """
    Generates a prompt using a model from EleutherAI.
    """
    return openai.Completion.create(
        prompt=prompt,
        engine=model_name,
        max_tokens=max_tokens,
        temperature=temperature,
        stop=stop_token,
    )["choices"][0]["text"]


def generate_n_prompts(
    prompt,
    n_completions: int = 1,
    model_name: str = "gpt-neo-125m",
    temperature=0.9,
    max_tokens=25,
    stop_token=None,
) -> List[str]:
    """
    Generates a prompt using a model from EleutherAI.
    """
    raw_response = openai.Completion.create(
        prompt=prompt,
        engine=model_name,
        n=n_completions,
        max_tokens=max_tokens,
        temperature=temperature,
        stop=stop_token,
    )
    return [response["text"] for response in raw_response.choices]

