import time
import multiprocessing
import threading

def io_intensive_task(n):
    time.sleep(n)  # I/O 작업을 시뮬레이션 (n초 대기)
    print(f"Thread Task {n} completed")

def process_function(num_threads):
    threads = []
    for i in range(1, num_threads + 1):
        thread = threading.Thread(target=io_intensive_task, args=(i,))
        threads.append(thread)
        thread.start()  # 스레드 시작

    for thread in threads:
        thread.join()  # 모든 스레드가 완료될 때까지 대기

if __name__ == "__main__":
    start_time = time.time()
    num_tasks = 6  # 총 작업 수

    for i in range(1, num_tasks + 1):
        io_intensive_task(i)  # 각 작업 실행

    end_time = time.time()
    print(f"Default: {end_time - start_time:.4f}")

    start_time = time.time()
    num_processes = 2  # 프로세스 수
    num_threads_per_process = 3  # 각 프로세스에서 실행할 스레드 수

    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=process_function, args=(num_threads_per_process,))
        processes.append(process)
        process.start()  # 프로세스 시작

    for process in processes:
        process.join()  # 모든 프로세스가 완료될 때까지 대기

    end_time = time.time()
    print(f"multiprocessing and multithreading:{end_time - start_time:.4f}")
