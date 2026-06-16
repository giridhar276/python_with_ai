# Topic: Config Handling
# Example: Mask secret value

api_key = "abcd1234secretvalue"

def mask_secret(secret):
    return secret[:4] + "****" + secret[-4:]

print(mask_secret(api_key))
