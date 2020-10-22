def big_number_sum(a,b):
    arraylen=max(len(a),len(b))+1
    alist=[int(i) for i in a][::-1]+[0]*(arraylen-len(a))
    blist=[int(i) for i in b][::-1]+[0]*(arraylen-len(b))
    result=[0]*arraylen
    for i in range(arraylen):
        temp=alist[i]+blist[i]+result[i]
        if temp>=10:
            result[i]=temp-10
            result[i+1]=1
        else:result[i]=temp
    if result[-1]==0:
        result.pop()
    result_reverse=result[::-1]
    result_string=''.join([str(i) for i in result_reverse])
    return result_string
a=big_number_sum('123456789','999999')
print(a)