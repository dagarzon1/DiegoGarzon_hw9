cpp_vs_python.png:times_python.csv times_cpp.csv
	python DiegoGarzon_Graficas.py
times_cpp.csv:gen_times.x
	./gen_times.x > times_cpp.csv
gen_times.x:DiegoGarzon_GenerarTiempos.cpp
	c++ DiegoGarzon_GenerarTiempos.cpp -o gen_times.x
times_python.csv:DiegoGarzon_GenerarTiempos.py
	python DiegoGarzon_GenerarTiempos.py > times_python.csv
clean:
	rm times_cpp.csv gen_times.x times_python.csv cpp_vs_python.png

