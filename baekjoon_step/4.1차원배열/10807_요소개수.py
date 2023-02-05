import sys
N=int(input())
data=list(map(int,sys.stdin.readline().rstrip().split(' ')))
v=int(input())

my_dict={}
for i in range(N):
    if data[i] in my_dict:
        my_dict[data[i]]=my_dict[data[i]]+1
    else:
        my_dict[data[i]]=1

# dict.get(v,0) --> dict에 v가 존재하면 return value,  없으면 return 0
print(my_dict.get(v,0))