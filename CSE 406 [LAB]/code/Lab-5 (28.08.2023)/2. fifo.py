re_string = list(map(int, input("Reference string: ").split(", "))) #1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
# 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1
#print(re_string)

n = int(input("Total number of page frame: "))

memory = ["-"]*n
#print(memory)
i = 0
page_fault = 0
while re_string != []:
    if i == n:
        i = 0
    x = re_string.pop(0)
    if str(x) in memory:
        print("----")
    else:
        page_fault += 1
        memory[i] = str(x)
        i += 1
        print(memory)

print(f"Page frames : {page_fault}")