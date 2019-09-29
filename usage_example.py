from sympy import symbols
from numpy import array, transpose, dot
from gradient import grad
from newton import newton
import xlsxwriter


def local_foo(x):
    return (x-2)**2


x, y, z = symbols("x y z")


# region -------------------- Function 4 --------------------
print("============= Function 4 =============")
"""
Usage example of Gradient Descent function
"""


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

workbook = xlsxwriter.Workbook('test_grad.xlsx')
worksheet = workbook.add_worksheet()

col = 4

for index, init_values in enumerate(init_values_list):
    rol = 4    

    min_x_1, min_value_1, n_1 = grad(function, [x, y], init_values, tol=tolerance_1)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_1)
    print("Argument at minimum value: ", min_x_1, "Minimum value: ",
            min_value_1, "Number of iterations: ", n_1)

    min_x_2, min_value_2, n_2= grad(function, [x, y], init_values, tol=tolerance_2)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_2)
    print("Argument at minimum value: ", min_x_2, "Minimum value: ",
            min_value_2, "Number of iterations: ", n_2)


    min_x_3, min_value_3, n_3 = grad(function, [x, y], init_values, tol=tolerance_3)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_3)
    print("Argument at minimum value: ", min_x_3, "Minimum value: ",
            min_value_3, "Number of iterations: ", n_3)


    min_x_4, min_value_4, n_4 = grad(function, [x, y], init_values, tol=tolerance_4)

    print("\n", "Initial values: ", init_values, "Tolerance used: ", tolerance_4)
    print("Argument at minimum value: ", min_x_4, "Minimum value: ",
            min_value_4, "Number of iterations: ", n_4)


    min_x_5, min_value_5, n_5 = grad(function, [x, y], init_values, tol=tolerance_5)

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


# region -------------------- Function 8 --------------------
"""
Usage example of Newton Method function
"""
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

workbook = xlsxwriter.Workbook('test_newton.xlsx')
worksheet = workbook.add_worksheet()

col = 4

for index, init_values in enumerate(init_values_list):
    rol = 4
    
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
