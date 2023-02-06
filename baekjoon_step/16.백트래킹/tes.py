n = int(input())
def isTrue(x,y) :
    tmpArray=[['.']*n for i in range(n) ]
    tmpArray[x][y]='Q'
    idx=[]
    for i in range(n) :
        for j in range(n) :
            if tmpArray[i][y]!='Q' : 
                idx.append([i+n*y])
            if tmpArray[x][j]!='Q' : idx.append([x+n*j])
            if abs(i-x)-abs(j-y)==0 :
                if tmpArray[i][j]!='Q' : idx.append([i+n*j])
    
    return idx
i=0
tmpArray=isTrue(0,0)
for j in range(n) :
    if tmpArray[i+1][j]!='x':
        tmp=isTrue(i+1,j)
dic={'q':[0],'x':[2,3,4,5,6,9,11,13,15]}
for i in range(n*n):
    if i not in dic.get('x') :
        dic['q']=dic['q'].append(i)
        dic['x']=list(set(dic['x']+isTrue(i//n,i%n)))
    
            