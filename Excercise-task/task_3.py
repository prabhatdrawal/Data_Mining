import numpy as np
x = np.array([1,0,1,0,0,0])
y = np.array([1,0,1,1,0,1])
def smc(x1,y1):
 return (x1 == y1)

def jaccard(x1,y1):
   intersection = np.logical_and(x1, y1).sum()
   union = np.logical_or(x1, y1).sum()
   return(intersection / union)

print("SMC:", smc(x,y))
print("Jaccard:", jaccard(x,y))