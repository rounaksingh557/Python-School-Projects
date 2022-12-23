import time

# Dynamic Storage
start = time.time()
my_list = []
for num in range(30_000_000):
    my_list.append(num) #type: ignore
end = time.time()
print(f'Seconds: {end-start}')

# Pre-Allocation
start = time.time()
my_list2 = [0]*30_000_000
for num in range(30_000_000):
    my_list2[num] = num
end = time.time()
print(f"Seconds: {end-start}")