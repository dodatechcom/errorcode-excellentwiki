---
title: "[Solution] Haskell Pattern Match Failure"
description: "Fix Haskell pattern match failure when a function encounters unhandled cases. Make patterns exhaustive with proper cases."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A pattern match failure occurs when a Haskell function encounters a value that none of its pattern matching cases handle. At runtime, Haskell throws an `IrrefutablePatternFailed` exception.

## Common Causes

- Incomplete pattern on lists (missing empty list case)
- Missing Maybe/Either cases
- Guards that reject all values
- Case expression without catch-all

## How to Fix

```haskell
-- WRONG: Missing empty list case
headSafe :: [a] -> Maybe a
headSafe (x:xs) = Just x
-- Missing: headSafe [] = Nothing

-- CORRECT: Handle all cases
headSafe :: [a] -> Maybe a
headSafe (x:xs) = Just x
headSafe []      = Nothing
```

```haskell
-- WRONG: Incomplete Maybe handling
fromMaybe :: a -> Maybe a -> a
fromMaybe def (Just x)  = x
-- Missing: fromMaybe def Nothing = def

-- CORRECT: Handle both cases
fromMaybe :: a -> Maybe a -> a
fromMaybe def (Just x)  = x
fromMaybe def Nothing   = def
```

```haskell
-- WRONG: Guards without catch-all
classify n
  | n > 0     = "positive"
  | n < 0     = "negative"
-- Missing n == 0 case

-- CORRECT: Cover all cases with otherwise
classify n
  | n > 0     = "positive"
  | n < 0     = "negative"
  | otherwise = "zero"
```

## Examples

```haskell
-- Example 1: Pattern matching on Either
processResult :: Either String Int -> String
processResult (Right n) = "Got number: " ++ show n
processResult (Left err) = "Error: " ++ err

-- Example 2: Pattern matching on tuples
describe :: (Int, Int) -> String
describe (0, 0) = "origin"
describe (x, 0) = "on x-axis"
describe (0, y) = "on y-axis"
describe (x, y) = "at (" ++ show x ++ "," ++ show y ++ ")"

-- Example 3: Using wildcard for catch-all
safeDivide :: Double -> Double -> Maybe Double
safeDivide _ 0 = Nothing
safeDivide a b = Just (a / b)
```

## Related Errors

- [non-exhaustive]({{< relref "/languages/haskell/non-exhaustive" >}}) — non-exhaustive patterns
- [haskell-type-error]({{< relref "/languages/haskell/haskell-type-error" >}}) — type error
- [haskell-not-in-scope]({{< relref "/languages/haskell/haskell-not-in-scope" >}}) — not in scope
