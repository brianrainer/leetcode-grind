from collections import defaultdict

def solve(l):
    d = defaultdict(int)

    for x in l:
        d[x]+=1

    res = 0
    for v in d.values():
        res += v//3

    return res
    


def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        _ = int(input())
        l = [int(x) for x in input().strip().split()]
        sys.stdout.write(str(solve(l)) + "\n")
        tc -= 1

fast()