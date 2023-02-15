
# inp=''.join(input())
inp=input().upper()
checked_char=[]
max_cnt=0
max_idx=0
ifsame=False
for i in range(len(inp)):
    tmp_cnt=0
    if inp[i] not in checked_char:
        checked_char.append(inp[i])
        for j in range(i,len(inp)):
            if inp[i]==inp[j]:
                tmp_cnt+=1
    if tmp_cnt==max_cnt and max_cnt!=0:
        s_flag=True
    if tmp_cnt>max_cnt:
        max_idx=i
        max_cnt=tmp_cnt
        s_flag=False
if s_flag:
    print("?")
else:
    print(inp[max_idx])