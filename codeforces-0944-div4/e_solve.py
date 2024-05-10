def solve(a,b,x):
    a = [0] + a
    b = [0] + b

    n = len(a)
    lo = 0
    hi = n-1
    return 0
    


def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        n,k,q = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        res = []
        while q:
            x = int(input())
            res.append(solve(a,b,x))
            q -= 1
        for i in range(len(res)-1):
            sys.stdout.write(str(res[i]) + " ")
        sys.stdout.write(str(res[-1]) + "\n")
        tc -= 1

fast()