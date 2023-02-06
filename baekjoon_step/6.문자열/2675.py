import sys
N=int(input())
string=[]
re=[]
newStr=[]
for i in range(N):
    data=list(input().split(' '))

    re.append(data[0])
    string.append(list(data[1][:]))
for i in range(N):
    newStr=[]
    for j in string[i]:
        newStr.append([j*int(re[i])])
    for k in newStr:
        print(k[0],end='')
    print()