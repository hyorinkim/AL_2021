import sys
N=int(sys.stdin.readline())
list1=list()
for i in range(N):
    list1.append(int(sys.stdin.readline()))
list2=sorted(list1)
for data in (list2):
    print(data)
objrev=reversed(list1)
print(list(objrev))

m='나는 정말로 배가 고프다.'
m=m.split()
m.sort(key=len)
print(m)