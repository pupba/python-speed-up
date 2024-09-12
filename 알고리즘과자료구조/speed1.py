import time
if __name__ == "__main__":
    start = time.time()
    a = []
    for i in range(100000000):
        a.append(i)
    end = time.time()
    print(f"Default : {end-start:.4f}sec")

    start = time.time()
    a = [i for i in range(100000000)]
    end = time.time()
    print(f"List Comprehension : {end-start:.4f}sec")