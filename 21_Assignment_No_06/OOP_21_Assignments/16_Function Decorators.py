# This is the decorator function
def log_function_call(func):
    # Inner function that adds extra behavior
    def wrapper():
        print("Function is being called")  # Message before calling the function
        func()  # Call the original function
    return wrapper  # Return the inner function

# Apply the decorator to the say_hello function
@log_function_call
def say_hello():
    print("Say Hello")  # Original function message

# Call the decorated function
say_hello()
