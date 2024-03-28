def solve(n):
    import sys
    n *= 2
    for i in range(n):
        s = ''
        flip = i%4 < 2
        for j in range(n):
            if j%4 < 2:
                if flip:
                    s += '#'
                else:
                    s += '.'
            else:
                if flip:
                    s += '.'
                else:
                    s += '#'
        sys.stdout.write(str(s) + "\n")

def main():
    import io,os
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        n = int(input())
        solve(n)
        tc -= 1

main()