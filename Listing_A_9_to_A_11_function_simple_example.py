def my_function(a, b):
    return a + b 

def my_function(a=1, b=2):
    return a + b 

def my_function(*args, **kwargs):
    print (f"args --> {args}")
    print (f"kwargs --> {kwargs}")

print (my_function(100, 200, a=300, b=400))