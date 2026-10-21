'''
Author: Aymen Khan
Oct 2026
Test the model's memory
'''

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

def ask(message):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        temperature=0,
        messages= message
    )
    raw = response.choices[0].message.content
    return raw
'''
question_1 = [{"role" : "user", "content": "My favorite tool is Docker"}]
question_2 = [{"role" : "user", "content": "What is my favorite tool?"}]
print(ask(question_1))
print("\n ******************")
print(ask(question_2))
'''

# Give the model "memory"
history = []

history.append({"role" : "user", "content" : "My favorite tool is Docker"})
# Now history has one item (message in a Dictionary format)
reply = ask(history)
print(f"AI reply to statement about Docker is: ", reply)

history.append({"role":"assistant", "content": reply})
print("\n*******************")

history.append({"role":"user", "content":"Give me some helpful course names for my favorite tool"})
reply = ask(history)
print(f"AI reply to SECOND question: ", reply)
history.append({"role":"assistant", "content": reply})



