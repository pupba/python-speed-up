import time
from multiprocessing import Pool

def cpu_intensive_task(n):
    result = 0
    for i in range(n):
        result += i ** 2
    return result

if __name__ == "__main__":
    start_time = time.time()
    results = []
    for _ in range(4):  # 4개의 작업을 순차적으로 수행
        result = cpu_intensive_task(10**6)
        results.append(result)
    end_time = time.time()

    print("Results:", results)
    print("Sigle Processing:", end_time - start_time)


    start_time = time.time()
    with Pool(processes=4) as pool:  # 4개의 프로세스를 생성
        results = pool.map(cpu_intensive_task, [10**6] * 4)  # 4개의 작업을 병렬로 수행
    end_time = time.time()

    print("Results:", results)
    print("Multi processing:", end_time - start_time)
