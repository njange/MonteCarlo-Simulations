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