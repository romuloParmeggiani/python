import threading
import time

results = {}
def longSquare(n, results):
    time.sleep(1)
    results[n] = n**2

# t1 = threading.Thread(target=longSquare, args=(1, results))
# t2 = threading.Thread(target=longSquare, args=(2, results))

# t1.start()
# t2.start()

# t1.join()
# t2.join()
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0, 5)]
[t.start() for t in threads]
[t.join() for t in threads]

print(results)