# Topic: File Handling
# Example: Read YAML

import os

try:
    import yaml
except ImportError:
    print("Please install PyYAML: pip install pyyaml")
    raise SystemExit

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "app_config.yaml")

with open(file_path, "r", encoding="utf-8") as file:
    # safe_load() converts YAML content into Python data.
    config = yaml.safe_load(file)

print(config)
