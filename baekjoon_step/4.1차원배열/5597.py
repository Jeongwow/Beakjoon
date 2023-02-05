import sys

no_submit=[i for i in range(1,31)]
# print(no_submit)

for i in range(28):
    num=int(input())
    no_submit.remove(num)
no_submit=map(str,no_submit)
print('\n'.join(no_submit))
    
    