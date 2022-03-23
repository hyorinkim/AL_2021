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
