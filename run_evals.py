'''
Author: Aymen Khan
October 2026
Evals script to run against each test from test_set.json
'''

import json
from explain_error import explain_error

# open/read the test set file
tests = json.load(open("test_set.json"))

# counter for passed tests
passed = 0

for test in tests:
    expected = test["expected"]
    '''Always declare the answer variable inside a try/catch block, so that even if the cloud hosted provider (Groq) rejects the response due to
    invalid response data/shape, it doesn't crash our application. Instead, the exception gets thrown for the bad test and the app continues
    with the rest of the tests.
    '''
    try:
        answer = explain_error(test["input"])
    except Exception as e:
        print("FAIL ", test["id"], "- the API call failed: ", e)
        continue
    # create an empty list to keep track of problems we may catch
    problems = []

    # Compare each item from 'expected' field to the answer/response
    if answer.is_error != expected["is_error"]:
        problems.append(f"is_error was: {answer.is_error}")
    if expected["is_error"]:
        if answer.confidence not in expected["confidence"]:
            problems.append(f"confidence was {answer.confidence}")
        # combine the contents of the steps list from real answer into one long str so it can be looped over to find the keywords
        full_text_steps = " ".join([answer.what_happened, answer.likely_cause, *answer.steps]).lower()
        # capture each keyword from the test_json expected steps so they could be checked against individually
        keywords = expected["mention_any"]
        if keywords: # check if keywords list is empty or not
            found = False
            for word in keywords:
                if word.lower() in full_text_steps:
                    found = True
                    break
            if not found:
                problems.append(f"didn't mention any of {keywords}")

    if problems:
        print(f"FAIL ", test["id"], "-", "; ".join(problems))
    else:
        print(f"PASS ", test["id"])
        passed += 1

print(f"\nScore: {passed} / {len(tests)}")




