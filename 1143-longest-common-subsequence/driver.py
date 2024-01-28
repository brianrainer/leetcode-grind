from solve import Solution

def main():
    with open('input.txt', 'r') as f:
        print('1143. Longest Common Subsequence')
        testcase = int(f.readline())
        for _ in range(testcase):
            text1 = str(f.readline()).strip()
            text2 = str(f.readline()).strip()
            result = Solution.longestCommonSubsequence(_, text1, text2)
            print(text1, text2, result, sep='\n')
        f.close()

main()