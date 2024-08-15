import numpy as np
first = np.array([5,6,2,1,8])
print(first)
second =np.array([5,"bijay",4])
print(second)
first.sort()
first=np.random.choice(first)
print(first)


def main():
    print("Starting")
main() 

def parameter(a,b):
    return a+b
b=parameter(2,4)
print(b)
