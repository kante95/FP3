set table "2.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=0:6] [] [] log10(10**t), + 0 + -180/3.1415957*atan(0.01*10**t) + -180/3.1415957*atan(0.001*10**t) + -180/3.1415957*atan(0.0001*10**t) 
