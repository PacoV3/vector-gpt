import logging
import openai
from chat_utils import ask
from app_secrets import OPENAI_API_KEY

if __name__ == "__main__":
    while True:
        user_query = input("Enter your question: ")
        openai.api_key = OPENAI_API_KEY
        logging.basicConfig(level=logging.WARNING,
                            format="%(asctime)s %(levelname)s %(message)s")
        logging.getLogger().setLevel(logging.INFO)
        print(ask(user_query))
