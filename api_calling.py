from dotenv import load_dotenv
import os
from google import genai

load_dotenv(dotenv_path=".env")

api_key = os.environ.get("GEMINI_API_KEY")
model = os.environ.get("MODEL")

client = genai.Client(api_key=api_key)

def debugCode(images,options):

    prompt=f"Solve the code error by the code image and give {options} for this code error like e professional Debugger"
    
    response = client.models.generate_content(
    model=model,
    contents=[images, prompt]
    )

    return response.text