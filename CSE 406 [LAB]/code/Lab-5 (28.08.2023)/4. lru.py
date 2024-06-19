re_string = list(map(int, input("Reference string: ").split(", ")))
# 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1
page_fault = int(input("Enter No Of Frames:  "))
n = len(re_string)
m = [-1]*page_fault
t = [0]*page_fault
c = []
total = 0
idx = 0
sum = 0

print('\nOutput wil be: ')
for i in range(n):
    test = 0
    for p in range(page_fault):
        c.append(m[p])

    for j in range(page_fault):
        if re_string[i] == m[j]:
            test = 1
            total += 1
            t[j] = total
            break
    if test == 0:
        idx = t.index(min(t))
        m[idx] = re_string[i]
        total += 1
        t[idx] = total
        sum += 1

    if c == m:
        for q in range(page_fault):
            print('-', end=' ')
    else:
        for q in range(page_fault):
            if m[q] == -1:
                print("-", end=' ')
            else:
                print(m[q], end=' ')
    c.clear()
    print()

print(f"Page Fault: {sum}")