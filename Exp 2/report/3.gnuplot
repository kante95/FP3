set table "3.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=0:4.1] [] [] log10(10**t), + 20*log10(abs(1/sqrt(1+(0.01*10**t)**2))) + 20*log10(abs(1/sqrt(1+(0.001*10**t)**2))) + 20*log10(abs(1/sqrt(1+(0.0001*10**t)**2))) + 20*log10(abs(1/(10**t)))+20*log10(10/0.01)-20*log10(abs(1/sqrt(1+(0.01*10**t)**2))) 
