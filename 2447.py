import time
start = time.time()  # 시작 시간 저장

# 수행 속도 측정 => N=3**8일때   time : 6.173681259155273초

def recurrent(N):
    if N==1:
        return '*'
    
    recur=recurrent(N//3)
    local_result=[]
    
    for i in recur:
        local_result.append(i*3)
    # print(''.join(local_result))
    
    for i in recur:
        local_result.append(i+' '*(N//3)+i)
    # print(''.join(local_result))
    
    for i in recur:
        local_result.append(i*3)
    # print(''.join(local_result))
    
    return local_result
        



# N=int(input())
N=3**8

result=recurrent(N)
for i in range(len(result)):
    print(''.join(result[i]))
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

