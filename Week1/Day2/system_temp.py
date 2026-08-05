import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"
prompt = "suggest name for my food brand and also suggest tagline for my food brand"

massage_system={"role": "system", "content": "you are my brand manager who suggest name for my food brand and also suggest tagline for my food brand"}

message = {"role": role, "content": prompt}
messages = [massage_system, message]

response = client.chat.completions.create(model=model, messages=messages,temperature=2.0)

# Print only the generated text content
print(response.choices[0].message.content)