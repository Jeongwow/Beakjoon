import sys

T=int(input())

for i in range(T):
    print(' '*(T-(int(i)+1)),'*'*(int(i)+1),sep='')
