import sys
N=int(input())
data=list(map(int,sys.stdin.readline().rstrip().split(' ')))

exist=[]
max=data[0]
min=data[0]
for i in data:
    if i > max:
        max=i
    if i<min:
        min=i

print(min,max)