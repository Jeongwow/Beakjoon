import sys

N=sys.stdin.readline()

result_arr=[]
for i in range(int(N)):
    num=sys.stdin.readline().rstrip().split(' ')
    # print(num)
    result_arr.append(int(num[0])+int(num[1]))

for i in range(int(N)):
    print("Case #",i+1,":",' ',result_arr[i],sep='')