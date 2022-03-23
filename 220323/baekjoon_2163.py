choco=list(map(int,input().split()))
if choco[0]>choco[1]:
    print((choco[1]-1)+(choco[0]-1)*choco[1])
else:
    print((choco[0]-1)+(choco[1]-1)*choco[0])
#short code
print(eval('*'.join(input().split()))-1)