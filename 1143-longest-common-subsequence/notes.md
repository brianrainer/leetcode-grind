# Longest Common Substring
Tags: Dynamic Programming, Medium, Classic

## Intuition
We cannot use Brute Force since to generate all the subsequence
of both string and comparing them would have time complexity of $$ O(2^m * 2^n) $$
which is too large for constraint $$ 1 <= m, n <= 1000 $$

We cannot use Greedy as well because it can lead to wrong answer
by taking suboptimal solution when there are an early match.

Instead we need to break down the problem into its subproblem.

For each character, we compare with every other character:

* If they match then we can increment the current max streak and
incorporate both characters into the current longest common subsequence.

* If they don't then we need to ignore *one* character,
either from `text1` or `text2`, and we can do this by taking the max
of `[i-1][j] or [i][j-1]`

Consider this table:

|*|*|**t**|**c**|**a**|**g**|**g**|**t**|**a**|**c**|**t**|
|-|-|-|-|-|-|-|-|-|-|-|
|*|0|0|0|0|0|0|0|0|0|0|
|**g**|0|0|0|0|1|1|1|1|1|1|
|**c**|<mark>0</mark>|0|1|1|1|1|1|1|2|2|
|**t**|0|<span style="background-color: #ff0000">1</span>|1|1|1|1|2|2|2|3|
|**c**|0|1|<span style="background-color: #ff0000">2</span>|<mark>2</mark>|<mark>2</mark>|2|2|2|3|3|
|**g**|0|1|2|2|3|<span style="background-color: #ff0000">3</span>|<mark>3</mark>|3|3|3|
|**a**|0|1|2|3|3|3|3|<span style="background-color: #ff0000">4</span>|4|4|
|**c**|0|1|2|3|3|3|3|4|<span style="background-color: #ff0000">5</span>|5|
|**t**|0|1|2|3|3|3|4|4|5|<span style="background-color: #ff0000">6</span>|
|**g**|0|1|2|3|4|4|4|4|5|<mark>6</mark>|

We compare string `tcaggtact` with `gctcgactg`.
When we found a match (marked by red highlight), we increment the current max streak and incorporate the character
and if we don't found a match (marked by yellow highlight), we take the current max streak and continue it 
so it can be considered by the next match along the comparison.

In this example, the final LCS is `tcgact` (from `tc**g*act*` and `**tcgact*`).

## Approach
1. Initialize 2D array to store DP calculation
2. For each previous character we compare and check
if they are the same ( `text1[i-1] == text2[j-1]` ),
if it is then we can add the current maximum LCS:
`dp[i][j] = 1 + dp[i-1][j-1]`
3. If not then we skip one character, either from the first text 
or the second text, by taking the maximum of `dp[i-1][j]` or `dp[i][j-1]`

## Complexity
- Time: $$ O(mn) $$
where `m` is length of `text1` and
`n` is length of `text2`.

- Space: $$ O(mn) $$
we use 2D array to store the bottom up DP calculation
comparing the two strings

## Code
```
def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

## Key Learning
* When dealing with longest subsequence we can consider using
dynamic programming.
* Break down problems into it's subproblem and think carefully.
