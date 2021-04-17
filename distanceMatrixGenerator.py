# Form Distance matrix

import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

data_path = 'data/sub-01/ses-1/funct/sub-01_ses-1_fmRI.nii'
img = nib.load(data_path)
image_data = img.get_fdata()

# set hyperparameters
lam = .1
D_temp = np.zeros((1017, 1017))

for i in range(1017):
    for j in range(i):
        D_temp[i, j] = ssim(np.squeeze(image_data[:, :, :, i]), np.squeeze(image_data[:, :, :, j]))  +  lam*np.abs(i - j)


D = D_temp + np.transpose(D_temp)
print(str(D[2, 2]))


np.savez('DistanceMatrix_sub01', D, lam)


print("hi")

