---
title: "[Solution] Haskell Bang Pattern Error"
description: "Fix Haskell bang pattern errors when using strict evaluation annotations in function arguments."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

Bang pattern errors occur when the BangPatterns extension is not enabled or when bang patterns are used incorrectly.

## Common Causes

- BangPatterns extension not enabled
- Bang pattern on type that cannot be evaluated
- Incorrect placement of bang pattern
- Bang pattern with lazy context

## How to Fix

### 1. Enable BangPatterns extension

```haskell
{-# LANGUAGE BangPatterns #-}

-- WRONG: No extension
-- f !x = x + 1

-- CORRECT
f :: Int -> Int
f !x = x + 1
```

### 2. Use bang patterns in accumulators

```haskell
{-# LANGUAGE BangPatterns #-}

sumList :: [Int] -> Int
sumList = go 0
  where
    go !acc [] = acc
    go !acc (x:xs) = go (acc + x) xs
```

## Examples

```haskell
{-# LANGUAGE BangPatterns #-}

factorial :: Integer -> Integer
factorial n = go 1 n
  where
    go !acc 0 = acc
    go !acc n = go (acc * n) (n - 1)

main :: IO ()
main = print (factorial 20)
```

## Related Errors

- [Compile error](/languages/haskell/haskell-ghc-error)
- [Type error](/languages/haskell/haskell-type-error)
- [Pattern match error](/languages/haskell/haskell-pattern-match)
