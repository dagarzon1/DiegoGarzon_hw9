cpp_vs_python.png:times_python.csv times_cpp.csv
	python DiegoGarzon_Graficas.py
times_cpp.csv:gen_times.x
	./gen_times.x > times_cpp.csv
gen_times.x:
	c++ DiegoGarzon_GenerarTiempos.cpp -o gen_times.x
times_python.csv:
	python DiegoGarzon_GenerarTiempos.py > times_python.csv
clean:
	rm times_cpp.csv gen_times.x times_python.csv cpp_vs_python.png

