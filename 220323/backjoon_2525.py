recurrent=list(map(int,input().split()))
running=int(input())
recurrent[1]=(recurrent[1]+running)%60
recurrent[0]+=(recurrent[1]+running)/60
if recurrent[0]==24:
    recurrent[0]=0
print("%d %d",recurrent[0],recurrent[1])