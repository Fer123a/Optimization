xfoil_inputs = "xfoil_inputs.txt"

fid = open(xfoil_inputs, "w")

fid.write("LOAD \n")
fid.close()

import python_xfoil_mod

python_xfoil_mod.objective()