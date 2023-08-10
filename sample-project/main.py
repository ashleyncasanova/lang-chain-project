# Example OpenAI script for generating super hero names for animals

import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    print("Missing OPENAI_API_KEY environment variable.")
    exit()

animal = input("Animal: ")

prompt = f"""Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {animal.capitalize()}
Names:"""

response = openai.Completion.create(
    model="text-curie-001",
    prompt=prompt,
    temperature=0.7,
    max_tokens=60,
)

print(response)