# Evaluate Reverse Polish Notation
Tags: Stack, Easy, O(n)

## Intuition
At first glance, there are two types of characters in the tokens:
either numbers or operation. We need to treat them differently.

To efficiently calculate we can use a Stack
to store the numbers, and everytime we encounter an operation symbol,
we pop back the last two numbers and add the result back.

## Approach
1. Initialize stack
2. Loop through `tokens`, if character is number,
add to stack, and if it's not, pop the last two numbers from stack,
calculate the result, and add back to stack

## Complexity
- Time complexity: $$O(n)$$
Loop through `tokens` which has `n` elements.
- Space complexity: $$O(n)$$
At most the stack is filled with `n` numbers.

## Code
```
def rev_polish(t):
    s = []
    for x in t:
        if x not in "+-*/":
            s.append(int(x))
        else:
            p = s.pop()
            q = s.pop()
            if x == '+':
                s.append(q+p)
            if x == '*':
                s.append(q*p)
            if x == '-':
                s.append(q-p)
            if x == '/':
                s.append(int(q/p))
    return s.pop()
```

## Key Learning
* When you are familiar with Stack, this problem
becomes trivial / easy.
* Need to be careful of the order of operation.
`a-b != b-a`, and stack behaviour is last in first out.
* Also need to be careful of decimal truncation.
In python `//` is floor, and for operations involving
negative numbers it can give wrong results.
