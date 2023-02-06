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
    # print('=====================')
    # for prl in raN:
    #     print(cmap[prl])
    # print('=====================')
    return cmap

def main():
    N=int(input())

    raN=range(N)
    set_end_chess_map=[]
    global cnt
    cnt=0
    qenum=N
    for i in raN:
        for j in raN:
            chess_map=[[1 for _ in raN] for _ in raN]
            chess_map=change(chess_map,[i,j])
            end_his_map=[[0 for _ in raN] for _ in raN]
            end_his_map[i][j]=1
            sf=0
            for k in raN:
                for l in raN:
                    bp=0
                    if chess_map[k][l]==1:
                        chess_map=change(chess_map,[k,l])
                        end_his_map[k][l]=1
                    for lst in raN:
                        if 1 in chess_map[lst]:
                            bp+=1
                    if bp==N:
                        break
                if bp==N:
                    cnt+=1
                    break
            # for cntnum in range(len(set_end_chess_map)):
            #     if end_his_map == set_end_chess_map[cntnum]:
            #         sf=1
            # if sf==0:
            # set_end_chess_map.append(end_his_map)
            # print(end_his_map)
            print(chess_map)
            # print('=====================')
            # for prl in raN:
            #     print(chess_map[prl])
            # print('=====================')
    print(len(set_end_chess_map))
    # for qqq in range(len(set_end_chess_map)):
        # print(set_end_chess_map[qqq])
    print('cnt=',cnt)

if __name__=="__main__":
    main()

