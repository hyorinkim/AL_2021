# n * m 형태의 배열로 입력 받음
n,m = map(int,input().split())
n_min=list()
for i in range(n):
    data = list(map(int,input().split()))
    n_min.append(min(data))#각 행마다 가장 작은 수만 골라서 리스트에 넣음

print(max(n_min))# 그 중에서 가장 큰수