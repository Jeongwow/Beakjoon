date=input().split(' ')
time=int(input())

h=int(date[0])
m=int(date[1])

h_time=(m+time)//60

if h_time>0:
    if h+h_time>=24:
        h=h+h_time-24
        m=0-(60*h_time-(m+time))
    else:
        h+=h_time
        m=0-(60*h_time-(m+time))
        
else:
    m+=time
print(h,m,sep=' ')