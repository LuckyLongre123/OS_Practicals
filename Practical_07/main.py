pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3

frames = []
faults = 0

print("Page Reference String:", pages)
print("Frame Capacity:", capacity, "\n")

for i in range(len(pages)):
    page = pages[i]
    print("Page", page, ": ", end="")

    if page not in frames:
        if len(frames) < capacity:
            frames.append(page)
        else:
            farthest = -1
            index_to_replace = 0
            for j in range(len(frames)):
                try:
                    next_use = pages[i+1:].index(frames[j])
                except ValueError:
                    next_use = float('inf')

                if next_use > farthest:
                    farthest = next_use
                    index_to_replace = j

            frames[index_to_replace] = page

        faults += 1
        print("Fault - Frames:", frames)
    else:
        print("Hit   - Frames:", frames)

print("\nTotal Page Faults:", faults)
