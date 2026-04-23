from django.conf import settings
from openai import OpenAI
from . import prompts


class SGEAgent:

    def __init__(self):
        self.__client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def invoke(self):
        response = self.__client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    'role': 'system',
                    'content': prompts.SYSTEM_PROMPT,
                },
                {
                    'role': 'user',
                    'content': prompts.USER_PROMPT,
                },
            ]
        )
        result = response.choices[0].message.content
        return result