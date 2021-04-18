import numpy as np
import pickle
import matplotlib.pyplot as plt


def lookupTaskBlock(vertex, subSampleRate):
    time_of_frame = vertex*1.5*subSampleRate;
    if time_of_frame <= 180:
        return 0
    else:
        int_part = int(time_of_frame/192)
        mod_part = (time_of_frame - 180) % 192
        if mod_part < 12:
            return 4
        elif int_part == 1 or int_part == 4:
            return 3
        elif int_part == 2 or int_part == 7:
            return 2
        elif int_part == 3 or int_part == 6:
            return 1
        elif int_part == 5:
            return 0
        else:
            print("error!")
            return -1


def countDistinct(arr):

    arr =np.squeeze(arr)
    length = len(arr)
    res = 1


    return res

Time_frame_blocks = {'Resting': 0, 'Math': 1, 'Video': 2, 'Memory': 3, 'Instructions': 4}

tol = .00001;

subSampleRate = 4;

with open('generatedSimplexes/Sub2_Barcode_and_Simplex.pickle', "rb") as fp:   #Pickling
    BD_simplexes = pickle.load(fp)


taskblock_span = np.zeros((len(BD_simplexes), 3))
for idx, simplex in enumerate(BD_simplexes):
    dim = simplex[0]
    b = simplex[1]
    d = simplex[2]
    death_complex = simplex[4]
    frame_locations = np.zeros((len(death_complex), 1))
    for i in range(len(death_complex)):
        vertex = death_complex[i]
        frame_locations[i] =  lookupTaskBlock(vertex, subSampleRate)
    num_unique = len(np.unique(frame_locations))
    taskblock_span[idx, :] = [d, num_unique, dim]

plt.scatter(taskblock_span[:, 0], taskblock_span[:, 1], c = taskblock_span[:, 2])
plt.show()












