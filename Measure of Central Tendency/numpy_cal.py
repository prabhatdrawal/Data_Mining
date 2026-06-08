import numpy as np 
data = np.array([15,22,18,45,20,17,23])

print("mean",np.mean(data))
print("median",np.median(data))
vals, counts = np.unique(data, return_counts=True)
print("mode", vals[np.argmax(counts)])


data_new = np.array([30,35,40,45,50,55,60,70])
print("range",np.ptp(data_new))
print("std",np.std(data_new))
print("iqr",np.percentile(data_new,75)-np.percentile(data_new,25))

q3_20= np.percentile(data_new, 75, method='hazen')
q1_20 = np.percentile(data_new, 25, method='hazen')
print("iqr", q3_20 - q1_20)

q3_22 = np.percentile(data_new, 75, method='weibull')
q1_22 = np.percentile(data_new, 25, method='weibull')
print("iqr", q3_22 - q1_22)  #

