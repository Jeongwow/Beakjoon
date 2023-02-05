import numpy as np
import time
start = time.time()  # 시작 시간 저장

N=int(input())

length = N//3
hole=3
# N=3 초기 numpy array 형성
result=np.array([['*','*','*'],['*',' ','*'],['*','*','*']])

if N==3:
    for i in range(len(result)):
        print(''.join(result[i]))
else:
    """
    while문을 통해 규칙성을 갖는 '*'을 출력함.
    (N=3k이며, 이때 1 ≤ k < 8) 각 N에 대해 
    규칙성을 갖는 블럭을 split하여 생각해보면,
    9개로 나눌 수 있다. 또 이것을 나눠서 생각해보면
    총 3개의 row vector가 연결되어 있는 것으로 떠올려 볼 수 있다.
    3개의 row vector에 대한 규칙성으로 '*'과 ' '를 numpy array에
    추가하여 원하는 패턴의 '*'을 출력 할 수 있다.
    np.append의 axis설정 개념을 통해 코드를 작성하였다.
    
    수행 속도 측정 => N=3**8 일때  time : 14.116699695587158 초
    """
    while length>1:
        tmp_empty=np.array([[' ' for _ in range(hole)] for _ in range(hole)])
        local_result=result
        for i in range(3):
            if i==1:
                tmp_arr=np.array(local_result)
                tmp_arr=np.append(tmp_arr,tmp_empty,axis=1)
                tmp_arr=np.append(tmp_arr,local_result,axis=1)
                result=np.append(result,tmp_arr,axis=0)
            else:
                tmp_arr=np.array(local_result)
                tmp_arr=np.append(tmp_arr,local_result,axis=1)
                tmp_arr=np.append(tmp_arr,local_result,axis=1)
                if i==0:
                    result=np.array(tmp_arr)
                else:
                    result=np.append(result,tmp_arr,axis=0)
        hole*=3
        length//=3

# 마지막 출력층
for i in range(N):
    print(''.join(result[i]))
    
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간


