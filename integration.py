import random
import math

def monte_carlo_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    return 4 * inside_circle / num_samples
        
#Estimate pi using 1,000,000 samples

pi_estimate = monte_carlo_pi(1000000)
print(f"Estimated value of pi:{pi_estimate}")

# The monte_carlo_pi function uses the Monte Carlo method
#  to estimate the value of pi by generating random points
#  in a square and counting how many fall within a quarter circle. 
# The more points generated, the more accurate the estimate will be.
# The estimated value of pi is calculated as 4 times the ratio of points 
# inside the circle to the total number of points generated. 
# The function returns this estimate. 
# In this example, we use 1,000,000 samples to estimate pi and print the result.