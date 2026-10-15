from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    # temperature controls the "randomness" of the response (0 = steady, higher = more varied)
    # temperature=1.5,
    messages=[
        {"role": "user", "content": "Explain what an API is in one sentence."},
    ],
)

print(response.choices[0].message.content)
