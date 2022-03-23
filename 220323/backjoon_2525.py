time=[input()for __ in range(2) ]
recurrent=list(map(int,time[0].split()))
running=int(time[1])
recurrent[0]+=int((recurrent[1]+running)/60)
recurrent[1]=(recurrent[1]+running)%60
if recurrent[0]>=24:
    recurrent[0]%=24
print(recurrent[0],recurrent[1])