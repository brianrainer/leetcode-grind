# codeforces contest 953 division 3
# A - Setting Up Camp
# https://codeforces.com/contest/1945/problem/A

def solve(i,j,k):
    ans = i
    if j%3 != 0:
        mj = j % 3
        if mj + k < 3:
            return -1
        ans += 1
        k -= (3 - mj)
    ans += j//3
    ans += k//3
    if k % 3 != 0:
        ans += 1
    return ans

def main():
    tc = int(input().strip())
    while tc:
        i,j,k = [int(x) for x in input().strip().split()]
        print("%d\n" % solve(i,j,k))
        tc -= 1

def fast_main():
    import io, os, sys
    input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        i,j,k = [int(x) for x in input().split()]
        sys.stdout.write(str(solve(i,j,k)) + "\n")
        tc -= 1

fast_main()
