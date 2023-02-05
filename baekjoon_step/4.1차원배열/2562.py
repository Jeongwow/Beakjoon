import sys

max=0
max_idx=0
for i in range(9):
    data=int(sys.stdin.readline().rstrip())
    if data>max:
        max=data
        max_idx=i
print(max,max_idx+1,sep='\n')
