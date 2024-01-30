from solve import Solution

def main():
    sol = Solution()
    out = []
    with open('output.txt', 'r') as f:
        tc = int(f.readline())
        for _ in range(tc):
            out.append(int(f.readline()))

    with open('input.txt', 'r') as f:
        testcases = int(f.readline())
        for tc in range(1, testcases+1):
            tokens = f.readline().strip().split(' ')
            result = sol.evalRPN(tokens)
            print(tokens)
            print('Case #%d: %d' % (tc, result))
            print(result == out[tc-1])

main()
