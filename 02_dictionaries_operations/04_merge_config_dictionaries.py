# Topic: Dictionaries
# Example: Merge configuration dictionaries

default_config = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO"
}

prod_config = {
    "timeout": 60,
    "log_level": "ERROR"
}

final_config = {**default_config, **prod_config}

print(final_config)
