import time

#Funcion recursiva para calcular el n-simo valor de fibonacci
def fibonacci(n):
	#Condicional que tiene el caso base
	if (n==1) or (n==0):
		#retornar el caso base
		return n
	#retornar el caso recursivo
	return fibonacci(n-1)+fibonacci(n-2)

#Funcion para calcular el tiempo pasado
def get_time(n):
	#Variable que tiene el tiempo inicial
	t=time.time()
	#calculo de fibonacci usando la funcion recursiva
	fibonacci(n)
	#determinar el tiempo que se gasto
	t1=time.time()-t
	#retornar el tiempo gastado
	return t1
	
for i in range(36):
	print fibonacci(i), ",", get_time(i)
