from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

system_prompt = """
You are a friendly DevOps helper.
You explain errors to beginners in simple, plain English.
Keep your answer short.

Always answer in this format:

What happened:
One or two sentences explaining the error.

Likely cause:
The most likely reason this happened.

What to try:
Up to 3 numbered steps, simplest first.

If this doesn't fix it:
Say which details or commands would help investigate further.
"""

error = """
Error response from daemon: driver failed programming external connectivity
on endpoint web: Bind for 0.0.0.0:8080 failed: port is already allocated
"""


response = client.chat.completions.create(
    model = "openai/gpt-oss-20b",
    temperature = 0,
    messages = [
	{"role" : "system", "content" : system_prompt},
	{"role" : "user", "content" : error},
	],
    )

print(response.choices[0].message.content)
