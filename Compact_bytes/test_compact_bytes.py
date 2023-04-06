import numpy as np
from compact_bytes import *
from numpy.random import randint
import matplotlib.pyplot as plt

n = 5 # Minimum number of bits to represent the numbers, n<8
x = randint(low = 0, high = 2**n, size = 100, dtype = np.uint8)
compressed = compact_bytes(x, n)
uncompressed = decompact_bytes(compressed, n)

print("Original list: ", x)
print("Decompacted list: ", uncompressed)
plt.subplot(211)
plt.ylabel("Original list")
plt.stem(x)
plt.subplot(212)
plt.ylabel("Decompacted list")
plt.stem(uncompressed)
plt.show()
