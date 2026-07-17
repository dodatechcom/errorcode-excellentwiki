---
title: "[Solution] Haskell Non-Exhaustive Patterns Warning"
description: "Fix Haskell non-exhaustive patterns warnings. Cover all cases in pattern matching to avoid runtime failures."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["warning"]
weight: 5
---

## What This Error Means

A non-exhaustive patterns warning indicates that a function doesn't handle all possible inputs. At runtime, unhandled cases throw a pattern match failure exception.

## Common Causes

- Function missing cases for constructors
- Incomplete pattern matching on custom types
- Missing guards for boundary values
- Recursive functions without base case patterns

## How to Fix

```haskell
-- WARNING: Non-exhaustive patterns for factorial
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)
-- Warning: factorial (-1) crashes

-- CORRECT: Add guard for negative numbers
factorial :: Integer -> Integer
factorial 0 = 1
factorial n | n > 0     = n * factorial (n - 1)
            | otherwise = error "factorial: negative input"
```

```haskell
-- WARNING: Missing case in pattern
safeDivide :: Double -> Double -> Maybe Double
safeDivide a b = Just (a / b)
-- Warning: divide by zero not handled

-- CORRECT: Handle explicitly
safeDivide :: Double -> Double -> Maybe Double
safeDivide _ 0 = Nothing
safeDivide a b = Just (a / b)
```

```haskell
-- WARNING: Custom type incomplete pattern
data Shape = Circle Double | Square Double | Rectangle Double Double

area :: Shape -> Double
area (Circle r) = pi * r * r
area (Square s) = s * s
-- Warning: Rectangle case missing

-- CORRECT: Cover all constructors
area :: Shape -> Double
area (Circle r)       = pi * r * r
area (Square s)       = s * s
area (Rectangle w h)  = w * h
```

## Examples

```haskell
-- Example 1: Use -Wall to catch all warnings
-- ghc -Wall MyModule.hs

-- Example 2: Exhaustive check with custom type
data Status = Active | Inactive | Pending

describe :: Status -> String
describe Active   = "Currently active"
describe Inactive = "Not active"
describe Pending  = "Awaiting approval"
-- No warning: all cases covered

-- Example 3: Safe head with explicit empty case
safeHead :: [a] -> Maybe a
safeHead []    = Nothing
safeHead (x:_) = Just x
```

## Related Errors

- [haskell-pattern-match]({{< relref "/languages/haskell/haskell-pattern-match" >}}) — pattern match failure
- [haskell-type-error]({{< relref "/languages/haskell/haskell-type-error" >}}) — type error
- [non-exhaustive]({{< relref "/languages/haskell/non-exhaustive" >}}) — non-exhaustive patterns
