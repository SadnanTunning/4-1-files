re_string = list(map(int, input("Reference string: ").split(", ")))
# 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1
page_fault = int (input("Enter No Of Frames:  "))
n = len(re_string)
m = [-1]*page_fault
c = []
l = []
sum = 0

print('\nOutput wil be: ')
for i in range(n):
    test = 0
    for p in range(page_fault):
        c.append(m[p])
    if i < page_fault:
        m[i] = re_string[i]
        sum += 1
        re_string[i] = -99
    else:
        for j in range(page_fault):
            if re_string[i] == m[j]:
                test = 1
                re_string[i] = -99
                break
        if test == 0:
            for s in range(page_fault):
                if(m[s] in re_string):
                    l.append(re_string.index(m[s]))
                else:
                    l.append(999)
            idx = l.index(max(l))
            m[idx] = re_string[i]
            sum += 1
            re_string[i] = -99
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
    l.clear()
    print()

print(f"Page Fault: {sum}")