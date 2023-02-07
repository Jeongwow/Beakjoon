import copy
def rec(N,Map,Total_len):
    global cnt
    global result
    # reccurent
    if N==Total_len:
        Q_cnt=0
        for iqqi in range(Total_len):
            Q_cnt+=Map[iqqi].count(5)
        if Q_cnt==Total_len:
            if Map not in result:
                for ab in range(Total_len):
                    print(Map[ab])
                print()
                cnt+=1
                result.append(Map)
        return
    
    CanGo=[]
    for idx in range(Total_len):
        if Map[N][idx]==1:
                CanGo.append(idx)
    if CanGo==[]:
        rec(N+1,Map,Total_len)
    else :
        for i in CanGo:
            local_map=copy.deepcopy(Map)
            NewMap=change(Map,[N,i])
            rec(N+1,NewMap,Total_len)
            Map=copy.deepcopy(local_map)



def change(inmap,pos):
    cmap=inmap
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

def main():
    N=int(input())
    raN=range(N)
    global cnt
    global result
    result=[]
    cnt=0
    for i in raN:
        for j in raN:
            chess_map=[[1 for _ in raN] for _ in raN]
            chess_map=change(chess_map,[i,j])
            rec(0,chess_map,N)


    print('cnt=',cnt)

if __name__=="__main__":
    main()


"""
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])
"""