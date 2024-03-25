# codeforces contest 953 division 3 problem D
# D Seraphimi the Owl
# https://codeforces.com/contest/1945/problem/D

def solve(n,m,a,b):
    ans = float('inf')
    for i in range(n-1, -1, -1):
        if i < n-1:
            a[i] += min(a[i+1], b[i+1])
            b[i] += min(a[i+1], b[i+1])
        if i < m:
            ans = min(ans, a[i])
    return ans

def fast():
    import io, os, sys
    input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

    tc = int(input())
    while tc:
        n,m = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]

        sys.stdout.write(str(solve(n,m,a,b)) + "\n")

        tc -= 1

fast()