import collections

def solve(s):
    c = collections.Counter(s)

    if len(c) == 1:
        return "NO"
    return "YES\n{}".format(s[1:] + s[:1])
    


def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        s = input().decode().strip()
        sys.stdout.write(str(solve(s)) + "\n")
        tc -= 1

fast()