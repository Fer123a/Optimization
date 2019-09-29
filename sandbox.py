from golden_ratio import golden_ratio
from scipy import optimize
from sympy import symbols, diff, lambdify, cos, sin, log
from numpy import array, transpose, dot
import time
from gradient import grad
from newton import newton
from pandas import DataFrame
import pandas as pd
import xlsxwriter


def local_foo(x):
    return (x-2)**2


x, y, z = symbols("x y z")



"""
# region -------------------- Function 1 --------------------
print("============= Function 1 =============")

function = x**2 + y**2 + z**2

# init_values = [-10, 5, -9]
init_values = [7, 3, 50]
# init_values = [-90, 88, 65]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10

min_x, min_value, n = newton(function, [x, y, z], init_values, tol=tolerance_1)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = newton(function, [x, y, z], init_values, tol=tolerance_2)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = newton(function, [x, y, z], init_values, tol=tolerance_3)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = newton(function, [x, y, z], init_values, tol=tolerance_4)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)


min_x, min_value, n = newton(function, [x, y, z], init_values, tol=tolerance_5)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
print("Argument at minimum value: ", min_x, "Minimum value: ",
      min_value, "Number of iterations: ", n)
# endregion
"""



"""
# region -------------------- Function 2 --------------------

print("============= Function 2 =============")

function = 1000*x**2 + y**2 + z**2

# init_values = [-96, 4, 22]
init_values = [0, 87, 30]
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



"""
# region -------------------- Function 3 --------------------
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

min_x_1, min_value_1, n_1 = newton(function, [x, y, z], init_values, tol=tolerance_1)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
print("Argument at minimum value: ", min_x_1, "Minimum value: ",
      min_value_1, "Number of iterations: ", n_1)

min_x_2, min_value_2, n_2= newton(function, [x, y, z], init_values, tol=tolerance_2)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
print("Argument at minimum value: ", min_x_2, "Minimum value: ",
      min_value_2, "Number of iterations: ", n_2)


min_x_3, min_value_3, n_3 = newton(function, [x, y, z], init_values, tol=tolerance_3)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
print("Argument at minimum value: ", min_x_3, "Minimum value: ",
      min_value_3, "Number of iterations: ", n_3)


min_x_4, min_value_4, n_4 = newton(function, [x, y, z], init_values, tol=tolerance_4)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
print("Argument at minimum value: ", min_x_4, "Minimum value: ",
      min_value_4, "Number of iterations: ", n_4)


min_x_5, min_value_5, n_5 = newton(function, [x, y, z], init_values, tol=tolerance_5)

print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
print("Argument at minimum value: ", min_x_5, "Minimum value: ",
      min_value_5, "Number of iterations: ", n_5)

l1 = [None, None, None, 'Valores Iniciais', 'Valores Finais', 'Valores Finais', 'Valores Finais', 'Valores Finais',
      'Valores Finais']
l2 = [None, None, 'x', init_values[0], min_x_1[0], min_x_2[0], min_x_3[0], min_x_4[0], min_x_5[0]]
l3 = [None, None, 'y', init_values[1], min_x_1[1], min_x_2[1], min_x_3[1], min_x_4[1], min_x_5[1]]
l4 = [None, None, 'z', init_values[2], min_x_1[2], min_x_2[2], min_x_3[2], min_x_4[2], min_x_5[2]]
l5 = [None, None, 'Tolerância Utilizada', None, tolerance_1, tolerance_2, tolerance_3, tolerance_4, tolerance_5]
l6 = [None, None, 'Valor da Função Objetivo', None, min_value_1, min_value_2, min_value_3, min_value_4, min_value_5]
l7 = [None, None, 'Número de Iterações', None, n_1, n_2, n_3, n_4, n_5]


df = DataFrame({" ":["" for _  in range(len(l1))], "  ": l1, "   ": l2, "    ": l3, "     ": l4, "      ": l5,
               "             ": l6, "       ": l7})

df.to_excel('test.xlsx', sheet_name='sheet1', index=False)


# endregion
"""



"""
# region -------------------- Function 4 --------------------
print("============= Function 4 =============")

function = 100*(x**2-y)**2 + (1-x)**2

init_values_1 = [2, 2]
init_values_2 = [74, -6]
init_values_3 = [-25, -10]

init_values_list = [init_values_1, init_values_2, init_values_3]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

