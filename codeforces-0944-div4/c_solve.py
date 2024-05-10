import collections

def solve(a,b,c,d):

    a,b = min(a,b), max(a,b)
    c,d = min(c,d), max(c,d)

    count = 0
    while a<b:
        if a==c or a==d:
            count +=1
        a+=1
    
    if count == 1:
        return "YES"
    return "NO"
    


def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        a,b,c,d = [int(x) for x in input().split()]
        sys.stdout.write(str(solve(a,b,c,d)) + "\n")
        tc -= 1

fast()