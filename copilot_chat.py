'''
Author: Aymen Khan
October 2026
DevOps Helper/Copilot chatbot
'''

from copilot.explain_error import explain_error
from copilot.chat import ask
import sys

'''
1. @error - Receive the initial 'error' input/message from the user
2. @answer - Let the AI respond to the error
3. Print the AI response in the defined structured format 
4. Start the chat so the user can ask follow up questions for that 'error' (You: , AI: )
To do this, the history[] list won't be sent empty. Instead, it will be sent with the original 'error' message and the first AI answer. 
'''
error = open("error.txt").read()
answer = explain_error(error)

if not answer.is_error:
    print("This is not an error. Please restart the app and share an error message so I can help you debug.")
    sys.exit()

history = [
    {"role":"user", "content":error},
    {"role":"assistant", "content":answer.model_dump_json()} # Make sure the answer is always sent in TEXT/JSON format here
]

print("What happened:", answer.what_happened)
print("Likely cause:", answer.likely_cause)
print("Steps:")
for step in answer.steps:
    print("- ", step)

# Now start the chat
while True:
    print("\n")
    question = input("You: ")
    if question == "quit" or question == "exit":
        break
    history.append({"role":"user", "content": question})
    reply = ask(history[:2] + history[2:][-4:])
    history.append({"role":"assistant", "content": reply})
    print("AI: ", reply)

