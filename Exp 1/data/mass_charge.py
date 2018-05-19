import numpy as np

a = np.array([88.085, 244.271, 343.402, 506.567, 619.733, 756.873, 784.883, 1001.163, 1138.301, 1251.46])

b = np.array([116.095, 272.281, 371.412, 534.586, 647.744, 784.883, 881.998, 1029.173, 1166.312, 1279.47])

c = np.array([131.11, 287.296, 286.427, 549.6, 662.758, 897.013, 1044.187, 1181.327])

angio = 1298.493 # Ang + 2H

x = angio - a
x = x[::-1] #flip the array

y = angio - b
y = y[::-1]

z = angio - c
z = z[::-1]
"""
# print loop
for i in range(len(a)):
    print("$a_{" + str(i+1) + "}$ & $" + str(a[i]) + r"$ & $b_{" + str(i+1) + "}$ & $" + str(b[i]) + "$ & $c_{" + str(i+1) + "}$ & $" + (str(c[i]) if i<8 else "") + "$ \\\\")

for i in range(len(x)):
    print("$x_{" + str(i+1) + "}$ & $" + str(x[i]) + r"$ & $y_{" + str(i+1) + "}$ & $" + str(y[i]) + "$ & $z_{" + str(i+1) + "}$ & $" + (str(z[i]) if i<8 else "") + "$ \\\\")
"""
# internal fragments
def find(arr1, arr2, aim):
    angio3 = 1299.501 # triple charged Angio
    for i in range(0,len(arr1)):
        for j in range(0,len(arr2)):
            mint = angio3 - arr1[i] - arr2[j]
            if (np.abs(mint - aim) < 1):
                print(str(mint) + " c_" + str(i+1) + " z_" + str(j+1))
# end
aim = np.array([110.07, 247.6, 292.08, 297.11, 506.27, 583.3, 619.35, 1056.03, 1099.32])
for i in aim:
    find(c, z, i)
