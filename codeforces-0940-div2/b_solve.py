def solve(n,k):
    res=[]
    bit=2
    i=0
    
    while k >= bit-1:
        res.append(bit-1)
        k -= bit-1
        bit <<= 1
    res.append(k)

    x=0
    while len(res)>=n:
        x+=res.pop()
    res.append(x)

    while len(res)<n:
        res.append(0)
    
    return " ".join([str(c) for c in res])


def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        n,k = [int(x) for x in input().strip().split()]
        sys.stdout.write(str(solve(n,k)) + "\n")
        tc -= 1

fast()