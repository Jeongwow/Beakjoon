import sys

T=int(input())

ori=T
now=T
cnt=0
while True:
    one=now%10
    if now<10:
        two=0
    else:
        two=now//10
    
    sum_sec=(one+two)%10
    now=one*10+sum_sec
    cnt+=1
    if ori==now and cnt!=0:
        break
    
print(cnt)