def modexp(x,n,p):
    if n==0:
        return 1
    t=(x*x)%p
    tmp=modexp(t,n>>1,p)
    if n%2!=0:
        tmp=(tmp*x)%p
    return tmp
a=modexp(3,1254,10)
a