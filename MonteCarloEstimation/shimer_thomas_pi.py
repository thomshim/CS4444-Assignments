import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def estimate_pi(n):
    count = 0 # count of points that land in circle
    for i in range(1,n):
        x_coord = np.random.uniform(-1,1)
        y_coord = np.random.uniform(-1,1)
        if math.sqrt(x_coord**2+y_coord**2) < 1:
            count += 1
    # Area of square => (2*r)^2 => 4*r^2
    # Area of circle => pi*r^2
    # Area Square/ Area Circle = (4*r^2)/(pi*r^2) = 4/pi
    # pi = 4 * points in circle / points in square
    return count * 4 / n
def question_two():
    # Estimate from 1 to 10000
    n_values = list(range(1, 100))
    pi_estimates = [estimate_pi(n) for n in n_values]
    # Log x plot
    plt.figure(figsize=(18, 10))
    plt.semilogx(n_values, pi_estimates, marker='o', markersize=1, color='blue', linestyle='None')  # valid args
    plt.axhline(y=math.pi, color='r', linestyle=':', label='Actual π')
    plt.xlabel('Number of points (n)')
    plt.ylabel('Estimated π Value')
    plt.title('Estimation of π using Monte Carlo method')
    plt.ylim(1, 4.0)
    plt.legend()
    plt.grid(True)
def question_three():
    n_values = [10 , 10 ** 2, 10 ** 3]
    R = 500
    plt.figure(figsize=(18, 10))
    for i, n in enumerate(n_values):
        estimates = [estimate_pi(n) for _ in range(R)]
        #Used AI for help graphing this section
        plt.subplot(1, 3, i + 1)
        sns.histplot(estimates, kde=True, stat='count', bins=20, color='skyblue')
        plt.axvline(math.pi, color='r', linestyle=':', label='π')
        plt.title(f"Sampling Distribution of π Estimates\nn={n}, R={R}")
        plt.xlabel('Estimated π')
        plt.ylabel('Frequency')
        plt.legend()
        plt.grid(True)

#question_two()
#question_three()