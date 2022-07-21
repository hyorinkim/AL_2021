# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

n,m,k=map(int,input().split())
data = list(map(int,input().split()))
# 탐욕법,그리디 문제
# data에서 가장 큰수와 다음으로 가장 큰수를 뽑아내기
data.sort(reverse=True)

bigOne=data[0]
bigTwo=data[1]
total_count=0
answer=0

while(total_count<m):

    for i in range(k):
        answer+=bigOne
        total_count+=1
    if (total_count % k == 0):
        answer += bigTwo
        total_count += 1
print(answer)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
