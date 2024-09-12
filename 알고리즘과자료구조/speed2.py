import time
if __name__ == "__main__":
    start = time.time()
    a = 0
    for i in range(1000000):
        a+=i
    print(a)
    end = time.time()
    print(f"Default : {end-start:.4f}sec")

    start = time.time()
    a = list(range(1000000))
    a = sum(a)
    print(a)
    end = time.time()
    print(f"SUM : {end-start:.4f}sec")