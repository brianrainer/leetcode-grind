def solve(s):
    n = len(s)
    cut = 1
    first = False
    for i in range(1, n):
        if s[i] != s[i-1]:
            cut += 1
            if not first and (s[i-1] == '0' and s[i] == '1'):
                cut -= 1
                first = True
    return cut
    


def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        s = input().decode().strip()
        sys.stdout.write(str(solve(s)) + "\n")
        tc -= 1

fast()