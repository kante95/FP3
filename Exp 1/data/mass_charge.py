import numpy as np

a = np.array([88.085, 244.271, 343.402, 506.567, 619.733, 756.873, 784.883, 1001.163, 1138.301, 1251.46])

b = np.array([116.095, 272.281, 371.412, 534.586, 647.744, 784.883, 881.998, 1029.173, 1166.312, 1279.47])

c = np.array([131.11, 287.296, 286.427, 549.6, 662.758, 897.013, 1044.187, 1181.327])

angio = 1298.493 # Ang + 2H

x = angio - a
x = x[::-1]

y = angio - b
y = y[::-1]

z = angio - c
z = z[::-1]

# print loop
for i in range(0,8):
    print("$a_" + str(i+1) + "$ & $" + str(a[i]) + r"$ & $b_" + str(i+1) + "$ & $" + str(b[i]) + "$ & $c_" + str(i+1) + "$ & $" + str(c[i]) + "$ \\\\")

for i in range(8,10):
    print("$a_{" + str(i+1) + "}$ & $" + str(a[i]) + r"$ & $b_{" + str(i+1) + "}$ & $" + str(b[i]) + "$ & $c_{" + str(i+1) + "}$ & " + " \\\\")

# internal fragments
angio3 = 1299.501 # dreifach geladenes Angio
for i in range(0,8):
    for j in range(0,10):
        mint = angio3 - c[i] - z[j]
        if (mint > 100):
            print(str(mint) + " c_" + str(i+1) + " z_" + str(j+1))
        else:
            break

# end
