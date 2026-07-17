---
title: "[Solution] Haskell MonadFail Error in Do-Notation"
description: "Fix Haskell MonadFail errors when pattern matching fails in do-notation. Use proper MonadFail methods or handle failures."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A MonadFail error occurs when a pattern match in do-notation fails and the monad cannot handle the failure. In Haskell 2010+, pattern match failures in do-notation require MonadFail.

## Common Causes

- Irrefutable pattern in do-notation (e.g., Just x from Nothing)
- Using view patterns in do-notation
- Case expressions with incomplete patterns in do-block
- Non-exhaustive pattern in do-notation binding

## How to Fix

```haskell
-- WRONG: Pattern match failure in do-notation
import Control.Monad (guard)

example :: Maybe Int
example = do
  Just x <- return Nothing  -- MonadFail error
  return x

-- CORRECT: Handle the failure case
example :: Maybe Int
example = do
  result <- return (Nothing :: Maybe Int)
  case result of
    Just x  -> return x
    Nothing -> Nothing
```

```haskell
-- WRONG: Guard without alternative
example :: Maybe Int
example = do
  x <- lookup "key" myMap
  guard (x > 10)
  return x

-- CORRECT: Use alternative or handle failure
example :: Maybe Int
example = do
  x <- lookup "key" myMap
  if x > 10 then return x else Nothing
```

```haskell
-- WRONG: Let binding with pattern
example :: IO ()
example = do
  let (x:xs) = []  -- Pattern match failure
  print x

-- CORRECT: Safe pattern
example :: IO ()
example = do
  let list = []
  case list of
    (x:xs) -> print x
    []     -> putStrLn "Empty list"
```

## Examples

```haskell
-- Example 1: MonadFail instance
import Control.Monad.Fail

safeHead :: [a] -> Maybe a
safeHead (x:_) = Just x
safeHead []    = Nothing

example :: Maybe Int
example = do
  x <- safeHead [1, 2, 3]
  return (x + 1)

-- Example 2: Using alternative
import Control.Applicative ((<|>))

lookupOrDefault :: String -> [(String, Int)] -> Maybe Int
lookupOrDefault key xs = lookup key xs <|> Just 0

-- Example 3: Explicit case in do-notation
safeDivide :: Double -> Double -> Maybe Double
safeDivide a b = do
  case b of
    0 -> Nothing
    _ -> return (a / b)
```

## Related Errors

- [haskell-pattern-match]({{< relref "/languages/haskell/haskell-pattern-match" >}}) — pattern match failure
- [haskell-non-exhaustive]({{< relref "/languages/haskell/haskell-non-exhaustive" >}}) — non-exhaustive patterns
- [haskell-type-error]({{< relref "/languages/haskell/haskell-type-error" >}}) — type error
