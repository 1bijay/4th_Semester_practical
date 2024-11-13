#machine learning
import numpy as np
x= np.array([2,4,6,8,10])
y= np.array([6,5,4,2,-1])

print(x)
print(y)
n= len(x)
print(n)
sum_x= np.sum(x)
sum_y= np.sum(y)
print(sum_x, sum_y)
sum_xy= np.sum(x*y)
print(sum_xy)
sum_xsq= np.sum(x**2)
print(sum_xsq)
#formula calculation
b1=(n*sum_xy-sum_x*sum_y)/(n*sum_xsq-(sum_x**2))
print(b1)

def prediction(x,b0=7,b1=-0.5):
    return  b0+b1*x

def prediction(x):
    return 7+(-0.5)*x

x=10
y=prediction(x)
print(y)

#def linerregression(): 
