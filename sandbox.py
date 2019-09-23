from golden_ratio import golden_ratio
from scipy import optimize
from sympy import symbols, diff, lambdify
import time
from gradient import grad
from newton import newton


def local_foo(x):
    return (x-2)**2


x, y, z = symbols("x y z")

"""
# -------------------- Function 1 --------------------
# region
print("============= Function 1 =============")

function = x**2 + y**2 + z**2

# init_values = [-10, 5, -9]
# init_values = [7, 3, 50]
init_values = [-90, 88, 65]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10

min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_1)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_2)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_3)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_4)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_5)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)
# endregion
"""

"""
# -------------------- Function 2 --------------------
# region

print("============= Function 2 =============")

function = 1000*x**2 + y**2 + z**2

init_values = [-96, 4, 22]
# init_values = [0, 87, 30]
# init_values = [-1, 2, 0]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10

min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_1)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)



min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_2)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_3)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_4)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_5)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)
# endregion
"""


# -------------------- Function 3 --------------------
# region
print("============= Function 3 =============")

function = 100000*x**2 + y**2 + z**2

# init_values = [500, 2, 0]
# init_values = [0, -2, 2]
init_values = [40, -2, 0]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10

min_x, min_value, n = newton(function, [x, y, z], init_values, tol=tolerance_1)

min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_1)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)



min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_2)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_3)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_4)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_5)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)
# endregion


"""
# -------------------- Function 4 --------------------
# region
print("============= Function 4 =============")

function = 100*(x**2-y)**2 +(1-x)**2

# init_values = [2, 2]
# init_values = [74, -6]
init_values = [-25, -10]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10

min_x, min_value, n = grad(function, [x, y], init_values, tol=tolerance_1)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y], init_values, tol=tolerance_2)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y], init_values, tol=tolerance_3)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y], init_values, tol=tolerance_4)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y], init_values, tol=tolerance_5)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)
# endregion
"""
"""
# -------------------- Function 5 --------------------
# region
print("============= Function 5 =============")

function = x**3 + y**3 + z**3

init_values = [-10, 5, -9]
# init_values = [7, 3, 50]
# init_values = [-90, 88, 65]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10

min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_1)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_2)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_3)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_4)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = grad(function, [x, y, z], init_values, tol=tolerance_5)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)
# endregion
"""

"""
xa, xb, xc, fa, fb, fc, funcalls = optimize.bracket(local_foo)

# region
# Sympy Sandbox
w = symbols('w')
function = (w-2)**2
function = lambdify(w, function)

tic = time.time()

min_x, min_value, iter = golden_ratio(function, "min", xa, xc)

toc = time.time()

print("\n", "Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", iter, "Time elapsed: ", toc-tic)

function = ((w-2)**3)/3
function = diff(function, w)
function = lambdify(w, function)

tic = time.time()

min_x, min_value, iter = golden_ratio(function, "min", xa, xc)

toc = time.time()

print("\n", "Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", iter, "Time elapsed: ", toc-tic)
# endregion

tic = time.time()

min_x, min_value, iter = golden_ratio(local_foo, "min", xa, xc)

toc = time.time()

print("\n", "Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", iter, "Time elapsed: ", toc-tic)

tic = time.time()

min_x, min_value, iter = optimize.golden(local_foo, brack=(xa, xc),
                                         full_output=True,
                                         tol=1e-5, maxiter=100)

toc = time.time()

print("\n", "Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", iter, "Time elapsed: ", toc-tic)
"""
