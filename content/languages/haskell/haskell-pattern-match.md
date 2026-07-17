---
title: "Pattern Match Failure in Haskell"
description: "Haskell raises pattern match failure when a function encounters a value that none of its cases handle"
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A pattern match failure occurs when a function encounters a value that none of its pattern matching cases handle. Haskell throws an `IrrefutablePatternFailed` exception at runtime.

## Common Causes

- Incomplete pattern on lists (missing empty list case)
- Missing Maybe/Either cases
- Guards that reject all values
- Case expression without catch-all

## How to Fix

Add missing cases:

```haskell
headSafe :: [a] -> Maybe a
headSafe (x:xs) = Just x
headSafe []      = Nothing
```

Handle Maybe explicitly:

```haskell
fromMaybe :: a -> Maybe a -> a
fromMaybe def (Just x)  = x
fromMaybe def Nothing   = def
```

Use wildcard for catch-all:

```haskell
classify n
  | n > 0     = "positive"
  | n < 0     = "negative"
  | otherwise = "zero"  -- Important: covers n == 0
```

## Examples

```haskell
unwrap (Just x) = x
-- Calling unwrap Nothing crashes: Pattern match failure
```

## Related Errors

- [Non-exhaustive patterns]({{< relref "/languages/haskell/non-exhaustive" >}})
- [Infinite type]({{< relref "/languages/haskell/infinite-loop" >}})
