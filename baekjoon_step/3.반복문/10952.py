import sys
data=[]
while True:
    data.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
    if data[-1][0] == data[-1][0] == 0:
        break


for i in range(len(data)-1):
    print(f'{data[i][0]+data[i][1]}')