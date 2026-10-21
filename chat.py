'''
Author: Aymen Khan
Oct 2026
Create an AI driven chat so the user can ask follow up questions.
'''

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

def ask(message):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        temperature=0,
        messages=message
    )
    print("tokens sent: ", response.usage.prompt_tokens)
    raw = response.choices[0].message.content
    return raw

# Give the model "memory" so it can answer follow up questions
history = []

while True:
    question = input("You: ")
    if question == "quit":
        break
    history.append({"role":"user", "content":question})
    reply = ask(history[-6:]) # we are only sending a range of last 3 turns (input + reply). From the 6th item (from the end) all the way to the end
    print(f"ChatBot: ", reply)
    history.append({"role":"assistant","content":reply})