for index, init_values in enumerate(init_values_list):
    rol = 4
    col = 4

    min_x_1, min_value_1, n_1 = newton(function, [x, y], init_values, tol=tolerance_1)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
    print("Argument at minimum value: ", min_x_1, "Minimum value: ",
            min_value_1, "Number of iterations: ", n_1)

    min_x_2, min_value_2, n_2= newton(function, [x, y], init_values, tol=tolerance_2)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
    print("Argument at minimum value: ", min_x_2, "Minimum value: ",
            min_value_2, "Number of iterations: ", n_2)


    min_x_3, min_value_3, n_3 = newton(function, [x, y], init_values, tol=tolerance_3)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
    print("Argument at minimum value: ", min_x_3, "Minimum value: ",
            min_value_3, "Number of iterations: ", n_3)


    min_x_4, min_value_4, n_4 = newton(function, [x, y], init_values, tol=tolerance_4)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
    print("Argument at minimum value: ", min_x_4, "Minimum value: ",
            min_value_4, "Number of iterations: ", n_4)


    min_x_5, min_value_5, n_5 = newton(function, [x, y], init_values, tol=tolerance_5)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
    print("Argument at minimum value: ", min_x_5, "Minimum value: ",
            min_value_5, "Number of iterations: ", n_5)

    l1 = [None, None, None, 'Valores Iniciais', 'Valores Finais', 'Valores Finais', 'Valores Finais', 'Valores Finais',
            'Valores Finais']
    l2 = [None, None, 'x', init_values[0], min_x_1[0], min_x_2[0], min_x_3[0], min_x_4[0], min_x_5[0]]
    l3 = [None, None, 'y', init_values[1], min_x_1[1], min_x_2[1], min_x_3[1], min_x_4[1], min_x_5[1]]
    # l4 = [None, None, 'z', init_values[2], min_x_1[2], min_x_2[2], min_x_3[2], min_x_4[2], min_x_5[2]]
    l5 = [None, None, 'Tolerância Utilizada', None, tolerance_1, tolerance_2, tolerance_3, tolerance_4, tolerance_5]
    l6 = [None, None, 'Valor da Função Objetivo', None, min_value_1, min_value_2, min_value_3, min_value_4, min_value_5]
    l7 = [None, None, 'Número de Iterações', None, n_1, n_2, n_3, n_4, n_5]

    for item1, item2, item3, item5, item6, item7 in zip(l1, l2, l3, l5, l6, l7):
        worksheet.write(rol+11*index, col, item1)
        worksheet.write(rol+11*index, col+1, item2)
        worksheet.write(rol+11*index, col+2, item3)
        #worksheet.write(rol+11*index, col+3, item4)
        worksheet.write(rol+11*index, col+3, item5)
        worksheet.write(rol+11*index, col+4, item6)
        worksheet.write(rol+11*index, col+5, item7)
        rol += 1

workbook.close()

    # df = DataFrame({" ":["" for _  in range(len(l1))], "  ": l1, "   ": l2, "    ": l3, "      ": l5,
    #            "             ": l6, "       ": l7})


    # df.to_excel('test.xlsx', sheet_name='sheet1', index=False, header=False,
    #            startrow=3+10*(index), startcol=3)

# endregion
"""



"""
# region -------------------- Function 5 --------------------
print("============= Function 5 =============")

function = x**3 + y**3 + z**3

init_values_1 = [-10, 5, -9]
init_values_2 = [7, 3, 50]
init_values_3 = [-90, 88, 65]

init_values_list = [init_values_1, init_values_2, init_values_3]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

