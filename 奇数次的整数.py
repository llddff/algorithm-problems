def find_lost_num(l):
    xorresult=0
    n=len(l)
    result=[0,0]
    for i in range(n):
        xorresult^=l[i]
    if xorresult==0:
        print('输入有误')
    seperator=1
    while seperator&xorresult==0:
        seperator<<=1
    for i in range(n):
        if seperator&l[i]==0:
            result[0]^=l[i]
        else:
            result[1]^=l[i]
    return result

l=[4,1,2,2,5,1,4,3,3,5]
a=find_lost_num(l)
print(a)