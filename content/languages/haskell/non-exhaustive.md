---
title: "Non-exhaustive patterns"
description: "Non-exhaustive patterns occur when a function doesn't cover all possible input cases."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["non-exhaustive", "patterns", "incomplete", "haskell"]
weight: 5
---

## What This Error Means

A `Non-exhaustive patterns` warning (which becomes a runtime error) occurs when a function's pattern matching doesn't cover all possible input values. The compiler may warn about this with `-Wincomplete-patterns`.

## Common Causes

- Missing cases for data constructors
- Not handling empty lists
- Missing catch-all patterns
- Incomplete guards

## How to Fix

```haskell
-- WARNING: Non-exhaustive patterns in function 'tail'
safeTail :: [a] -> [a]
safeTail (x:xs) = xs
-- Missing: safeTail [] = []

-- CORRECT: Add all cases
safeTail :: [a] -> [a]
safeTail (x:xs) = xs
safeTail []      = []
```

```haskell
-- WARNING: Non-exhaustive pattern
describe :: Bool -> String
describe True = "yes"
-- Missing: describe False = "no"

-- CORRECT: Cover all constructors
describe :: Bool -> String
describe True  = "yes"
describe False = "no"
```

## Examples

```haskell
-- Example 1: Missing list case
head' (x:_) = x
-- head' [] crashes

-- Example 2: Missing Bool case
not' True = False
-- not' False crashes

-- Example 3: Missing Maybe case
fromJust (Just x) = x
-- fromJust Nothing crashes
```

## Related Errors

- [Pattern match failure](/languages/haskell/pattern-match)
- [Variable not in scope](/languages/haskell/variable-not-in-scope)
