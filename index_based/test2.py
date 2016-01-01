from functions2 import transposition_matrix
import numpy as np
import random
import time

l = 27
r = 300
g = np.array([[random.random() for x in range(l)] for y in range(l)])
k = np.array([[[random.random() for x in range(l)] for y in range(l)] for z in range(r)])
kl = np.array([g for z in range(r)])

xs = time.time()
a = np.dot(kl,g)
y = time.time()
b = [np.dot(kl[x,:,:],g) for x in range(kl.shape[0])]
z = time.time()

print '%.8f' % (z-y)
print '%.8f' % (y-xs)
