# Form Distance matrix

import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim



def distanceMatrix(sub_id):

    print("Distance matrix for subject " + str(sub_id) + " started")

    data_path = 'originalScans/sub-' + sub_id + '/SBJ' + sub_id + '_Ctask.nii.gz'
    img = nib.load(data_path)
    image_data = img.get_fdata()

    print("Distance matrix loaded correctly")

    D_temp = np.zeros((1017, 1017))

    for i in range(1017):
        for j in range(i):
            D_temp[i, j] = np.linalg.norm(np.squeeze(image_data[:, :, :, i]) - np.squeeze(image_data[:, :, :, j]))


    D = D_temp + np.transpose(D_temp)
    D = D/np.average(D)

    save_path = 'distanceMatrices/sub' + sub_id
    np.savez(save_path, D)



for i in range(4, 20):
    if i != 5 and i != 11:
        if i >= 10:
            distanceMatrix(str(i))
        else:
            distanceMatrix('0' + str(i))








