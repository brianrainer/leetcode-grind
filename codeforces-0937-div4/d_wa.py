def solve(n):

    def is_bin(x):
        res = x
        while res:
            if res%10 > 1:
                return False
            res //= 10
        return True
    
    if is_bin(n):
        return "YES"
    
    while n % 10 == 0:
        n //= 10

    def factorize(x):
        res = x
        i = 2
        fdict = {}
        while i*i <= x:
            if res % i == 0:
                fdict[i] = 0
                while res % i == 0:
                    fdict[i] += 1
                    res //= i
            i += 1
        if res > 1:
            fdict[res] = 1
        return fdict

    fdict = factorize(n)
    for k in fdict.keys():
        if not is_bin(k):                
            return "NO"

    return "YES"

def main():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        x = int(input())
        sys.stdout.write(str(solve(x)) + "\n")
        tc -= 1

main()