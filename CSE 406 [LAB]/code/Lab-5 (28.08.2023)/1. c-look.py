# Read the input queue of disk requests as a comma-separated string
queue = input("Enter the queue of values: ").split(',')
q = [int(x) for x in queue]

# Read the initial position of the disk head
start = int(input("Enter the initial position of the head: "))

# Append the starting position to the list of requests, sort the list, and find the index of the starting position
q.append(start)
q.sort()
start_indx = q.index(start)

path = ""
path1 = ""
total_distance = 0

# Loop through the requests from the starting index to the end of the list
for i in range(start_indx, len(q) - 1):
    path1 += str(q[i]) + " "
    path += f'({q[i+1]}-{q[i]}) + '
    total_distance += q[i+1] - q[i]

# Loop through the requests from the beginning of the list to the starting index
for i in range(0, start_indx - 1):
    path1 += str(q[i]) + " "
    path += f'({q[i+1]}-{q[i]}) + '
    total_distance += q[i+1] - q[i]

# Add the last request to the path
path1 += str(q[start_indx - 1]) + " "
path += f'({q[-1]}-{q[0]})'
total_distance += q[-1] - q[0]

# Print the sequence of visited requests
print("Sequence of visited requests:", path1)

# Print the total distance calculation using "start-end" pairs
print("Total distance calculation:", path)

# Print the total distance traveled by the disk head
print("Total distance traveled:", total_distance)
