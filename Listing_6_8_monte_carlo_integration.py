import matplotlib.pyplot as plt 
import numpy as np 
from scipy import integrate
np.random.seed(1234)

class MonteCarloIntegration:
    def __init__(self, n, a, b, xmin, xmax, ymin, ymax):
        self.n = n # 1000000
        self.a = a # 0
        self.b = b # 5
        self.xmin = xmin
        self.xmax = xmax 
        self.ymin = ymin 
        self.ymax = ymax 

    # define function
    def func(self, x):
        return (10 * x**4 + 15 * x**3 + 25 * x**2 + 35 * x + 50)**0.2 * np.exp(-x) 

    # plot curve
    def plot_func(self):
        x_arr = np.linspace(self.a, self.b, self.n)
        y_arr= self.func(x_arr)
        plt.plot(x_arr, y_arr, "b-", lw=2)
        plt.xlim([self.a,self.b])
        plt.xlabel("X", fontsize = 12)
        plt.ylabel("Y", fontsize = 12)
        plt.savefig("xxx.jpg", dpi=600)
        plt.tight_layout()
        plt.show()

    def area_under_curve_rectangle(self):
        # Riemann sum
        dx = (self.b-self.a) / self.n
        sigma_sum = np.sum(self.func(self.a + np.arange(1, self.n + 1) * dx))
        auc = dx * (sigma_sum)
        return auc 

    def area_under_curve_trapezoid(self):
        dx = (self.b - self.a)/self.n 
        sigma_sum = np.sum(self.func(self.a + np.arange(1, self.n)*dx))
        auc = dx * (self.func(self.a) * 0.5 + self.func(self.b) * 0.5 + sigma_sum)
        return auc 

    def monte_carlo_mean_value_method(self):
        dx = (self.b - self.a) / self.n 
        Us = np.random.uniform(size = self.n)
        I = dx * np.sum(self.func(self.a + (self.b-self.a) * Us))
        return I 

    def monte_carlo_area_ratio_method(self):
        rectangle_area = (self.xmax - self.xmin) * (self.ymax - self.ymin) 
        random_pts_x = np.random.uniform(self.xmin,self.xmax,self.n)
        random_pts_y = np.random.uniform(self.ymin,self.ymax,self.n)
        pts_below_curve = np.sum(self.func(random_pts_x) > random_pts_y)
        I = rectangle_area * pts_below_curve / self.n 
        return I 

    # Scipy Integration
    def scipy_quad_integration(self):
        I, error = integrate.quad(self.func, self.a, self.b)
        return I 

    def run_with_different_methods(self):
        try:
            I_rectangle = self.area_under_curve_rectangle()
            print (f"The integral is estimated to be {I_rectangle} via Riemann sum")
        except Exception as e: 
            print (e)

        try:
            I_trapezoid = self.area_under_curve_trapezoid()
            print (f"The integral is estimated to be {I_trapezoid} via Trapezoid method")
        except Exception as e:
            print (e)

        try:
            I_MC_mean_value = self.monte_carlo_mean_value_method()
            print (f"The integral is estimated to be {I_MC_mean_value} via Monte Carlo mean value method")
        except Exception as e:
            print (e)
        
        try:
            I_MC_area_ratio = self.monte_carlo_area_ratio_method()
            print (f"The integral is estimated to be {I_MC_area_ratio} via Monte Carlo area ratio method")
        except Exception as e:
            print (e)

        try:
            I_scipy_quad = self.scipy_quad_integration()
            print (f"The integral is estimated to be {I_scipy_quad} via SciPy quad integration")
        except Exception as e:
            print (e)
        
if __name__ == "__main__":
    smooth_integral = MonteCarloIntegration(1000000, 0, 5, 0, 5, 0, 2.2)
    smooth_integral.run_with_different_methods()
    rapid_varying_integral = MonteCarloIntegration(1000000, 0, 2, 0, 2, 0, 1)
    rapid_varying_integral.func = lambda x: (np.sin(1/(x * (2-x))))**2 
    rapid_varying_integral.run_with_different_methods()