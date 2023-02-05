import sys

all_remainder=set()
for i in range(10):
    N=int(input())
    all_remainder.add(N%42)

print(len(all_remainder))