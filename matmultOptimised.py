#Matrix multiplication, replacing nested forloops with numpy
import numpy as np

N = 250

# NxN matrix
X = np.matrix(np.random.randint(100, size=(N, N)))
# Nx(N+1) matrix
Y = np.matrix(np.random.randint(100, size=(N, N+1)))
    
result = X * Y

for r in result:
    print(r)