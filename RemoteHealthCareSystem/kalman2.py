import random
import pylab
import numpy as np
from numpy.random import randn
temp=['2.69', '2.49', '2.35', '2.21', '2.17', '2.13', '2.14', '2.15', '2.09', '1.99', '1.91', '1.82', '1.71', '1.66', '1.64', '1.64', '1.67', '1.68', '1.69', '1.73', '1.78', '1.79', '1.81', '1.86', '1.88', '1.90', '1.95', '1.97', '1.99', '2.03', '2.07', '2.08', '1.98', '1.87', '1.74', '1.57', '1.43', '1.30', '1.18', '1.14', '1.09', '1.04', '1.01', '0.99', '0.93', '0.85', '0.77', '0.69', '0.61', '0.56', '0.52', '0.49', '0.48', '0.48']

temp = list(map(float, temp))
#print(temp)
#print(len(temp))
print(np.var(temp))
iteration_count = len(temp)
#actual_values = [3.51,3.42,3.34,3.17,3.04,2.98,2.83,0.76,0.62,2.58,2.44,0.37,0.29,2.15,0.93,0.45,1.33,0.27,0.87,1.07,0.9,0.8,0.6]

actual_values=temp
#print(actual_values)
iteration_count = len(actual_values)
#mean of zero and a standard deviation of one
noisy_measurement = [randn() * 0.3 - 0.3 + actual_val for actual_val in actual_values]
#print(random.random())

#process_variance = 1e-5
estimated_measurement_variance = np.var(temp)  # estimate of measurement variance, change to see effect

output = []
after_estimate = 0.0
after_error_estimate = 1.0

for iteration in range(1, iteration_count):
    before_estimate = after_estimate
    #print(before_estimate)

    before_error_estimate = after_error_estimate 
    #print(before_error_estimate)

    factor = before_error_estimate / (before_error_estimate + estimated_measurement_variance)
    #print(factor)

    after_estimate = before_estimate + factor * (noisy_measurement[iteration] - before_estimate)
    #print(after_estimate)

    after_error_estimate = (1 - factor) * before_error_estimate
    #print(after_error_estimate)

    output.append(after_estimate)

print(actual_values)
print("---------------------------------------------------")

print(output)
print("---------------------------------------------------")

print(noisy_measurement)
