import math
def find_greatest_common_divisor_iterative(num_1, num_2):
    # make sure num_1 >= num_2
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1

    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1

def find_greatest_common_divisor_recursive(num_1, num_2):
    # make sure num_1 >= num_2
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1

    if num_2 == 0:
        return num_1
    else:
        return find_greatest_common_divisor_recursive(num_2, num_1 % num_2)

if __name__ == "__main__":
    num_1, num_2 = 153, 123
    print (math.gcd(num_1, num_2))
    print (find_greatest_common_divisor_iterative(num_1, num_2))
    print (find_greatest_common_divisor_recursive(num_1, num_2))
