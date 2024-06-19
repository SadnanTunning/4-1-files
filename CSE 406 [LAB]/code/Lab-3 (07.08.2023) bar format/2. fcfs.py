input_queue = list(map(int, input("Enter the value for queue: ").split(", ")))  # e.g., 98, 183, 37, 122, 14, 124, 65, 67
head_start = int(input("Enter the head start: "))

path = []
path.append(head_start)
total_distance = ""
ans = 0
while input_queue:
    x = input_queue.pop(0)
    path.append(x)
    if x > head_start:
        total_distance += "(" + str(x) + "-" + str(head_start) + ")"
        ans += (x - head_start)
    else:
        total_distance += "(" + str(head_start) + "-" + str(x) + ")"
        ans += (head_start - x)

    if input_queue:
        total_distance += " + "

    head_start = x

print(f"Path: {' '.join(map(str, path))}")
print(f"Total Distance: {total_distance}")
print(f"Illustration shows total head movement of {ans} cylinders")