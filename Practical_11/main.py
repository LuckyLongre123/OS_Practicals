import threading

numbers = list(range(1, 101))
num_threads = 4
chunk_size = len(numbers) // num_threads
results = [0] * num_threads

def sum_chunk(chunk, index):
    results[index] = sum(chunk)
    print("Thread", index, ": Sum of chunk =", results[index])

threads = []

for i in range(num_threads):
    start = i * chunk_size
    end = start + chunk_size if i < num_threads - 1 else len(numbers)
    chunk = numbers[start:end]

    thread = threading.Thread(target=sum_chunk, args=(chunk, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

total_sum = sum(results)
print("\nTotal Sum:", total_sum)
print("Expected Sum (1 to 100):", sum(numbers))
