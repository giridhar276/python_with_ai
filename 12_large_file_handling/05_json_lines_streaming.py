# Topic: Large File Handling
# Example: JSON Lines streaming

import os
import json

jsonl_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "events.jsonl")
os.makedirs(os.path.dirname(jsonl_file), exist_ok=True)

with open(jsonl_file, "w", encoding="utf-8") as file:
    for i in range(1, 6):
        file.write(json.dumps({"event_id": i, "status": "success"}) + "\n")

with open(jsonl_file, "r", encoding="utf-8") as file:
    for line in file:
        event = json.loads(line)
        print(event)
