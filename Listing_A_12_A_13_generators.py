my_generator_1 = (num for num in range(1, 101))
my_generator_1.__next__()
my_generator_1_list = list(my_generator_1)

def my_generator_function(lower_bound, upperbound):
    for num in range(lower_bound, upperbound):
        yield num 

my_generator_2 = my_generator_function(1, 101)
my_generator_2.__next__()
my_generator_2_list = list(my_generator_2)