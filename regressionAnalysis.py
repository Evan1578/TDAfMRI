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
behavior_path = 'BEHAV_FIGURE04_PNAS2014.xlsx'
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


summary_stats2 = {}
for key, value in task_blocks.items():
    if key != '06':
        num = len(value)
        total = 0
        for i in range(num):
            if value[i, 1] > 1:
                total += 1

        summary_stats2[key] = total / num
print(summary_stats2)


summary_stats3 = {}
for key, value in task_blocks.items():
    if key != '06':
        num = len(value)
        d0 = 0
        t0 = 0
        d1 = 0
        t1 = 0
        for i in range(num):
            if value[i, 2] == 0:
                d0 += value[i, 1]
                t0 += 1
            elif value[i, 2] == 1:
                d1 += value[i, 1]
                t1 += 1
            else:
                print('uh oh')

        summary_stats3[key] = [d0/t0, d1/t1]
print(summary_stats3)


X = np.zeros((17, 1))
X2 = np.zeros((17, 1))
X3 = np.zeros((17, 1))
X4 = np.zeros((17, 1))
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
        X2[counter] = summary_stats2[sub_id]
        X3[counter] = summary_stats3[sub_id][0]
        X4[counter] = summary_stats3[sub_id][1]

        counter += 1

print("hi")
reg = linear_model.LinearRegression().fit(X, Y)
print('Coefficients: \n', reg.coef_)
# run regression

plt.scatter(X, Y,  color='black')
plt.show()

plt.scatter(X2, Y,  color='black')
plt.show()

plt.scatter(X3, Y,  color='black')
plt.show()

plt.scatter(X4, Y,  color='black')
plt.show()

