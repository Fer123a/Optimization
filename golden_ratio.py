import math

gr = (math.sqrt(5) + 1)/2


def golden_ratio(foo, min_max, a, b, tol=1e-5, max_iter=100):
    """
    This method computes the maximum or minimum value
    of a unimodal algebraic function over a closed interval
    using the Golden Section Search algorithm.
    """
    n = 0
    c = b - (b-a)/gr
    d = a + (b-a)/gr

    if min_max == "min":
        while abs(b - a) > tol*(abs(c)+abs(d)):
            # TODO: Find out why the stop criteria above is recommended.
            # The stop criteria above is used in literature and in scipy pack.
            # while abs(b - a) > tol:
            if foo(c) < foo(d):
                b = d
                d = c

                c = b - (b-a)/gr

            else:
                a = c
                c = d

                d = a + (b-a)/gr

            n += 1

            if n == max_iter:
                raise RuntimeError("The number of iterations reached "
                                   "the defined maximum number of iterations.")

        else:
            return (a+b)/2, foo((a+b)/2), n

    # TODO: Implement the steps to find the maximum of a function
    if min_max == "max":
        pass
