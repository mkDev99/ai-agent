import sys
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types

if len(sys.argv) >= 2:
    user_prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
        ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
            )

    print(response.text)
    
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":

        usage = response.usage_metadata
        print(f"\nUser prompt: {user_prompt}")
        print(f"\nPrompt tokens: {usage.prompt_token_count}\nResponse tokens: {usage.candidates_token_count}")
else:
    print("No prompt given")
    sys.exit(1)
