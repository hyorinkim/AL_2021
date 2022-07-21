n,k=map(int,input().split())
#n이 1일 될때 까지
count=0
while (n!=1):
    if(n%k==0):# n을 k로 나눈 몫
        n/=k
        count+=1
    else: #n에서 1을 뺀다
        n-=1
        count+=1
print(count)




