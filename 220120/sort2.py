N=int(input())
list1=list()
for i in range(N):
    list1.append(int(input()))
list2=sorted(list1)
print(list2)
objrev=reversed(list1)
print(list(objrev))