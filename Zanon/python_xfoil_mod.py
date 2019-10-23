# CALLING XFOIL FROM PYTHON
# Written by: JoshTheEngineer
# YouTube: www.youtube.com/joshtheengineer
# Website: www.joshtheengineer.com
# Started: 01/01/19
# Updated: 01/01/19 - Started code in MATLAB
#                   - Works as expected
#          02/03/19 - Transferred code from MATLAB to Python
#                   - Works as expected

import os
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# CREATE LOADING FILE

# Knowns
NACA = '4412'
AoA = '0'
num_nodes = '160'
airfoil_dat_file = 'Save_Airfoil.txt'
cp_distribution_file = 'Save_Cp.txt'
xfoil_inputs = 'xfoil_input.txt'
airfoil_coeff = 'airfoil_coeff.txt'

# Delete files if they exist
if os.path.exists(airfoil_dat_file):
    os.remove(airfoil_dat_file)

if os.path.exists(cp_distribution_file):
    os.remove(cp_distribution_file)

if os.path.exists(xfoil_inputs):
    os.remove(xfoil_inputs)

if os.path.exists(airfoil_coeff):
    os.remove(airfoil_coeff)

# Create the airfoil
fid = open(xfoil_inputs, "w")
fid.write("NACA " + NACA + "\n")
fid.write("PPAR\n")
fid.write("N " + num_nodes + "\n")
fid.write("\n\n")
fid.write("PSAV " + airfoil_dat_file + "\n")
fid.write("OPER\n")
fid.write("Visc\n")
fid.write("200000\n")
fid.write("PACC\n")
fid.write(airfoil_coeff + "\n")
fid.write("\n")
fid.write("ALFA " + AoA + "\n")
fid.write("CPWR " + cp_distribution_file + "\n")
fid.write("quit\n")
fid.close()

# Run the XFoil calling command
os.system("xfoil.exe < xfoil_input.txt")

# Delete file after running
if os.path.exists(xfoil_inputs):
    os.remove(xfoil_inputs)

# READ DATA FILE: AIRFOIL

working_dir = os.getcwd()
file_full_path = working_dir + r"\\" + airfoil_dat_file

# Load the data from the text file
dataBuffer = np.loadtxt(file_full_path, skiprows=0)

# Extract data from the loaded dataBuffer array
XB = dataBuffer[:, 0]
YB = dataBuffer[:, 1]

# Delete file after loading
# if os.path.exists(saveFlnmAF):
#     os.remove(saveFlnmAF)

"""
# READ DATA FILE: PRESSURE COEFFICIENT

# Load the data from the text file
dataBuffer = np.loadtxt(cp_distribution_file, skiprows=3)

# Extract data from the loaded dataBuffer array
X_0 = dataBuffer[:, 0]
Y_0 = dataBuffer[:, 1]
Cp_0 = dataBuffer[:, 2]
"""


def objective(y_coord):
    # Transformar a entrada y em um txt junto com o x definido globalmente
    # mat->txt (Cria arquivo com nome Airfoil_y)

    airfoil_coord = np.array([XB, y_coord])
    np.savetxt(airfoil_dat_file, airfoil_coord.transpose(), fmt="%s")

    fid = open(xfoil_inputs, "w")
    fid.write("LOAD " + airfoil_dat_file + "\n")
    fid.write("PPAR\n")
    fid.write("N " + num_nodes + "\n")
    fid.write("\n\n")
    fid.write("OPER\n")
    fid.write("Visc\n")
    fid.write("200000\n")
    fid.write("PACC\n")
    fid.write(airfoil_coeff + "\n")
    fid.write("\n")
    fid.write("ALFA " + AoA + "\n")
    fid.write("CPWR " + cp_distribution_file + "\n")
    fid.write("quit\n")
    fid.close()

    dataBuffer = np.loadtxt(airfoil_coeff, skiprows=12)
    Cl = dataBuffer[1]
    Cd = dataBuffer[2]

    # Load the data from the text file
    dataBuffer = np.loadtxt(file_full_path, skiprows=0)

    # Extract data from the loaded dataBuffer array
    XB = dataBuffer[:, 0]
    YB = dataBuffer[:, 1]

    XB_U = XB[YB >= 0]
    XB_L = XB[YB < 0]
    YB_U = YB[YB >= 0]
    YB_L = YB[YB < 0]

    plt.figure(1)
    plt.cla()
    plt.plot(XB_U, YB_U, 'b.-', label='Upper')
    plt.plot(XB_L, YB_L, 'r.-', label='Lower')
    plt.xlabel('X-Coordinate')
    plt.ylabel('Y-Coordinate')
    plt.title('Airfoil')
    plt.axis('equal')
    plt.legend()
    plt.show()

    return Cl/Cd


def constraint(x):
    # Esta função define o valor da condição de contorno do problema

    pass


if __name__ == "__main__":

    # Delete file after loading
    # if os.path.exists(saveFlnmCp):
    #    os.remove(saveFlnmCp)

    
    # EXTRACT UPPER AND LOWER AIRFOIL DATA

    # Split airfoil into (U)pper and (L)ower
    XB_U = XB[YB >= 0]
    XB_L = XB[YB < 0]
    YB_U = YB[YB >= 0]
    YB_L = YB[YB < 0]

    """
        # Aqui se define os limites das massas em que o foguete pode atingir
    b = (0.0, 25000.0)
    bnds = (b, b, b)

    # Define-se as condições que o problema impõe
    cons1 = {'type': 'eq', 'fun': constraint}
    cons = [cons1]

    # A Solução do problema através do método de otimização
    res = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints = cons)




    res = minimize(objective, x0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})
    """

    res = minimize(objective, YB, method='nelder-mead', options={'xtol': 1e-4, 'disp': True})

    """
    # Split XFoil results into (U)pper and (L)ower
    Cp_U = Cp_0[YB >= 0]
    Cp_L = Cp_0[YB < 0]
    X_U = X_0[YB >= 0]
    X_L = X_0[YB < 0]
    """


    # PLOT DATA

    # Plot airfoil
    plt.figure(1)
    plt.cla()
    plt.plot(XB_U, YB_U, 'b.-', label='Upper')
    plt.plot(XB_L, YB_L, 'r.-', label='Lower')
    plt.xlabel('X-Coordinate')
    plt.ylabel('Y-Coordinate')
    plt.title('Airfoil')
    plt.axis('equal')
    plt.legend()
    plt.show()

    """
    # Plot pressure coefficient
    fig = plt.figure(2)
    plt.cla()
    plt.plot(X_U, Cp_U, 'b.-', label='Upper')
    plt.plot(X_L, Cp_L, 'r.-', label='Lower')
    plt.xlim(0, 1)
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Pressure Coefficient')
    plt.show()
    plt.legend()
    plt.gca().invert_yaxis()
    """
