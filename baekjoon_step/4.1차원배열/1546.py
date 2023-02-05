import sys

N=int(input())
data=list(map(int,sys.stdin.readline().rstrip().split(' ')))
# print(data)
max_s=max(data)
new_score=[]
for i in data:
    new_score.append(i/max_s*100)
print(sum(new_score)/len(data))
