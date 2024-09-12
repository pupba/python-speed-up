import time
import threading

def io_intensive_task(n):
    time.sleep(n)  # I/O 작업을 시뮬레이션 (n초 대기)
    print(f"Task {n} completed")

if __name__ == "__main__":
    start_time = time.time()

    for i in range(1, 5):  # 1초, 2초, 3초, 4초 대기 작업
        io_intensive_task(i)
    end_time = time.time()
    print("Single-Threading:", end_time - start_time)


    start_time = time.time()
    threads = []
    for i in range(1, 5):  # 1초, 2초, 3초, 4초 대기 작업
        thread = threading.Thread(target=io_intensive_task, args=(i,))
        threads.append(thread)
        thread.start()  # 스레드 시작

    for thread in threads:
        thread.join()  # 모든 스레드가 완료될 때까지 대기

    end_time = time.time()
    print("Multi-Threading:", end_time - start_time)