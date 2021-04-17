
import numpy as np
import pandas as pd
import pickle as pickle
import gudhi as gd
from pylab import *
import matplotlib.pyplot as plt
import math

lam = .1
test = np.load('DistanceMatrix_sub01.npz', allow_pickle = True)
D = test['arr_0'];

for i in range(1017):
    for j in range(1017):
        D[i, j] = D[i, j] + lam*np.abs(i - j)

D = D[::4, ::4];


skeleton_protein = gd.RipsComplex(
    distance_matrix = D,
    max_edge_length = 30
)

Rips_simplex_tree_fMRI = skeleton_protein.create_simplex_tree(max_dimension = 3)

print("Simplex Created!")


BarCodes_Rips0 = Rips_simplex_tree_fMRI.persistence()


for i in BarCodes_Rips0:
    print(str(i))

print("barcode created")
filtration = Rips_simplex_tree_fMRI.get_filtration()
print("filtration created")
filtration2 = Rips_simplex_tree_fMRI.get_filtration()

all_pairs = Rips_simplex_tree_fMRI.persistence_pairs()

Desired = []

print("iterating through barcodes!!")

for i in BarCodes_Rips0:
    dim = i[0]
    [b, d] = i[1]
    if b == 0:
        print("hi")
    born_equals = []
    death_flag = False
    for j in filtration:
        if j[1] == b:
            born_equals.append(j[0])
    born_death_pairs = []
    for j in all_pairs:
        for k in born_equals:
            j[0].sort()
            k.sort()
            if j[0] == k:
                born_death_pairs.append((k, j[1]))

    for j in born_death_pairs:
        j[1].sort()
        for k in filtration2:
            k[0].sort()
            if k[0] == j[1]:
                if k[1] == d:
                    if death_flag:
                        print("oh no!")
                    else:
                        death_component = k[0];
                        death_flag = True;
    if 'death_component' in globals():
        Desired.append((dim, b,d, death_component))
        del death_component
    else:
        print('hi')


print("Process Completed")



with open('Sub1_Barcode_and_Simplex.pickle', 'wb') as fp:   #Pickling
    pickle.dump(Desired, fp)






