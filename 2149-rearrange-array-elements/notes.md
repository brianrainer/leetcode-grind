# Rearrange Array Elements by Sign
#easy #O(n)

## Intuition
There are two approach: to use two pointers
or to use additional list or queue to separate the
positive and negative numbers. Both need additional
O(n) space, and many people got trapped thinking this
problem can be solved in O(1) additional space.

## Approach: Additional List / Brute Force
1. Create two variables to temporarily hold
positive and negative numbers
2. Iterate through the list and separate the numbers
to their respective queues
3. Build back the initial list

```python
def rearrangeArray(nums: List[int]) -> List[int]:
    plus = []
    minus = []
    for x in nums:
        if x < 0:
            minus.append(x)
        else:
            plus.append(x)
    ans = []
    for i in range(len(plus)):
        ans.append(plus[i])
        ans.append(minus[i])
    return ans
```

## Complexity
- Time Complexity   : $$ O(n) $$
We loop through the array twice with array length `n`
- Space Complexity  : $$ O(n) $$
We use additional space to hold the numbers


## Approach: Two Pointers
1. Create an empty list to hold the results
2. Create two pointers, for positive and negative signs
3. Iterate through the array, when you find the 
positive numbers, set the result array, and add the positive pointer by two.
Do the same for negative numbers

```python
def rearrangeArray(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [None for _ in range(n)]
    plus = 0
    minus = 1

    for x in nums:
        if x < 0:
            ans[minus] = x
            minus += 2
        else:
            ans[plus] = x
            plus += 2
    return ans
```

## Complexity
- Time Complexity   : $$ O(n) $$
We loop through the array once with length `n`
- Space Complexity  : $$ O(n) $$
We use two pointers and additional space to hold the answer


## Key Learning
- Sometimes some problem cannot be optimized further.
This problem's best solution is still O(n) and not O(1)
because we have to keep the order of the number appearance.
- In python you can set `None` as a default value
when creating it in list comprehension.
