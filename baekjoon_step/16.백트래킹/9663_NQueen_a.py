import copy
def rec(floor,Map):
    # reccurent
    if floor==N:
        Q_cnt=0
        for iqqi in range(N):
            Q_cnt+=Map[iqqi].count(5)
        if Q_cnt==N:
                result.append(Map)
        return
    CanGo=[]
    for idx in range(N):
        if Map[floor][idx]==1:
                CanGo.append(idx)
    if CanGo==[]:
        rec(floor+1,Map)
    else :
        for i in CanGo:
            local_map=copy.deepcopy(Map)
            NewMap=change(Map,[floor,i])
            rec(floor+1,NewMap)
            Map=local_map

def change(cmap,pos):
    leng=len(cmap)
    raN=range(leng)
    cmap[pos[0]][:]=[0 for _ in raN] 
    # 열을 0으로
    for tmp in range(leng):
        cmap[tmp][pos[1]]=0
    for k in range(-leng+1,leng): # 수정필요할지도..
        if pos[0]+k>=0 and pos[0]+k<leng:
            if pos[1]+k>=0 and pos[1]+k<leng:
                cmap[pos[0]+k][pos[1]+k]=0
        if pos[0]+k>=0 and pos[0]+k<leng:
            if pos[1]-k>=0 and pos[1]-k<leng:
                cmap[pos[0]+k][pos[1]-k]=0
    cmap[pos[0]][pos[1]]=5
    return cmap


N=int(input())
raN=range(N)
result=[]
cnt=0
f_chess_map=[[1 for _ in raN] for _ in raN]

for i in raN:
    for j in raN:
        chess_map=copy.deepcopy(f_chess_map)
        chess_map=change(chess_map,[i,j])
        rec(0,chess_map)

res=[]
for num in range(len(result)):
    Q_cnt=0
    for i in raN:
        Q_cnt+=result[num][i].count(5)
    if Q_cnt==N:
        res.append(result[num])
idx_list=set()

for i in range(len(res)):
    for j in range(i+1,len(res)):
        if res[i]==res[j]:
            idx_list.add(i)

for i in sorted(idx_list,reverse=True):
    res.pop(i)     


print(len(res))