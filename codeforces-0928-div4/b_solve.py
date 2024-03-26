def solve(n, shape):
    prev = 0
    cur = 0
    for j in range(n):
        if shape[0][j] == '1':
            prev += 1
    for i in range(1, n):
        cur = 0
        for j in range(n):
            if shape[i][j] == '1':
                cur += 1
        if prev == cur and cur > 0:
            return "SQUARE"
        prev = cur
    return "TRIANGLE"

def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        n = int(input())
        shape = []
        for _ in range(n):
            l = input().decode()
            shape.append(l)
        sys.stdout.write(str(solve(n,shape)) + "\n")
        tc -= 1

fast()