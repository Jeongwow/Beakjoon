inp=input().split(' ')
inp=list(map(int,inp))
A=inp[0]
B=inp[1]
C=inp[2]

sell_num=0
if B>=C:
    sell_num=-1
else:
    sell_num=A//(C-B)+1
print(sell_num)