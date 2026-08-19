import os
import openai
from dotenv import load_dotenv
from openai import OpenAI

from app.aws_help.models import AWSHelpResponse

load_dotenv()
client = OpenAI()

instructions = """You are an AWS Expert. Guide the user through solutions step by step.
                    Rules: Only respond to AWS related queries, respond with 'This is not an AWS Query' if the query is
                     a non AWS query in direct or indirect language
                    """
def get_help_streaming(prompt: str):
    try:
        stream = client.responses.create(
            model = os.getenv("MODEL",""),
            instructions = instructions,
            input = prompt,
            stream = True
        )
        for event in stream:
            if event.type == "response.output_text.delta":
                yield event.delta
    except openai.APITimeoutError:
        raise
    except openai.APIConnectionError:
        raise
    except openai.APIError:
        raise


def get_help(prompt: str):
    try:
        response = client.responses.parse(
            model = os.getenv("MODEL",""),
            instructions = """You are an AWS Expert. Guide the user through solutions step by step.
                    Rules: Only respond to AWS related queries, respond with 'This is not an AWS Query' if the query is
                     a non AWS query in direct or indirect language
                    """,
            input = prompt,
            text_format = AWSHelpResponse
        )
        return response.output_parsed
    except openai.APITimeoutError:
        raise
    except openai.APIConnectionError:
        raise
    except openai.APIError:
        raise