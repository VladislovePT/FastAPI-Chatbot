
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
import os
from dotenv import load_dotenv

load_dotenv()

def create_kernel():
    kernel = sk.Kernel()
    api_key = os.getenv("OPENAI_API_KEY")
    service_id = "chat-gpt"

    kernel.add_service(
        OpenAIChatCompletion(
            service_id=service_id,
            api_key=api_key,
            ai_model_id="gpt-4o"
        ),
    )

    return kernel
