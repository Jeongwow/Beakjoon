import sys
strdata=list(map(str,sys.stdin.readline().rstrip()))

result=[]

for i in range(ord('a'),ord('z')+1):
    if chr(i) in strdata:
        result.append(strdata.index(chr(i)))
    else:
        result.append(-1)
result=list(map(str,result))
print(' '.join(result))
