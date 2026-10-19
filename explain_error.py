################################
# Author: Aymen Khan
# October 2026
# DevOps Helper/Copilot agent
################################

from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, ConfigDict
from typing import Literal

load_dotenv()
client = Groq()

system_prompt = """
You are a friendly DevOps helper.
You explain errors to beginners in simple, plain English.
Keep your answer short.

Always answer in JSON with exactly these keys:

"is_error" : true if the message is an error, false if not.
"confidence" : how sure you are about the cause of the error:
	"high" = the error message clearly shows the cause 
	"medium" = there is a likely cause, but other causes are possible
	"low" = the error is too vague to know the cause
"what_happened" : "one or two sentences explaining the error"
"likely_cause" : "the most likely reason this happened"
"steps" : ["up to 3 steps, simplest first. Do not number them"]
"if_not_fixed" : "which details or commands would help investigate further"

Only return the JSON. No other text.

Rules:
If you are not sure about the error, then say so. Do not guess.
Only suggest commands that really exist. Do not make up commands or options.
If a step could delete data or stop a running service, warn the user first.
If the message is not an error, say so and ask the user to paste the error.
"""

#error = """
#Error response from daemon: driver failed programming external connectivity
#on endpoint web: Bind for 0.0.0.0:8080 failed: port is already allocated
#"""
error = open("error.txt").read()


# Create a template (class) which will be our blueprint. 
# Then we'll have Pydantic create the schema for us based on the blueprint
class ErrorExplanation(BaseModel):
	model_config = ConfigDict(extra = "forbid")
	is_error : bool
	confidence : Literal["high", "medium", "low"]
	what_happened : str
	likely_cause : str
	steps : list[str]
	if_not_fixed : str


response = client.chat.completions.create(
    model = "openai/gpt-oss-20b",
    temperature = 0,
    response_format = {
	"type" : "json_schema",
	"json_schema" : {"name" : "error_explainer", "strict" : True, "schema" : ErrorExplanation.model_json_schema()}
},
    messages = [
	{"role" : "system", "content" : system_prompt},
	{"role" : "user", "content" : error},
	],
    )

raw = response.choices[0].message.content

answer = ErrorExplanation.model_validate_json(raw)

if not answer.is_error:
	print("This is not an error. Please share a valid error message")
else:
	print("Confidence: ", answer.confidence)
	print("What happened:", answer.what_happened)
	print("Likely cause:", answer.likely_cause)
	print("What to try:")
	for step in answer.steps:
		print("- ", step)
	print("If this doesn't fix it:", answer.if_not_fixed)
