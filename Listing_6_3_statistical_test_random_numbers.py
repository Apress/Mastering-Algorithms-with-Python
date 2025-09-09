import scipy.stats as stats 
import random
random.seed(1234)

class StatisticalTestRandomNumbers:
    def __init__(self, nums):
        self.nums = nums 
        self.N = len(self.nums)

    def count_num_plus_minus(self, plus_and_minus):
        if not plus_and_minus:
            return 
            
        count = 1
        last_seen = plus_and_minus[0]
        for i in range(1, len(plus_and_minus)):
            cur_sign = plus_and_minus[i]
            if cur_sign == last_seen:
                continue
            else:
                count += 1
                last_seen = cur_sign
        return count 

    def uniformity_chi_square_test(self, k):
        E, remainder = divmod(self.N, k)
        if remainder != 0:
            raise Exception(f"The random numbers cannot be equally divided into {k} parts")
             
        interval_size = 1. / k 
        chi_square = 0
        for i in range(k):
            O = 0
            lower_bound = i * interval_size
            upper_bound = (i + 1) * interval_size
            for num in self.nums:
                if lower_bound <num <= upper_bound:
                    O += 1
            chi_square += (O - E)**2 / E 
        chi_square_table_value = stats.chi2.ppf(0.95, k-1)
        print (f"chisquare = {chi_square}")
        if chi_square > chi_square_table_value:
            return False
        return True

    def independence_up_and_down_test(self):
        plus_and_minus = []
        for i in range(1, self.N):
            if self.nums[i] >= self.nums[i-1]:
                plus_and_minus.append("+")
            else:
                plus_and_minus.append("-")
        A = self.count_num_plus_minus(plus_and_minus)
        n = self.N 
        u = (2*n - 1) / 3
        sigma = ((16 * n - 29) / 90)**0.5
        z0 = abs((A - u) / sigma) 
        # alpha = 0.05 
        print (f"z0 = {z0}")
        if z0 > 1.96: 
            return False
        return True 

    def independence_above_and_below_mean_test(self):
        plus_and_minus = []
        n1 = 0 # number of observations >=0.5
        n2 = 0 # number of observations <0.5
        n = self.N 
        for num in self.nums:
            if num >= 0.5:
                plus_and_minus.append("+")
                n1 += 1
            else:
                plus_and_minus.append("-")
                n2 += 1
        B = self.count_num_plus_minus(plus_and_minus)
        u = 2 * n1 * n2 / n + 0.5
        sigma = (2 * n1 * n2 *(2 * n1 * n2 - n) / (n**2 * (n-1)))**0.5 
        z0 = abs((B - u) / sigma) 
        print (f"z0 = {z0}")
        if z0 > 1.96: 
            return False
        return True 

    def independence_correlation_test(self):
        n = self.N 
        corr_sum = 0
        for i in range(n - 1):
            corr_sum += self.nums[i] * self.nums[i+1]
        rou = (12. / (n-1)) * corr_sum - 3.
        sigma = ((13 * n - 19) / (n -1)**2)**0.5 
        z0 = rou / sigma 
        print (f"z0 = {z0}")
        if z0 > 1.96:
            return False
        return True 

if __name__ == "__main__": 
    rand_nums_from_python = [random.random() for _ in range(10000)]  
    test_random_nums = StatisticalTestRandomNumbers(nums = rand_nums_from_python)
    # chi square test
    print (test_random_nums.uniformity_chi_square_test(5))
    # up and down test
    print (test_random_nums.independence_up_and_down_test())
    # above and below mean test
    print (test_random_nums.independence_above_and_below_mean_test())
    # correlation test
    print (test_random_nums.independence_correlation_test())

    
