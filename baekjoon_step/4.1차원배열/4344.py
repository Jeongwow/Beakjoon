import sys

N=int(input())

rate=[]

for k in range(N):
    data=list(map(int,sys.stdin.readline().rstrip().split(' ')))
    stu_num=data[0]
    data.pop(0)
    means=sum(data)/stu_num
    rate_num=0
    for j in data:
        if j>means: rate_num+=1
    
    rate.append(round(rate_num/stu_num*100,3))
    


for i in range(N):
    print(f'{rate[i]:.3f}%')
    # print(means[i]) 
