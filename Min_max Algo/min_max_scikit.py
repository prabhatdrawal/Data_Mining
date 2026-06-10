import numpy as np
from sklearn.preprocessing import MinMaxScaler

x = np.array([1, 7, 9, 12, 99]).reshape(-1, 1)
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

print(x_scaled.flatten())
