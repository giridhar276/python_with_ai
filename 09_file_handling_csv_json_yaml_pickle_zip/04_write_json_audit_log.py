# Topic: File Handling
# Example: Write JSON

import os
import json
from datetime import datetime

output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "audit_log.json")
os.makedirs(os.path.dirname(output_file), exist_ok=True)

audit_data = {
    "event": "LOGIN",
    "user": "asha",
    "timestamp": datetime.now().isoformat()
}

with open(output_file, "w", encoding="utf-8") as file:
    # json.dump() writes Python data into JSON format.
    json.dump(audit_data, file, indent=4)

print(output_file)
