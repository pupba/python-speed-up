from numba import cuda
import numpy as np

@cuda.jit
def add_arrays(a, b, c):
    idx = cuda.grid(1)
    if idx < c.size:
        c[idx] = a[idx] + b[idx]

# NumPy 배열 생성
n = 1000000
a = np.ones(n)
b = np.ones(n)
c = np.zeros(n)

# GPU에서 실행
threads_per_block = 256
blocks_per_grid = (n + (threads_per_block - 1)) // threads_per_block

add_arrays[blocks_per_grid, threads_per_block](a, b, c)

print("Sum of arrays:", c.sum())
