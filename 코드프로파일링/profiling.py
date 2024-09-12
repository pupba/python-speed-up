import cProfile
import numpy as np
def find_max_python(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# 숫자가 포함된 리스트
numbers = [np.random.randint(0,1000) for _ in range(1000000)]

# 기본 구현 프로파일링
print("기본 구현 프로파일링:")
cProfile.run('find_max_python(numbers)')

def find_max_optimized(numbers):
    return max(numbers)

# 개선된 구현 프로파일링
print("개선된 구현 프로파일링:")
cProfile.run('find_max_optimized(numbers)')