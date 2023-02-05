X=int(input())
N=int(input())

sum_of_things=0

datas_price_num=[]
for i in range(N):
    datas_price_num =input().split(' ')
    sum_of_things+=(int(datas_price_num[0])*int(datas_price_num[1]))


if sum_of_things==X:
    print('Yes')
else:
    print('No')