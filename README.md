# DevOps Copilot

An AI helper that explains error messages in plain English.

Paste an error and get a simple explanation of what went wrong and what to try next. You can ask follow-up questions about the error.

## How to run

1. Create a virtual environment and install the libraries:

   ```bash
   python3 -m venv .venv
   .venv/bin/pip install -r requirements.txt
   ```

2. Get a free API key at https://console.groq.com, then copy `.env.example` to `.env` and add your key:

   ```bash
   cp .env.example .env
   ```

3. Put an error message in `error.txt` and start the copilot:

   ```bash
   .venv/bin/python copilot_chat.py
   ```

   Ask follow-up questions, or type `quit` or `exit` to stop.

4. Run the evals (from the main folder):

   ```bash
   .venv/bin/python -m evals.run_evals
   ```

## Project layout

```
copilot/          the app: error explainer and chat
evals/            test set and eval script
experiments/      small learning scripts
copilot_chat.py   start here
```

## Planned
- Search my own notes and guides for answers
- Investigate problems step by step
