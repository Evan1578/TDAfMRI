
import numpy as np
import pandas as pd
import pickle as pickle
import gudhi as gd
from pylab import *
import matplotlib.pyplot as plt
import math
import time


def BarcodeAndSimplex(D, save_path):

    skeleton_protein = gd.RipsComplex(
        distance_matrix=D,
        max_edge_length=.2
    )
    Rips_simplex_tree_fMRI = skeleton_protein.create_simplex_tree(max_dimension=2)

    print("Simplex Created!")

    BarCodes_Rips0 = Rips_simplex_tree_fMRI.persistence()

    print("barcode created")
    filtration = Rips_simplex_tree_fMRI.get_filtration()
    filtration_list = []
    for i in filtration:
        filtration_list.append(i)
    print("filtration created")

    all_pairs = Rips_simplex_tree_fMRI.persistence_pairs()

    Desired = []

    print("iterating through barcodes!!")

    for i in BarCodes_Rips0:
        dim = i[0]
        [b, d] = i[1]
        if b == 0 and math.isinf(d):
            continue
        born_equals = []
        death_flag = False
        for j in filtration_list:
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
            for k in filtration_list:
                k[0].sort()
                if k[0] == j[1]:
                    if k[1] == d:
                        if death_flag:
                            print("oh no!")
                        else:
                            simplex_component = j[0];
                            death_component = j[1];
                            death_flag = True;
        if 'simplex_component' in globals():
            Desired.append((dim, b, d, simplex_component, death_component))
            del simplex_component
        else:
            print('Death Component not found')

    print("Process Completed")

    #for i in Desired:
   #     print(str(i))

    with open(save_path, 'wb') as fp:  # Pickling
        pickle.dump(Desired, fp)


directory = 'distanceMatrices/sub'
for i in range(3, 21):
    if i!= 5 and i!= 11:
        if i < 10:
            sub_id = '0' + str(i)
        else:
            sub_id = str(i)
        load_path = directory + sub_id + '.npz'
        test = np.load(load_path, allow_pickle=True)
        save_path = 'generatedSimplexes/Sub' + sub_id + '.pickle'
        D = test['arr_0']
        D = D[::4, ::4]
        BarcodeAndSimplex(D, save_path)












