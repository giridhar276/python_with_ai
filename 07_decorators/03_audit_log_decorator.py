# Topic: Decorators
# Example: Audit log decorator

def audit_log(func):
    def wrapper(*args, **kwargs):
        print("AUDIT started:", func.__name__)
        result = func(*args, **kwargs)
        print("AUDIT completed:", func.__name__)
        return result
    return wrapper

@audit_log
def approve_leave(employee_name):
    print("Leave approved for", employee_name)

approve_leave("Asha")
