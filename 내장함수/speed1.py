import time
if __name__ == "__main__":
    # 중복된 숫자가 포함된 리스트
    numbers = [5, 3, 8, 5, 2, 3, 9, 1, 2, 8, 7]

    start = time.time()

    # 1. 중복 제거
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    time.sleep(0.1)
    # 2. 정렬 (버블 정렬 알고리즘 사용)
    n = len(unique_numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if unique_numbers[j] > unique_numbers[j+1]:
                # swap
                unique_numbers[j], unique_numbers[j+1] = unique_numbers[j+1], unique_numbers[j]

    end = time.time()

    print(f"직접 구현 : {end-start:.4f}sec")

    start = time.time()
    
    # 중복 제거
    unique_numbers = list(set(numbers))
    time.sleep(0.1)
    # 정렬
    sorted_numbers = sorted(unique_numbers)
    
    end = time.time()
    print(f"내장함수 사용 : {end-start:.4f}sec")