from collections import Counter

def solve(m,n,l):
    cl = Counter(l)

    for _,v in cl.items():
        if v>=n:
            return n-1

    res = 0
    for _,v in cl.items():
        res += v

    return res


def fast_main():
    import io, os, sys
    input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        n,k = [int(x) for x in input().split()]
        l = [int(x) for x in input().split()]
        sys.stdout.write(str(solve(n,k,l)) + "\n")
        tc -= 1

fast_main()
