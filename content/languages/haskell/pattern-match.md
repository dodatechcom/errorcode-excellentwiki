---
title: "Pattern match failure"
description: "A pattern match failure occurs when a function encounters a value that none of its pattern matching cases handle."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["pattern-match", "non-exhaustive", "runtime", "haskell"]
weight: 5
---

## What This Error Means

A pattern match failure occurs when a function encounters a value that none of its pattern matching cases handle. Haskell throws an `IrrefutablePatternFailed` exception at runtime.

## Common Causes

- Incomplete pattern on lists
- Missing Maybe/Either cases
- Guards that reject all values
- Case expression without catch-all

## How to Fix

```haskell
-- WRONG: Incomplete pattern on lists
headSafe :: [a] -> a
headSafe (x:xs) = x
-- Missing: headSafe [] = error "empty list"

-- CORRECT: Add missing cases
headSafe (x:xs) = x
headSafe []      = error "empty list"
```

```haskell
-- WRONG: Missing Maybe case
fromMaybe :: a -> Maybe a -> a
fromMaybe def (Just x) = x
-- Missing: fromMaybe def Nothing = def

-- CORRECT: Handle all cases
fromMaybe def (Just x)  = x
fromMaybe def Nothing   = def
```

## Examples

```haskell
-- Example 1: Incomplete list pattern
headSafe (x:_) = x
headSafe []    = error "empty"
-- Calling headSafe [] still crashes if not caught

-- Example 2: Missing Maybe case
unwrap (Just x) = x
-- Calling unwrap Nothing crashes

-- Example 3: Guard rejects all
classify n
  | n > 0     = "positive"
  | n < 0     = "negative"
-- classify 0 crashes (no otherwise)
```

## Related Errors

- [Non-exhaustive patterns](/languages/haskell/non-exhaustive)
- [Infinite loop / stack overflow](/languages/haskell/infinite-loop)
