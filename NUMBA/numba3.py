import numpy as np
from numba import njit,prange
import time

def sum_array1(arr):
    total = 0.0
    for i in range(arr.size):
        total += arr[i]
    return total

@njit
def sum_array2(arr):
    total = 0.0
    for i in prange(arr.size):
        total += arr[i]
    return total

# NumPy 배열 생성
data = np.arange(1, 100000001)

# Numba를 사용한 함수 호출
start = time.time()
result = sum_array1(data)
print(f"No JIT:{time.time() - start:.3f}sec")
start = time.time()
result = sum_array2(data)
print(f"JIT:{time.time() - start:.3f}sec")
