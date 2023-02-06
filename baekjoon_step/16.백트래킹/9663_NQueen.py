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

    for i in raN:
        for j in raN:
            chess_map=[[1 for _ in raN] for _ in raN]
            chess_map=change(chess_map,[i,j])
            for k in raN:
                for l in raN:
                    if chess_map[k][l]==1:
                        chess_map=change(chess_map,[k,l])

            cnt_q=0
            for iqqi in raN:
                if 5 in chess_map[iqqi]:
                    cnt_q+=1
            if cnt_q==N:
                cnt+=1
                for prl in raN:
                    print(chess_map[prl])
                print()
        
    print(len(set_end_chess_map))
    print('cnt=',cnt)

if __name__=="__main__":
    main()
