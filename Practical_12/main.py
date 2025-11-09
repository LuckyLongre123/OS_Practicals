def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        for j, block in enumerate(blocks):
            if block >= process:
                allocation[i] = j
                blocks[j] -= process
                break
    return allocation

def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        best_idx = -1
        min_diff = float('inf')
        for j, block in enumerate(blocks):
            if block >= process:
                diff = block - process
                if diff < min_diff:
                    min_diff = diff
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= process
    return allocation

def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        worst_idx = -1
        max_diff = -1
        for j, block in enumerate(blocks):
            if block >= process:
                diff = block - process
                if diff > max_diff:
                    max_diff = diff
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= process
    return allocation

def display(name, func, blocks, processes):
    print("\n---", name, "---")
    temp = blocks.copy()
    allocation = func(temp, processes)
    print("Process\tSize\tBlock")
    for i, alloc in enumerate(allocation):
        if alloc != -1:
            print("{}\t{}\t{}".format(i+1, processes[i], alloc+1))
        else:
            print("{}\t{}\tNot Allocated".format(i+1, processes[i]))

block_sizes = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

print("Memory Blocks:", block_sizes)
print("Process Sizes:", process_sizes)

display("First Fit", first_fit, block_sizes, process_sizes)
display("Best Fit", best_fit, block_sizes, process_sizes)
display("Worst Fit", worst_fit, block_sizes, process_sizes)
