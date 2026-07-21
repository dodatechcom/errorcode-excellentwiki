---
title: "[Solution] Haskell MultiWayIf Error"
description: "Fix Haskell MultiWayIf errors when using if-then-else chains with multiple conditions."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

MultiWayIf errors occur when the MultiWayIf extension is not enabled or when guard conditions are incorrectly formatted.

## Common Causes

- MultiWayIf extension not enabled
- Missing vertical bar in guard syntax
- Conditions not returning Bool
- Missing else branch

## How to Fix

### 1. Enable MultiWayIf

```haskell
{-# LANGUAGE MultiWayIf #-}

classify :: Int -> String
classify x = if
  | x < 0    -> "negative"
  | x == 0   -> "zero"
  | x > 0    -> "positive"
  | otherwise -> "impossible"
```

### 2. Ensure all branches return same type

```haskell
{-# LANGUAGE MultiWayIf #-}

grade :: Int -> String
grade score = if
  | score >= 90 -> "A"
  | score >= 80 -> "B"
  | score >= 70 -> "C"
  | otherwise   -> "F"
```

## Examples

```haskell
{-# LANGUAGE MultiWayIf #-}

describe :: Int -> String
describe n = if
  | n < 0     -> "negative"
  | n == 0    -> "zero"
  | even n    -> "positive even"
  | otherwise -> "positive odd"

main :: IO ()
main = print (describe 42)
```

## Related Errors

- [Pattern match error](/languages/haskell/haskell-pattern-match)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Parse error](/languages/haskell/haskell-parse-error)
