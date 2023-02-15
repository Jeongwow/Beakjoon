a=input()
time=0
# print(ord('Z'))
for i in a:
    if ord(i)>=65 and ord(i)<=67: #2
        time+=3
    elif ord(i)>=68 and ord(i)<=70: #3
        time+=4
    elif ord(i)>=71 and ord(i)<=73: #4
        time+=5
    elif ord(i)>=74 and ord(i)<=76: #5
        time+=6    
    elif ord(i)>=77 and ord(i)<=79: #6
        time+=7
    elif ord(i)>=80 and ord(i)<=83: #7
        time+=8
    elif ord(i)>=84 and ord(i)<=86: #8
        time+=9
    elif ord(i)>=87 and ord(i)<=90: #9
        time+=10

print(time)