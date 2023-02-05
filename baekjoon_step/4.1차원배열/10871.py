import sys
N,X=map(int,input().split(' '))
data=list(map(int,sys.stdin.readline().rstrip().split(' ')))

exist=[]
order_num=0
for i in data:
    if i < X:
        print(i,end=' ')