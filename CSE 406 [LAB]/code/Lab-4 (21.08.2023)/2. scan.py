q=input().split(", ")  #Input ->98, 183, 37, 122, 14, 124, 65, 67
q=[int(x) for x in q]
q.append(0)
q.sort()
initial=int(input())  #Input ->53
total_dis=""
total=int()
path=""

indx=0
mn=abs(initial-q[0])
for i in range(1,len(q)):
        if mn>abs(initial-q[i]):
            mn=abs(initial-q[i])
            indx=i
fstq=q[:indx]
lstq=q[indx+1:]
print(fstq,lstq)
for i in range(len(fstq)-1,-1,-1):
    path+=str(initial)+" "
    total_dis+="("+str(max(fstq[i],initial))+"-"+str(min(fstq[i],initial))+")+"
    total+=abs(fstq[i]-initial)
    initial=fstq[i]
for i in lstq:
    path+=str(initial)+" "
    total_dis+="("+str(max(i,initial))+"-"+str(min(i,initial))+")+"
    total+=abs(i-initial)
    initial=i
path+=str(initial)
print("Total distance:",total_dis[:-1])
print("Path:",path)
print(f'Illustration shows total head movement of {total} cylinders.')