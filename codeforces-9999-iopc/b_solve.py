def solve(s):
    n = len(s)
    ans = n - 1

    for i in range(3, n):
        cnt = i-3
        if s[i-3] != 'O':
            cnt += 1
        if s[i-2] != 'D':
            cnt += 1
        if s[i-1] != 'O':
            cnt += 1
        if s[i  ] != 'O':
            cnt += 1
        cnt += n-i-1

        ans = min(ans, cnt)

    return ans


def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        s = input().decode().strip()
        sys.stdout.write(str(solve(s)) + "\n")
        tc -= 1

fast()