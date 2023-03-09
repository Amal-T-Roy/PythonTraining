

def decorator_function(original_function):
    def inner_function():
        print('In inner func')
        return original_function()
    return inner_function

@decorator_function
def display():
    print('In display function:')

# x = decorator_function(display)
display()
