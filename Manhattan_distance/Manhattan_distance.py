
x =[3,53,8,11]
y =[9,55,7,12]
md = 0
mul = 0
x_sum = 0
y_sum = 0
for i in range(4):
    md += abs(x[i] - y[i])
    mul += x[i]*y[i]
    x_sum += x[i]**2
    y_sum += y[i]**2

x_mag = (x_sum)**(1/2)
y_mag = (y_sum)**(1/2)
cosine =(mul / (x_mag*y_mag))
print(cosine)
   
print(md)