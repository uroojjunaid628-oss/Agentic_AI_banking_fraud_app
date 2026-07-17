import os

from dotenv import load_dotenv
from groq import Groq


# Load environment variables
load_dotenv()


class LLMService:
    """
    Handles communication with the Groq Large Language Model.
    """

    def __init__(self):
        """
        Initialize the Groq client.
        """

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.model = "llama-3.1-8b-instant"


    def generate_response(self, prompt):
        """
        Send a prompt to the LLM and return its response.
        """

        try:

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2
            )

            return response.choices[0].message.content

        except Exception as error:

            print(f"LLM Error:\n{error}")

            return None        