for index, init_values in enumerate(init_values_list):
    rol = 4
    col = 4

    min_x_1, min_value_1, n_1 = newton(function, [x, y, z], init_values, tol=tolerance_1)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
    print("Argument at minimum value: ", min_x_1, "Minimum value: ",
            min_value_1, "Number of iterations: ", n_1)

    min_x_2, min_value_2, n_2= newton(function, [x, y, z], init_values, tol=tolerance_2)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
    print("Argument at minimum value: ", min_x_2, "Minimum value: ",
            min_value_2, "Number of iterations: ", n_2)


    min_x_3, min_value_3, n_3 = newton(function, [x, y, z], init_values, tol=tolerance_3)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
    print("Argument at minimum value: ", min_x_3, "Minimum value: ",
            min_value_3, "Number of iterations: ", n_3)


    min_x_4, min_value_4, n_4 = newton(function, [x, y, z], init_values, tol=tolerance_4)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
    print("Argument at minimum value: ", min_x_4, "Minimum value: ",
            min_value_4, "Number of iterations: ", n_4)


    min_x_5, min_value_5, n_5 = newton(function, [x, y, z], init_values, tol=tolerance_5)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
    print("Argument at minimum value: ", min_x_5, "Minimum value: ",
            min_value_5, "Number of iterations: ", n_5)

    l1 = [None, None, None, 'Valores Iniciais', 'Valores Finais', 'Valores Finais', 'Valores Finais', 'Valores Finais',
            'Valores Finais']
    l2 = [None, None, 'x', init_values[0], min_x_1[0], min_x_2[0], min_x_3[0], min_x_4[0], min_x_5[0]]
    l3 = [None, None, 'y', init_values[1], min_x_1[1], min_x_2[1], min_x_3[1], min_x_4[1], min_x_5[1]]
    l4 = [None, None, 'z', init_values[2], min_x_1[2], min_x_2[2], min_x_3[2], min_x_4[2], min_x_5[2]]
    l5 = [None, None, 'Tolerância Utilizada', None, tolerance_1, tolerance_2, tolerance_3, tolerance_4, tolerance_5]
    l6 = [None, None, 'Valor da Função Objetivo', None, min_value_1, min_value_2, min_value_3, min_value_4, min_value_5]
    l7 = [None, None, 'Número de Iterações', None, n_1, n_2, n_3, n_4, n_5]

    for item1, item2, item3, item4, item5, item6, item7 in zip(l1, l2, l3, l4, l5, l6, l7):
        worksheet.write(rol+11*index, col, item1)
        worksheet.write(rol+11*index, col+1, item2)
        worksheet.write(rol+11*index, col+2, item3)
        worksheet.write(rol+11*index, col+3, item4)
        worksheet.write(rol+11*index, col+4, item5)
        worksheet.write(rol+11*index, col+5, item6)
        worksheet.write(rol+11*index, col+6, item7)
        rol += 1

workbook.close()
# endregion
"""



"""
# region -------------------- Function 6 --------------------
print("============= Function 6 =============")

function = 5*x**2 + 5*y**2 - x*y -11*x + 11*y + 11

init_values_1 = [-10, 5]
init_values_2 = [7, 3]
init_values_3 = [-90, 88]

init_values_list = [init_values_1, init_values_2, init_values_3]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10


workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

for index, init_values in enumerate(init_values_list):
    rol = 4
    col = 4

    min_x_1, min_value_1, n_1 = newton(function, [x, y], init_values, tol=tolerance_1)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
    print("Argument at minimum value: ", min_x_1, "Minimum value: ",
            min_value_1, "Number of iterations: ", n_1)

    min_x_2, min_value_2, n_2= newton(function, [x, y], init_values, tol=tolerance_2)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
    print("Argument at minimum value: ", min_x_2, "Minimum value: ",
            min_value_2, "Number of iterations: ", n_2)


    min_x_3, min_value_3, n_3 = newton(function, [x, y], init_values, tol=tolerance_3)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
    print("Argument at minimum value: ", min_x_3, "Minimum value: ",
            min_value_3, "Number of iterations: ", n_3)


    min_x_4, min_value_4, n_4 = newton(function, [x, y], init_values, tol=tolerance_4)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
    print("Argument at minimum value: ", min_x_4, "Minimum value: ",
            min_value_4, "Number of iterations: ", n_4)


    min_x_5, min_value_5, n_5 = newton(function, [x, y], init_values, tol=tolerance_5)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
    print("Argument at minimum value: ", min_x_5, "Minimum value: ",
            min_value_5, "Number of iterations: ", n_5)

    l1 = [None, None, None, 'Valores Iniciais', 'Valores Finais', 'Valores Finais', 'Valores Finais', 'Valores Finais',
            'Valores Finais']
    l2 = [None, None, 'x', init_values[0], min_x_1[0], min_x_2[0], min_x_3[0], min_x_4[0], min_x_5[0]]
    l3 = [None, None, 'y', init_values[1], min_x_1[1], min_x_2[1], min_x_3[1], min_x_4[1], min_x_5[1]]
    # l4 = [None, None, 'z', init_values[2], min_x_1[2], min_x_2[2], min_x_3[2], min_x_4[2], min_x_5[2]]
    l5 = [None, None, 'Tolerância Utilizada', None, tolerance_1, tolerance_2, tolerance_3, tolerance_4, tolerance_5]
    l6 = [None, None, 'Valor da Função Objetivo', None, min_value_1, min_value_2, min_value_3, min_value_4, min_value_5]
    l7 = [None, None, 'Número de Iterações', None, n_1, n_2, n_3, n_4, n_5]

    for item1, item2, item3, item5, item6, item7 in zip(l1, l2, l3, l5, l6, l7):
        worksheet.write(rol+11*index, col, item1)
        worksheet.write(rol+11*index, col+1, item2)
        worksheet.write(rol+11*index, col+2, item3)
        #worksheet.write(rol+11*index, col+3, item4)
        worksheet.write(rol+11*index, col+3, item5)
        worksheet.write(rol+11*index, col+4, item6)
        worksheet.write(rol+11*index, col+5, item7)
        rol += 1

