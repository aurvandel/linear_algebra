import numpy as np

L = np.array([1, 1.5, .5, 0]).reshape(2,2)
x0 = np.array([100,0]).reshape(2,1)
years = 2

result = np.empty([2,1])
for i in range(years):
    x0 = np.matmul(L,x0)
print(x0)

