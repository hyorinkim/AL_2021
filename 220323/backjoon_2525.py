time=[input()for __ in range(2) ]
recurrent=list(map(int,time[0].split()))
running=int(time[1])
recurrent[0]+=int((recurrent[1]+running)/60)
recurrent[1]=(recurrent[1]+running)%60
if recurrent[0]>=24:
    recurrent[0]%=24
print(recurrent[0],recurrent[1])

#short code
h,m,t=map(int,open(0).read().split())#open(0)는 파일 객체를 반환, read는 파일 전체의 내용을 하나의 문자열로 읽어 온다.
m+=t
print((h+m//60)%24,m%60)