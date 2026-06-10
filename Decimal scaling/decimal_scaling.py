import numpy as np

x = np.array([1,7,9,12,99])

def z_scale_func(x1,j1):
    return(x1/((10)**j1))


digit_counts = np.char.str_len(x.astype(str))  # Returns [1, 2, 4, 1]
j = max(digit_counts)
print(z_scale_func(x,j))