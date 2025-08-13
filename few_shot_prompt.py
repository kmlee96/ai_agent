from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
model_ver = os.getenv("MODEL_VER")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model=model_ver,
    temperature=0.9,
    messages=[
        {"role": "system", "content": "you are an animal sound creator"},
        {"role": "user", "content": "dog"},
        {"role": "assistant", "content": "bow wow"},
        {"role": "user", "content": "cat"},
        {"role": "assistant", "content": "meow"},
        {"role": "user", "content": "bird"},
    ]
)

print(response)

print("----")
print(response.choices[0].message.content)