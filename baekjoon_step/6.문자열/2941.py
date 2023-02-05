import sys
string=list(map(str,sys.stdin.readline().rstrip()))

cnt=1

if len(string)==1:
    print(cnt)
else:    
    for i in range(1,len(string)):
        if string[i]=='=' and (string[i-1]=='c' or string[i-1]=='s'):
            cnt-=1
        elif string[i]=='=' and string[i-1]=='z':
            if i>1 and string[i-2]=='d':
                cnt-=2
            else:
                cnt-=1
        elif string[i]=='-' and (string[i-1]=='c' or string[i-1]=='d'):
            cnt-=1
        elif string[i]=='j' and (string[i-1]=='l' or string[i-1]=='n'):
            cnt-=1
        cnt+=1
    print(cnt)