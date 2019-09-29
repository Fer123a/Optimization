from sympy import diff
from numpy import asarray, linalg, dot


def newton(foo, var_list, init_values, tol=1e-5, max_iter=10000,
           restric_low=None, restric_high=None):
    """
    This method computes the minimum value of a multivariable
    algebraic function using the Newton Algorithm,
    provided that a initial point is given.

    Parameters:
    foo: callable multivariable algebraic function, built with sympy;
    var_list: list containing independent variables of the function;
    init_values: list containing the initial values of the variables
                 provided in "var_list"
    tol: tolerance of the method;
    max_iter: maximum number of iteration allowed;
    restric_low: list containing the lower boundaries for the
                 variables values;
    restric_high: list containing the higher boundaries for the
                  variables values;
    """

    # Initial definitions and variables declaration
    n = 0
    current_values = asarray(init_values)
    previous_values = None
    previous_replacements = None
    gradient_vector = list()
    gradient_values = list()
    hessian_matrix = list()
    hessian_matrix_line = list()

    # Generate gradient vector analytically
    for var in var_list:
        gradient_vector.append(diff(foo, var))

    # Generate Hessian Matrix analytically
    for var in var_list:
        diff1 = diff(foo, var)
        for var2 in var_list:
            diff2 = diff(diff1, var2)
            hessian_matrix_line.append(diff2)
        hessian_matrix.append(hessian_matrix_line)
        hessian_matrix_line = list()

    # Perform the algorithm
    while n < max_iter:

        # Match each value with its corresponding variable,
        # to evaluate the hessian matrix, the gradient vector
        # and the objective function
        replacements = [(var, var_value) for var, var_value in
                        zip(var_list, current_values)]

        # Check if this is the first iteration, if not, check for stop criteria
        if n != 0:
            if linalg.norm(current_values - previous_values) < tol and \
               abs(foo.subs(replacements) -
               foo.subs(previous_replacements)) < tol and \
               linalg.norm(gradient_values) < tol:
                return current_values, foo.subs(replacements), n
            elif restric_high is not None or restric_low is not None:
                if linalg.norm(current_values - previous_values) < tol and \
                   abs(foo.subs(replacements) -
                   foo.subs(previous_replacements)) < tol:
                    return current_values, foo.subs(replacements), n

        gradient_values = list()

        # Evaluate Gradient Vector
        for index, _ in enumerate(gradient_vector):
            gradient_values.append(float(gradient_vector[index].
                                         subs(replacements)))

        gradient_values = asarray(gradient_values)

        # Evaluate Hessian Matrix
        hessian_values = list()
        hessian_values_line = list()
        for index1, _ in enumerate(var_list):
            for index2, _ in enumerate(var_list):
                hessian_values_line.append(float(
                                           hessian_matrix[index1][index2].
                                           subs(replacements)))

            hessian_values.append(hessian_values_line)
            hessian_values_line = list()

        hessian_values = asarray(hessian_values)

        hessian_values_inv = linalg.inv(hessian_values)

        # Save variable value of current iteration
        previous_values = current_values

        # Calculate variable values for next iteration
        current_values = previous_values - dot(hessian_values_inv,
                                               gradient_values.T)

        if restric_low is not None:
            for index, restriction in enumerate(restric_low):
                if current_values[index] < restriction:
                    current_values[index] = restriction

        if restric_high is not None:
            for index, restriction in enumerate(restric_high):
                if current_values[index] > restriction:
                    current_values[index] = restriction

        previous_replacements = replacements

        n += 1

    else:
        raise RuntimeError("The number of iterations reached "
                           "the defined maximum number of iterations.")
