inp=int(input())
tmp=(inp-2)//6 +2
num=1
cnt=1
while tmp>num:
    num+=cnt
    cnt+=1
print(cnt)