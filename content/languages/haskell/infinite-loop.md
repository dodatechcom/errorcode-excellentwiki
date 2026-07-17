---
title: "Infinite loop / stack overflow"
description: "An infinite loop occurs when a function calls itself indefinitely, eventually causing a stack overflow."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An infinite loop occurs when a recursive function never reaches its base case, causing infinite recursion. This eventually exhausts the call stack, resulting in a stack overflow. Haskell's lazy evaluation can sometimes hide infinite loops.

## Common Causes

- Missing base case in recursion
- Recursive call doesn't make progress
- Lazy evaluation hiding infinite structures
- Mutual recursion without termination

## How to Fix

```haskell
-- WRONG: No base case
factorial :: Integer -> Integer
factorial n = n * factorial (n - 1)  -- infinite loop

-- CORRECT: Add base case
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)
```

```haskell
-- WRONG: Infinite lazy list
infinite :: [Int]
infinite = 1 : infinite  -- infinite list

-- CORRECT: Use finite generation
finite :: [Int]
finite = take 100 [1..]  -- finite
```

## Examples

```haskell
-- Example 1: Infinite recursion
f = f  -- infinite loop

-- Example 2: Wrong base case
countdown n = countdown (n + 1)  -- goes up forever

-- Example 3: Lazy infinite structure
ones = 1 : ones  -- infinite list of 1s
head ones  -- works, but:
sum ones   -- infinite loop
```

## Related Errors

- [Pattern match failure](/languages/haskell/pattern-match)
- [Non-exhaustive patterns](/languages/haskell/non-exhaustive)
