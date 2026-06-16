# Topic: Decorators
# Example: Login required decorator

def login_required(func):
    def wrapper(user):
        # get() safely reads login status from the dictionary.
        if user.get("logged_in"):
            return func(user)
        print("Access denied")
    return wrapper

@login_required
def view_dashboard(user):
    print("Welcome", user["name"])

view_dashboard({"name": "Asha", "logged_in": True})
view_dashboard({"name": "Rahul", "logged_in": False})
