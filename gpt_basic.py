from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
model_ver = os.getenv("MODEL_VER")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model=model_ver,
    temperature=0.1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "How many oceans are on earth?"},
    ]
)

print(response)

print("----")
print(response.choices[0].message.content)