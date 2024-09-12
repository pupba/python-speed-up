import time
import numpy as np
if __name__ == "__main__":
    numbers = [np.random.randint(0,1000) for _ in range(10000000)]

    start = time.time()
    # 초기 최대값을 첫 번째 요소로 설정
    max_value = numbers[0]

    # 리스트를 순회하며 최대값 찾기
    for num in numbers:
        if num > max_value:
            max_value = num
    end = time.time()
    print(f"직접 구현 : {end-start:.4f}sec")

    start = time.time()

    # NumPy 배열로 변환 후 최대값 찾기
    max_value = np.max(numbers)
    end = time.time()
    print(f"Numpy : {end-start:.4f}sec")