workbook.close()
# endregion
"""


"""
# region -------------------- Function 7 --------------------
print("============= Function 7 =============")

pi = 3.14159265359

function = 50*((cos(0.15*pi*x) + 1)/(2 + 0.0025*(x**2)) + (cos(0.15*pi*y) + 1)/(2 + 0.0025*(y**2)))

init_values_1 = [2, 2]
init_values_2 = [7, 3]
init_values_3 = [-90, 88]

init_values_list = [init_values_1, init_values_2, init_values_3]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

for index, init_values in enumerate(init_values_list):
    rol = 4
    col = 4

    min_x_1, min_value_1, n_1 = newton(function, [x, y], init_values, tol=tolerance_1)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
    print("Argument at minimum value: ", min_x_1, "Minimum value: ",
            min_value_1, "Number of iterations: ", n_1)

    min_x_2, min_value_2, n_2= newton(function, [x, y], init_values, tol=tolerance_2)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
    print("Argument at minimum value: ", min_x_2, "Minimum value: ",
            min_value_2, "Number of iterations: ", n_2)


    min_x_3, min_value_3, n_3 = newton(function, [x, y], init_values, tol=tolerance_3)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
    print("Argument at minimum value: ", min_x_3, "Minimum value: ",
            min_value_3, "Number of iterations: ", n_3)


    min_x_4, min_value_4, n_4 = newton(function, [x, y], init_values, tol=tolerance_4)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
    print("Argument at minimum value: ", min_x_4, "Minimum value: ",
            min_value_4, "Number of iterations: ", n_4)


    min_x_5, min_value_5, n_5 = newton(function, [x, y], init_values, tol=tolerance_5)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
    print("Argument at minimum value: ", min_x_5, "Minimum value: ",
            min_value_5, "Number of iterations: ", n_5)

    l1 = [None, None, None, 'Valores Iniciais', 'Valores Finais', 'Valores Finais', 'Valores Finais', 'Valores Finais',
            'Valores Finais']
    l2 = [None, None, 'x', init_values[0], min_x_1[0], min_x_2[0], min_x_3[0], min_x_4[0], min_x_5[0]]
    l3 = [None, None, 'y', init_values[1], min_x_1[1], min_x_2[1], min_x_3[1], min_x_4[1], min_x_5[1]]
    # l4 = [None, None, 'z', init_values[2], min_x_1[2], min_x_2[2], min_x_3[2], min_x_4[2], min_x_5[2]]
    l5 = [None, None, 'Tolerância Utilizada', None, tolerance_1, tolerance_2, tolerance_3, tolerance_4, tolerance_5]
    l6 = [None, None, 'Valor da Função Objetivo', None, min_value_1, min_value_2, min_value_3, min_value_4, min_value_5]
    l7 = [None, None, 'Número de Iterações', None, n_1, n_2, n_3, n_4, n_5]

    for item1, item2, item3, item5, item6, item7 in zip(l1, l2, l3, l5, l6, l7):
        worksheet.write(rol+11*index, col, item1)
        worksheet.write(rol+11*index, col+1, item2)
        worksheet.write(rol+11*index, col+2, item3)
        #worksheet.write(rol+11*index, col+3, item4)
        worksheet.write(rol+11*index, col+3, item5)
        worksheet.write(rol+11*index, col+4, item6)
        worksheet.write(rol+11*index, col+5, item7)
        rol += 1

workbook.close()

