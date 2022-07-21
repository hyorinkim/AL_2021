# n * m 형태의 배열로 입력 받음
n,m = map(int,input().split())
n_min=list()
result=0
for i in range(n):
    data = list(map(int,input().split()))
    n_min.append(min(data))#각 행마다 가장 작은 수만 골라서 리스트에 넣음
#  min_value=min(data) #리스트에 안 넣고 
# result=max(result,min_value) # 각 행의 작은 수가 나올때 마다 비교해서 큰것만 result로 가짐
#print(result)
print(max(n_min))# 그 중에서 가장 큰수