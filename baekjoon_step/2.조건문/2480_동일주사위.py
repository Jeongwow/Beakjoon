data=input().split(' ')

data[0]=int(data[0])
data[1]=int(data[1])
data[2]=int(data[2])


same_num=0

for i in range(len(data)):
    for j in range(len(data)):
        if j>i and data[i]==data[j] and same_num!=2:
            same_num+=1
            last_same_idx=j

if same_num==2:
    print(data[last_same_idx]*1000+10000)
elif same_num==1:
    print(data[last_same_idx]*100+1000)
else:
    print(max(data)*100)