import sys

while True:
    try:
        data = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    except:
        break
    print(f'{data[0]+data[1]}')
