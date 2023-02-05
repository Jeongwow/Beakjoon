"""
먼저 self number 조건에 해당하는 숫자를 1~N 리스트에서 
remove하는 방식으로 코드를 구현함. 먼저 문제의 주제가 함수
인 만큼 1부터 n까지의 반복문을 돌며 그 숫자로 인해 생성되는 
다른 숫자들을 self number에서 제거하였다. 모든 숫자는 생성자로써
다른 숫자하나를 생성하게 되므로 1~n까지 반복문을 도는 것을 피하지
못할 것이라 생각함. 처음 방식은 while문 하나와 for문 3개로 구성되었기 
때문에 다소 시간이 많이 걸렸고, 이 문제를 해결하기 위해 생각을 
전환하여 반복문을 줄이는 작업을 진행하였다.
"""

def self_num(n):
    sum_n=0
    n=str(n)
    for i in n:
        sum_n+=int(i)
    return sum_n+int(n)

N=10000
self_set=[i for i in range(1,N)]
for i in range(1,N):
    testN=self_num(i)
    if testN in self_set:
        self_set.remove(testN)
for i in range(len(self_set)):
    print(self_set[i])