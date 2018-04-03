#include <iostream>
#include <ctime>

using namespace std;

int fibonacci(int n);
float get_time(int n);
int main()
{
// Iteracion para encontrar los primeros 35 numeros

for (int i=0;i<36;i++)
{
	// El tiempo por cada iteracion

	float tm=get_time(i);

	// Imprimir el valor de iteracion y el tiempo que tardo

	cout<<i<<","<<tm<<endl;
}

return 0;
}
//Funcion recursiva de fibonacci

int fibonacci(int n)
{
	//Condicional que tiene el caso base

	if (n==1 || n==0)
	{
		//retornar el caso base

		return n;
	}

	//retornar el caso recursivo

	return fibonacci(n-1)+fibonacci(n-2);
}

//Funcion para calcular el tiempo pasado

float get_time(int n)
{

// variable de tiempo

clock_t t=clock();

// calculo de fibonacci usando la funcion recursiva

int res=fibonacci(n);

// determinar el tiempo que se gasto

t=clock() - t;

// pasar el tiempo a segundos

float time = ((float)t)/CLOCKS_PER_SEC;

// retornar el tiempo en segundos

return time;
}


