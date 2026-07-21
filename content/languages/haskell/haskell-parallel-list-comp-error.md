---
title: "[Solution] Haskell ParallelListComp Error"
description: "Fix Haskell ParallelListComp errors when using parallel list comprehension syntax."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

ParallelListComp errors occur when the extension is not enabled or when parallel list comprehensions have mismatched generator lengths.

## Common Causes

- ParallelListComp extension not enabled
- Generators in parallel have different lengths
- Missing then keyword in parallel comprehension
- Conflicting parallel and standard comprehension syntax

## How to Fix

### 1. Enable ParallelListComp

```haskell
{-# LANGUAGE ParallelListComp #-}

-- WRONG: No extension
-- result = [ (x, y) | x <- [1..3] | y <- ['a'..'c'] ]

-- CORRECT
result = [ (x, y) | x <- [1..3] | y <- ['a'..'c'] ]
```

### 2. Ensure generators are compatible

```haskell
{-# LANGUAGE ParallelListComp #-}

-- WRONG: Different lengths
-- pairs = [ (x, y) | x <- [1..3] | y <- [1..5] ]

-- CORRECT: Same length
pairs = [ (x, y) | x <- [1..3] | y <- [1..3] ]
```

## Examples

```haskell
{-# LANGUAGE ParallelListComp #-}

zipWith3_like :: [a] -> [b] -> [c] -> [(a, b, c)]
zipWith3_like xs ys zs = [ (x, y, z) | x <- xs | y <- ys | z <- zs ]

main :: IO ()
main = print (zipWith3_like [1,2,3] ['a'..'c'] [10,20,30])
```

## Related Errors

- [List comprehension error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Pattern match error](/languages/haskell/haskell-pattern-match)
