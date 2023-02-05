"""
한수 => 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
"""

N=int(input())
cnt=0
for i in range(1,N+1):
    stri=str(i)
    term=1000000
    if i<100:
        cnt+=1
        continue
    else:
        old_term=999
        no_flag=0
        for j in range(1,len(stri)):
            new_term=int(stri[j])-int(stri[j-1])
            if j!=1 and old_term!=new_term:
                no_flag=1
                break
            old_term=new_term
        if no_flag==0:
            cnt+=1
print(cnt)