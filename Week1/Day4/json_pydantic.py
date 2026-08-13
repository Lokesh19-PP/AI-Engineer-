import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel


load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"

class Ticket(BaseModel):
    name: str
    device: str
    location: str
    phone_number: str

schema = Ticket.model_json_schema()

# 1. Fixed response_format syntax ("type" as a string)
response_format = {
    "type": "json_object",
}

# 2. Defined 'text' BEFORE it is used in system_prompt
text = "Hello my name is lokesh, i have an iphone which is not working properly, i am living in pune , my no. is 1234567890, please help me to fix it"

system_prompt = f"""Extract the following information from the text: name, device, location, and phone number. 
The output should be in valid JSON format matching this schema structure keys: name, device, location, and phone_number. 
The text is: '{text}'"""

message_system = {
    "role": "system",
    "content": system_prompt
}

prompts = f"Extract the information into JSON format."

message = {
    "role": role,
    "content": prompts
}

# 3. Include both messages in the list so the system prompt is sent
messages = [message_system, message]

response = client.chat.completions.create(
    model=model, 
    messages=messages, 
    response_format=response_format
)

answer = response.choices[0].message.content

print(answer)



# isko padthe kase hai
import json
raw_json=answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.device)
print(ticket.location)