# endregion
"""



"""
# region -------------------- Function 8 --------------------
print("============= Function 8 =============")

k1 = 5000
k2 = 1500
k3 = 2000
k4 = 1000
k5 = 2500
k6 = 500
k7 = 3000
k8 = 3500

P1 = 1000
P2 = 2000
P3 = 3000

x_vect = array([x, y, z])
k_vect = array([[k1 + k4 + k5, -k4, -k5],
                [-k4, k2 + k4 + k6, -k6],
                [-k5, -k6, k3 + k5 + k6 + k7 + k8]])
P_vect = array([P1, P2, P3])


term_1 = dot(transpose(x_vect), dot(k_vect, x_vect))/2
term_2 = dot(transpose(x_vect), P_vect)

function = term_1 - term_2

init_values_1 = [-10, 5, 0]
init_values_2 = [6, 30, -50]
init_values_3 = [-9, 2, 100]

init_values_list = [init_values_1, init_values_2, init_values_3]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

for index, init_values in enumerate(init_values_list): 
    rol = 4
    col = 4

    min_x_1, min_value_1, n_1 = newton(function, [x, y, z], init_values, tol=tolerance_1)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
    print("Argument at minimum value: ", min_x_1, "Minimum value: ",
            min_value_1, "Number of iterations: ", n_1)

    min_x_2, min_value_2, n_2= newton(function, [x, y, z], init_values, tol=tolerance_2)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
    print("Argument at minimum value: ", min_x_2, "Minimum value: ",
            min_value_2, "Number of iterations: ", n_2)


    min_x_3, min_value_3, n_3 = newton(function, [x, y, z], init_values, tol=tolerance_3)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
    print("Argument at minimum value: ", min_x_3, "Minimum value: ",
            min_value_3, "Number of iterations: ", n_3)


    min_x_4, min_value_4, n_4 = newton(function, [x, y, z], init_values, tol=tolerance_4)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
    print("Argument at minimum value: ", min_x_4, "Minimum value: ",
            min_value_4, "Number of iterations: ", n_4)


    min_x_5, min_value_5, n_5 = newton(function, [x, y, z], init_values, tol=tolerance_5)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
    print("Argument at minimum value: ", min_x_5, "Minimum value: ",
            min_value_5, "Number of iterations: ", n_5)

    l1 = [None, None, None, 'Valores Iniciais', 'Valores Finais', 'Valores Finais', 'Valores Finais', 'Valores Finais',
            'Valores Finais']
    l2 = [None, None, 'x', init_values[0], min_x_1[0], min_x_2[0], min_x_3[0], min_x_4[0], min_x_5[0]]
    l3 = [None, None, 'y', init_values[1], min_x_1[1], min_x_2[1], min_x_3[1], min_x_4[1], min_x_5[1]]
    l4 = [None, None, 'z', init_values[2], min_x_1[2], min_x_2[2], min_x_3[2], min_x_4[2], min_x_5[2]]
    l5 = [None, None, 'Tolerância Utilizada', None, tolerance_1, tolerance_2, tolerance_3, tolerance_4, tolerance_5]
    l6 = [None, None, 'Valor da Função Objetivo', None, min_value_1, min_value_2, min_value_3, min_value_4, min_value_5]
    l7 = [None, None, 'Número de Iterações', None, n_1, n_2, n_3, n_4, n_5]

    for item1, item2, item3, item4, item5, item6, item7 in zip(l1, l2, l3, l4, l5, l6, l7):
        worksheet.write(rol+11*index, col, item1)
        worksheet.write(rol+11*index, col+1, item2)
        worksheet.write(rol+11*index, col+2, item3)
        worksheet.write(rol+11*index, col+3, item4)
        worksheet.write(rol+11*index, col+4, item5)
        worksheet.write(rol+11*index, col+5, item6)
        worksheet.write(rol+11*index, col+6, item7)
        rol += 1

workbook.close()

# endregion
"""



"""
# region -------------------- Function 9 --------------------
print("============= Function 9 =============")

m1c, m2c, m3c = symbols("m1c m2c m3c")

# Massa estrutural de cada estágio
m1e =  m2e = m3e = 50000

# Aceleração da gravidade
g = 9.80665

# Impulso específico em cada estágio
ie1 = 400
ie2 = 200
ie3 = 100

# Velocidade de exaustão efetiva em cada etágio
ve1 = ie1*g
ve2 = ie2*g
ve3 = ie3*g

