# Topic: User Defined Functions
# Example: Keyword arguments

def create_profile(**details):
    # items() returns key-value pairs from keyword arguments.
    for key, value in details.items():
        print(key, ":", value)

create_profile(name="Asha", role="Data Engineer", location="Bangalore")
