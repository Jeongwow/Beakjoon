import sys

N=int(input())
string=[]

group_num=0
for i in range(N):
    no_group_flag=0
    group=[]
    string=list(map(str,sys.stdin.readline().rstrip()))
    # print(string)
    for j in string:
        if not j in group:
            group.append(j)
            continue
        elif group[-1]==j:
            continue
        no_group_flag=1
    if no_group_flag==0:
        group_num+=1
print(group_num)
    