mt1 = m1e + m1c
mt2 = m2e + m2c
mt3 = m3e + m3c

delta_v1 = ve1*log((mt1 + mt2 + mt3)/(m1e + mt2 + mt3))

delta_v2 = ve2*log((mt2 + mt3)/(m2e + mt3))

delta_v3 = ve3*log((mt3)/(m3e))

function = delta_v1 + delta_v2 + delta_v3

init_values_1 = [100000, 200000, 300000]
init_values_2 = [500000, 100000, 50000]
init_values_3 = [50000, 400000, 250000]

init_values_list = [init_values_1, init_values_2, init_values_3]

restriction_low = [0, 0, 0]
restriction_high = [600000, 400000, 300000]

tolerance_1 = 0.1
tolerance_2 = 0.01
tolerance_3 = 1e-4
tolerance_4 = 1e-7
tolerance_5 = 1e-10

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

col = 4

for index, init_values in enumerate(init_values_list): 
    rol = 4    

    min_x_1, min_value_1, n_1 = newton(function, [m1c, m2c, m3c], init_values, tol=tolerance_1,
                                       restric_low=restriction_low, restric_high=restriction_high)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
    print("Argument at minimum value: ", min_x_1, "Minimum value: ",
            min_value_1, "Number of iterations: ", n_1)


    min_x_2, min_value_2, n_2= newton(function, [m1c, m2c, m3c], init_values, tol=tolerance_2,
                                      restric_low=restriction_low, restric_high=restriction_high)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
    print("Argument at minimum value: ", min_x_2, "Minimum value: ",
            min_value_2, "Number of iterations: ", n_2)


    min_x_3, min_value_3, n_3 = newton(function, [m1c, m2c, m3c], init_values, tol=tolerance_3,
                                       restric_low=restriction_low, restric_high=restriction_high)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
    print("Argument at minimum value: ", min_x_3, "Minimum value: ",
            min_value_3, "Number of iterations: ", n_3)


    min_x_4, min_value_4, n_4 = newton(function, [m1c, m2c, m3c], init_values, tol=tolerance_4,
                                       restric_low=restriction_low, restric_high=restriction_high)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
    print("Argument at minimum value: ", min_x_4, "Minimum value: ",
            min_value_4, "Number of iterations: ", n_4)


    min_x_5, min_value_5, n_5 = newton(function, [m1c, m2c, m3c], init_values, tol=tolerance_5,
                                       restric_low=restriction_low, restric_high=restriction_high)
                            
    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_5)
    print("Argument at minimum value: ", min_x_5, "Minimum value: ",
            min_value_5, "Number of iterations: ", n_5)

    l1 = [None, None, None, 'Valores Iniciais', 'Valores Finais', 'Valores Finais', 'Valores Finais', 'Valores Finais',
            'Valores Finais']
    l2 = [None, None, 'm1c', init_values[0], min_x_1[0], min_x_2[0], min_x_3[0], min_x_4[0], min_x_5[0]]
    l3 = [None, None, 'm2c', init_values[1], min_x_1[1], min_x_2[1], min_x_3[1], min_x_4[1], min_x_5[1]]
    l4 = [None, None, 'm3c', init_values[2], min_x_1[2], min_x_2[2], min_x_3[2], min_x_4[2], min_x_5[2]]
    l5 = [None, None, 'Tolerância Utilizada', None, tolerance_1, tolerance_2, tolerance_3, tolerance_4, tolerance_5]
    l6 = [None, None, 'Valor da Função Objetivo', None, min_value_1, min_value_2, min_value_3, min_value_4, min_value_5]
    l7 = [None, None, 'Número de Iterações', None, n_1, n_2, n_3, n_4, n_5]

    for item1, item2, item3, item4, item5, item6, item7 in zip(l1, l2, l3, l4, l5, l6, l7):
            worksheet.write(rol+11*index, col, item1)
            worksheet.write(rol+11*index, col+1, item2)
            worksheet.write(rol+11*index, col+2, item3)
            worksheet.write(rol+11*index, col+3, item4)
            worksheet.write(rol+11*index, col+4, item5)
            worksheet.write(rol+11*index, col+5, item6)
            worksheet.write(rol+11*index, col+6, item7)
            rol += 1

workbook.close()

# endregion
"""


"""
# region Single variable tests

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
# endregion
"""
