x =[2,3,4,5,9]
y =[12,3,6,7,12]
manhattan = 0
mul = 0
x_sum = 0
y_sum = 0
eucladian = 0
for i in range(5):
    manhattan += abs(x[i] - y[i])
    eucladian += (x[i]-y[i])**2
    mul += x[i]*y[i]
    x_sum += x[i]**2
    y_sum += y[i]**2


x_mag = (x_sum)**(1/2)
y_mag = (y_sum)**(1/2)
cosine =(mul / (x_mag*y_mag))
euc_dis = eucladian**0.5
   
print(manhattan)
print(cosine)
print(euc_dis)