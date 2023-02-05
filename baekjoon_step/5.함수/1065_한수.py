"""
한수 => 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
"""

N=int(input())

for i in range(N):
    stri=str(i)
    for j in i:
        