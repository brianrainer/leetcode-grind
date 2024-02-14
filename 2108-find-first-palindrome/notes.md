# Find First Palindrome
#easy #O(nm)

## Intuition
very straightforward, loop through the array
check if it is a palindrome and return the first occurrence.

## Approach: List Comprehension / Reverse
1. Loop through the list of words, for each string
2. Create the reversed string, and compare it with the original
If palindrome then we found it

```python
def first_palindrome(words: List[str]) -> str:
    for s in words:
        if s == s[::-1]:
            return s
    return ""
```

## Complexity
- Time Complexity   : $$ O(nm) $$
where `n` is length of array words and `m` is length of string 
- Space Complexity  : $$ O(m) $$
we use constant space `m` length when creating the reversed string


## Approach: Two Pointers
1. Loop through array words and for each string
2. Use two pointer start and end, and compare until 
they don't match, or the pointer cross each other. If they do,
then we found a palindrome.

```python
def first_palindrome(words: List[str]) -> str:
    for s in words:
        start, end = 0, len(s)-1
        while start <= end:
            if s[start] != s[end]:
                break
            start += 1
            end -= 1
        if start > end:
            return s
    return ""
```

## Complexity
- Time Complexity   : $$ O(nm) $$
where `n` is length of array words and `m` is length of string
- Space Complexity  : $$ O(1) $$
we use constant space for additional two pointers.

## Key Learning
- In python you can use list comprehension `[::-1]`
to get the list in reversed order.
