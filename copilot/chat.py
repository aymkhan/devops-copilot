'''
Author: Aymen Khan
Oct 2026
Create an AI driven chat so the user can ask follow up questions.
'''

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

system_prompt = '''
You are a friendly DevOps helper for beginners.
Answer in plain, simple English.
Keep answers short: 3 to 5 sentences, unless the user asks for more.
'''

def ask(chat_messages):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        temperature=0,
        messages=[{"role":"system","content":system_prompt}] + chat_messages
    )
    print("tokens sent: ", response.usage.prompt_tokens)
    raw = response.choices[0].message.content
    return raw


if __name__ == "__main__":
    # Give the model "memory" so it can answer follow up questions
    history = []
    while True:
        question = input("You: ")
        if question == "quit" or question == "exit":
            break
        history.append({"role":"user", "content":question})
        reply = ask(history[-6:]) # we are only sending a range of last 3 turns (input + reply). From the 6th item (from the end) all the way to the end
        print(f"ChatBot: ", reply)
        history.append({"role":"assistant","content":reply})

