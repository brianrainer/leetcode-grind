# Paint House
Tags: Dynamic Programming, O(n), Medium-Easy

## Intuition
We can break down the problem into its subproblem.

Working backwards from the last house to paint,
we need to calculate what is the total cost if we paint the current house with
a specific color, and forced to choose other color for the next house.

Formula is `dp[i][j] = costs[i][j] + minimum(dp[i+1][k] where j != k)`

## Approach
1. Initialize array to store DP. We can use 2D or 1D array
2. Loop from last house to first house, for each house
we need to calculate the total cost if we pick that color,
compounded by the minimum total of the next house of different colors

## Complexity
Time complexity: $$ O(nc) $$
where `n` is length of `costs` and `c` is how many color options.
In this problem, the color is 3 so we the total time complexity is $$ O(n) $$

Space complexity: $$ O(nc), can be improved to O(c) $$
We need to store total min cost for each house. I'll leave how to improve
the space complexity to $$ O(c) $$ as an exercise.

## Code
```
def min_cost(c) -> int:
    n = len(c)
    dp = [[0 for _ in range(3)] for _ in range(n)]
    dp[n-1] = c[n-1]
    for i in range(n-2,-1,-1):
        for j in range(3):
            dp[i][j] = c[i][j] + min([dp[i][k] for k in range(3) if j != k])
    return min(dp[0])
```

## Key Learning
* When encountering words `minimize` or `maximize` it might be
a hint for a Dynamic Programming.
* Working backwards from the final house to paint
makes the problem easy to visualize
* Similar to [198. House Robber](https://leetcode.com/problems/house-robber/description)
