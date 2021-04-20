import numpy as np
import pandas
import pickle
from sklearn import linear_model
import matplotlib.pyplot as plt

# load persistence homology data
load_path = 'taskblocks.pickle'
with open(load_path, "rb") as fp:  # Pickling
    task_blocks = pickle.load(fp)

# load behavior summary statistics
behavior_path = 'originalScans/BEHAVIORAL/BEHAV_FIGURE04_PNAS2014.xlsx'
behavior = pandas.read_excel(behavior_path, sheet_name= 'Global')
test = behavior.to_numpy()
# compute summary statistics
summary_stats = {}
for key, value in task_blocks.items():
    sub_summary = 0;
    num = len(value)
    for i in range(0, num):
        sub_summary = sub_summary + (.4 - value[i, 0])*(value[i, 1] - 1)*(1/(value[i, 2] + 1))

    summary_stats[key] = sub_summary

X = np.zeros((17, 1))
Y = np.zeros((17, 1))
counter = 0
for i in range(1, 21):
    if i != 5 and i != 6 and i != 11:
        Y[counter] = float(test[i + 1, 1])
        if i < 10:
            sub_id = '0' + str(i)
        else:
            sub_id = str(i)

        X[counter] = summary_stats[sub_id]

        counter += 1

print("hi")
reg = linear_model.LinearRegression().fit(X, Y)
print('Coefficients: \n', reg.coef_)
# run regression

plt.scatter(X, Y,  color='black')

plt.show()