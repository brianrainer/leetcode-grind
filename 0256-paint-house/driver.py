from solve import Solution

def main():
    with open('input.txt', 'r') as f:
        testcase = int(f.readline())
        for tc in range(1, testcase+1):
            n = int(f.readline())
            costs = []
            for _ in range(n):
                l = [int(x) for x in f.readline().split(',')]
                costs.append(l)
            
            result = Solution.minCost(_, costs)
            print(costs)
            print('Case #%d: %d' % (tc, result))

main()
