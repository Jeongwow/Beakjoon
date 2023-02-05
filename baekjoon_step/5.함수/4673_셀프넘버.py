def self_num(num,maxn):
    local_sn=[]
    while True:
        sum=0
        for j in num:
            sum+=int(j)
        if sum+int(num)>maxn:
            return local_sn
        ad=sum+int(num)
        local_sn.append(str(ad))
        num=str(ad)
    
n=10000
all_num=[i for i in range(n)]
all_num=list(map(str,all_num))
for i in range(1,n):
    print(i,'번째')
    if str(i) in all_num:
        rem=self_num(str(i),n)
        print(i,'는 스킵')
        
    for j in rem:
        if j in all_num:
            all_num.remove(j)
print('\n'.join(all_num))
        