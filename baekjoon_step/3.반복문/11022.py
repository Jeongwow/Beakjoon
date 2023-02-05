import sys

T=int(input())

data=[]
for i in range(T):
    data.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

for i in range(T):
    print(f'Case #{int(i)+1}: {data[i][0]} + {data[i][1]} = {data[i][0]+data[i][1]}')