from golden_ratio import golden_ratio
from sympy import symbols, diff, lambdify
from numpy import asarray, linalg
from scipy import optimize


def grad(foo, var_list, init_values, tol=1e-5, max_iter=10000):
    """
    This method computes the minimum value of a multivariable
    algebraic function using the Gradient Descent algorithm,
    provided that a initial point is given.

    Parameters:
    foo: callable multivariable algebraic function built with sympy;
    var_list: list containing independent variables of the function;
    init_values: list containing the initial values of the variables
                 provided in "var_list"
    tol: tolerance of the method;
    max_iter: maximum number of iteration allowed;
    """

    # Initial definitions and variables declaration
    alpha = symbols("alpha")
    n = 0
    current_values = asarray(init_values)
    previous_values = None
    previous_replacements = None
    gradient_vector = list()
    gradient_values = list()

    # Generate gradient vector analytically
    for var in var_list:
        gradient_vector.append(diff(foo, var))

    # Perform Gradient Descent Algorithm
    while n < max_iter:

        replacements = [(var, var_value) for var, var_value in
                        zip(var_list, current_values)]

        # Check if this is the first iteration, if not, check for stop criteria
        if n != 0:
            if linalg.norm(current_values - previous_values) < tol and \
               abs(foo.subs(replacements) -
               foo.subs(previous_replacements)) < tol and \
               linalg.norm(gradient_values) < tol:
                return current_values, foo.subs(replacements), n

        gradient_values = list()

        for index, _ in enumerate(gradient_vector):
            gradient_values.append(float
                                   (gradient_vector[index].subs(replacements)))

        gradient_values = asarray(gradient_values)

        alpha_foo_arg = current_values - alpha*gradient_values

        alpha_replacements = [(var, var_value) for var, var_value in
                              zip(var_list, alpha_foo_arg)]

        alpha_foo = foo.subs(alpha_replacements)

        alpha_foo = lambdify(alpha, alpha_foo)

        # Perform bracketing for determining the boundaries for line sarch
        xa, _, xc, _, _, _, _ = optimize.bracket(alpha_foo)

        # Perform line search for minimizing "alpha"
        # using the Golden Section Method
        min_alpha, _, _ = golden_ratio(alpha_foo, "min", xa, xc)

        # Save variable value of current iteration
        previous_values = current_values

        # Calculate variable values for next iteration
        current_values = previous_values - min_alpha*gradient_values

        previous_replacements = replacements

        n += 1

    else:
        raise RuntimeError("The number of iterations reached "
                           "the defined maximum number of iterations.")
