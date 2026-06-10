import numpy as np

x = np.array([1,7,9,12,99])

def min_max_func(x1,max_val,min_val):
    return((x1-min_val)/(max_val-min_val))



max_value  = max(x)
min_value = min(x)
print(max_value)
print(min_value)
for i in range (len(x)):
    print(min_max_func(x[i],max_value,min_value))



