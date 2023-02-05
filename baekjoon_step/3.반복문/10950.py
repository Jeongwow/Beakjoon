N=int(input())

data=[]
for i in range(N):
    data.append(input().split())

for i in range(N):
    print(int(data[i][0])+int(data[i][1]))


