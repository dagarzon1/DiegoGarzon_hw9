import numpy as np
import matplotlib.pyplot as plt

#Cargar los datos de python y cpp

data_py=np.loadtxt("times_python.csv", delimeter=",")
data_cpp=np.loadtxt("times_cpp.csv", delimter=",")

#Graficar los datos

plt.plot(data_py[:,0],data_py[:,1], label="python")
plt.plot(data_cpp[:,0],data_cpp[:,1], label="c++")

#Configurar la grafica

plt.xlabel("Iteration number")
plt.ylabel("Computational time (s)")
plt.legend()
plt.title("cpp vs python")

#Guardar la grafica

plt.savefig("cpp_vs_python.png")
