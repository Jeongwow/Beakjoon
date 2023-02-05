import sys

N=int(input())
score=[0]*N

for k in range(N):
    answer=list(map(str,sys.stdin.readline().rstrip()))
    cor_cnt=0
    for i in answer:
        if i=='O':
            cor_cnt+=1
        else:
            cor_cnt=0
        score[k]+=cor_cnt
score=map(str,score)
print('\n'.join(score))
