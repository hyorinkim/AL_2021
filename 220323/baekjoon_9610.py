num=int(input())
points=[input() for __ in range(num)]
di={'Q1':0,'Q2':0 ,"Q3":0,"Q4":0,"AXIS":0}
for i in range(num):
    li=points[i].split()
    p=[int(li[0]),int(li[1])]
    if p[0]>0:
        if p[1]>0:
            di['Q1']+=1
        elif p[1]<0:
            di['Q4']+=1
        else: di['AXIS']+=1
    elif p[0]<0:
        if p[1]>0:
            di['Q2']+=1
        elif p[1]<0:
            di['Q3']+=1
        else: di['AXIS']+=1
    else: di['AXIS']+=1
for k in di:
    print(k+": "+str(di[k]))
#short code
d=[0]*5
for i in range(int(input())):
    m,n=map(int,input().split())
    if m*n==0:d[4]+=1
    else:d[(0 if n>0 else 3)if m>0 else(1 if n>0 else 2)]+=1 # (true 일때 )if (조건) else (false일때) 구조이다.
for i in range(4):print("Q%d: %d"%(i+1,d[i]))# 표현 방식
print("AXIS:",d[4])