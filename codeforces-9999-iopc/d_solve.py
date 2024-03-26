def solve(n,t,arr):
    arr.sort()
    arr.reverse()

    if arr[0] > t:
        return -1

    cnt = sum([1 for x in arr if x == t])
    arr = [x for x in arr if x != t]

    m = len(arr)
    res = m
    server = []

    def dfs(i):
        nonlocal res
        
        if len(server) >= res:
            return
        
        if i == m:
            res = min(res, len(server))
            return

        for j in range(len(server)):
            if server[j] + arr[i] <= t:
                server[j] += arr[i]
                dfs(i+1)
                server[j] -= arr[i]
        
        server.append(arr[i])
        dfs(i+1)
        server.pop()

    dfs(0)
    return res + cnt

def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n, t = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    sys.stdout.write(str(solve(n,t,arr)) + "\n")

def fast_tc():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        n, t = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]
        sys.stdout.write(str(solve(n,t,arr)) + "\n")
        tc -= 1

fast()
