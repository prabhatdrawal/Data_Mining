import numpy as np

x = np.array([2,3,4,5,9])
y = np.array([12,3,6,7,12])

def manhattan(x1,y1):
    return( np.sum(np.abs(x1 - y1)))

def euclidean(x1,y1):
    return(np.linalg.norm(x1 - y1))

def cosine(x1,y1):
    return(np.dot(x1,y1) / (np.linalg.norm(x1) * np.linalg.norm(y1)))




print(manhattan(x,y))
print("euclidean:",euclidean(x,y))
print("cosine:",cosine(x,y))