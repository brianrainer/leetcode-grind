from solve import Solution

def main():
    sol = Solution()
    out = []
    with open('output.txt', 'r') as f:
        tc = int(f.readline())
        for _ in range(tc):
            out.append(f.readline().strip())
    
    with open('input.txt', 'r') as f:
        tcs = int(f.readline())
        for tc in range(1, tcs+1):
            inp = f.readline().strip()

            result = sol.eval(inp)
            
            print(inp)
            print('Case #%d: %s' % (tc, result))
            print(result == out[tc-1])

main()
