---
title: "Type mismatch"
description: "A type mismatch occurs when an expression doesn't match the expected type."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["type", "mismatch", "compile", "haskell"]
weight: 5
---

## What This Error Means

A `Type mismatch` error occurs during compilation when the type of an expression doesn't match what's expected. Haskell has a strong static type system, so these errors are caught at compile time.

## Common Causes

- Passing wrong type to function
- Incorrect type annotation
- Mixing incompatible types
- Forgetting to convert between types

## How to Fix

```haskell
-- WRONG: Type mismatch
add :: Int -> Int -> Int
add x y = x + y

add 1 "hello"  -- Type mismatch: expected Int, got String

-- CORRECT: Use matching types
add 1 2  -- 3
```

```haskell
-- WRONG: Wrong type annotation
length :: Int -> Int
length xs = length xs  -- infinite recursion

-- CORRECT: Use correct type
length :: [a] -> Int
length [] = 0
length (_:xs) = 1 + length xs
```

## Examples

```haskell
-- Example 1: Wrong argument type
not "hello"  -- Type mismatch: expected Bool, got String

-- Example 2: Wrong return type
head :: [a] -> a
head (x:xs) = xs  -- Type mismatch: expected a, got [a]

-- Example 3: Mixing types
True + 1  -- Type mismatch: Can't match Bool with Int
```

## Related Errors

- [Variable not in scope](/languages/haskell/variable-not-in-scope)
- [GHC compilation error](/languages/haskell/ghc-error)
