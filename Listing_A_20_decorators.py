from functools import lru_cache, wraps 
@lru_cache
def fibonacci(n):
    if n <=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

class MyClass:
    def __init__(self, nums):
        self.nums = nums 

    @staticmethod
    def calculate_squares(x):
        return x**2 

    def squaring_arr(self):
        return [MyClass.calculate_squares(num) for num in self.nums]

def introduction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print ("Before introducing myself...")
        func(*args, **kwargs)
        print ("After introducing myself...")
    return wrapper

@introduction
def greet(name):
    print (f"Hello my name is {name}")

if __name__ == "__main__":
    print (fibonacci(100))
    my_class = MyClass(nums = [1,2,3,4,5])
    print(my_class.calculate_squares(10))
    print(my_class.squaring_arr())
    greet("Thomas")
