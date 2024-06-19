def CSCAN(arr, head, disk_size):

    seek_count = 0
    distance = 0
    cur_track = 0
    left = []
    right = []
    seek_sequence = []

    left.append(0)
    right.append(disk_size - 1)

    for i in range(len(arr)):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    left.sort()
    right.sort()

    seek_sequence.append(head) 

    for i in range(len(right)):
        cur_track = right[i]
        seek_sequence.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    head = 0
    seek_count += (disk_size - 1)

    for i in range(len(left)):
        cur_track = left[i]
        seek_sequence.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    print(f"Illustration shows total head movement of  {seek_count} cylinders")
    print("Path:")
    print(*seek_sequence, sep=" ")

size = 8
disk_size = 200

print("Enter the values:")
arr = list(map(int, input().split()))

print("Enter the initial position of head: ")
head = int(input())
CSCAN(arr, head, disk_size)