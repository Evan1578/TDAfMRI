import numpy as np
import pickle
import matplotlib.pyplot as plt

tol = .00001;

with open('Sub1_Barcode_and_Simplex.pickle', "rb") as fp:   #Pickling
    BD_simplexes = pickle.load(fp)

nonZero_simplexes = []

for idx, simplex in enumerate(BD_simplexes):
    if simplex[0] > 0:
        nonZero_simplexes.append(simplex)

binary_Matrix = np.zeros((len(nonZero_simplexes), 1))
for idx, simplex in enumerate(nonZero_simplexes):
    b = simplex[1]
    d = simplex[2]
    complex = simplex[3]
    frame_locations = np.zeros((len(complex), 1))
    for i in range(len(complex)):
        vertex = complex[i]
        frame_locations[i] = int(vertex/32)
    if abs(np.var(frame_locations)) < tol:
        binary_Matrix[idx] = 1
    else:
        print("hi")


plt.plot(binary_Matrix)
plt.show()












