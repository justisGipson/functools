def decorator(func):
    def actual_func(*args, **kwargs):
        """Inner function within decorator, which does the actual work"""
        print(f"Before Calling {func.__name__}")
        func(*args, **kwargs)
        print(f"After Calling {func.__name__}")

    return actual_func

@decorator
def greet(name):
    """Says hello to somebody"""
    print(f"Hello, {name}!")

greet("Martin")
# Before Calling greet
# Hello, Martin!
# After Calling greet
print(greet.__name__)
# actual_func
print(greet.__doc__)
# Inner function within decorator, which does the actual work
