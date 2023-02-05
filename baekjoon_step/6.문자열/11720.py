import sys
N=int(input())
strdata=list(map(int,sys.stdin.readline().rstrip()))
su=0
for i in strdata:
    su+=i
print(su)
    