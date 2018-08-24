from scipy.optimize import minimize
import numpy as np

def rosenbrock_3(x):
    """
    Define Rosenbrock Function under 3 dimension
    :param x: a vector 3*1
    :return: rosenbrock value for certain x
    """
    return (1 - x[0]) ** 2 + 100 * (x[2] - x[1] ** 2) ** 2 + (1 - x[1]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2

def derivative_3(x):
    """
    Define Rosenbrock Second order derivative under 3 dimension
    :param x: a vector 3*1
    :return: rosenbrock second order derivative value for certain x
    """
    return np.array([400 * x[0] ** 3 - 400 * x[1] * x[0] - 2 + 2 * x[0],400 * x[1] ** 3 - 400 * x[2] * x[1] - 200 * x[0] ** 2 - 2 + 202 * x[1], 200 * x[2] - 200 * x[1] ** 2])


if __name__ == '__main__':
    for i in range(10):
        x0 = np.random.uniform(5, 10, 3)
        min = minimize(rosenbrock_3, x0, method='L-BFGS-B', jac=derivative_3)
        print("Optimized Point:", min.x, "; Optimized Result:", min.fun)
