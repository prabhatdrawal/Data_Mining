import numpy as np

x = np.array([1,7,9,12,99])

def z_scale_func(x1,mean_val,sd_val):
    return((x1-mean_val)/sd_val)



mean_value = np.mean(x)
sd_value = np.std(x)
for i in range (len(x)):
    print(z_scale_func(x[i],mean_value,sd_value))
