inp=input().split(' ')

cnt=0
if inp[0]=='':
    cnt+=1
if inp[-1]=='':
    cnt+=1
print(len(inp)-cnt)