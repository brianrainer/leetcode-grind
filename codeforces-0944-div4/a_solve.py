from collections import Counter


def fast_main():
    import io, os, sys
    input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        x,y = [int(x) for x in input().split()]
        sys.stdout.write(str(min(x,y)) + " " + str(max(x,y)) + "\n")
        tc -= 1

fast_main()
