n=int(input())
#한자리와 두자리 숫자는 다 등차수열 1~99는 다 등차수열
#세자리 숫자 부터 등차수열인 것 구하면 된다.
def count(n):
    ct=0
    for i in range(n,100):

        third=i/100
        second=(i%100)/10
        one=(i-third*100)-second*10
       
        if third-second == second-one: 
            print(third)
            print(second)
            print(one)
            ct+=1
    return ct+99
if n<100: 
    print(n) 
else: 
    v=count(n)
    print(v)  
