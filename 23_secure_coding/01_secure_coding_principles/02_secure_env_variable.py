"""
Example 2: Secure Configuration Using Environment Variables

Concept:
Use environment variables instead of hardcoding secrets.

How to run on Mac/Linux:
export APP_API_KEY="sample-api-key"
python 02_secure_env_variable.py

How to run on Windows CMD:
set APP_API_KEY=sample-api-key
python 02_secure_env_variable.py

How to run on Windows PowerShell:
$env:APP_API_KEY="sample-api-key"
python 02_secure_env_variable.py
"""

import os

api_key = os.getenv("APP_API_KEY")

if not api_key:
    print("APP_API_KEY is not set.")
    print("Please set the environment variable before running this script.")
else:
    print("API key loaded successfully from environment variable.")
    print("For security, we should not print the actual API key.")
