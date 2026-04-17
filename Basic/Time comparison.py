import time

ms = time.time_ns() // 1000000
a = 0
print("Starting loop...")
print("Current time:", ms, "ms")
for i in range(1, 10000000):
    a += 1
ms2 = time.time_ns() // 1000000
print("Time taken:", ms2 - ms, "ms")