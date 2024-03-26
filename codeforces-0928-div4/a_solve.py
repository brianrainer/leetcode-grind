def solve(s):
    a = 0
    for ch in s:
        if ch == 'A':
            a += 1
    return 'A' if a > 2 else 'B'


def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        s = input().decode()
        sys.stdout.write(str(solve(s)) + "\n")
        tc -= 1

fast()
