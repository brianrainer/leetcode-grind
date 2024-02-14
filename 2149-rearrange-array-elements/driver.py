from solve import Solution

def main():
    sol = Solution()
    out = []
    with open('output.txt', 'r') as f:
        tc = int(f.readline())
        for _ in range(tc):
            outp = f.readline().strip()
            res = [int(x) for x in outp.split(',')]
            out.append(res)
    
    with open('input.txt', 'r') as f:
        tcs = int(f.readline())
        for tc in range(1, tcs+1):
            inp = f.readline().strip()
            nums = [int(x) for x in inp.split(',')]

            result = sol.rearrangeArray(nums)
            
            print(inp)
            print('Case #%d: %s' % (tc, result))
            print(result == out[tc-1])

main()
