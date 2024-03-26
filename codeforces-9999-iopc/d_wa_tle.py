import heapq

def solve(n,t,arr):
    arr.sort()
    arr.reverse()

    if arr[0] > t:
        return -1

    ans = []

    for x in arr:
        is_found = False
        for j in range(len(ans)):
            if ans[j] + x <= t:
                ans[j] += x
                is_found = True
                break
        if not is_found:
            ans.append(x)

    return len(ans)

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

fast_tc()