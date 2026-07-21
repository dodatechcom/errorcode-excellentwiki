---
title: "[Solution] Haskell UnboxedSums Error"
description: "Fix Haskell UnboxedSums errors when using unboxed sum types for memory-efficient alternatives."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

UnboxedSums errors occur when the UnboxedSums extension is not enabled or when unboxed sum types are used incorrectly.

## Common Causes

- UnboxedSums extension not enabled
- Unboxed sum used with non-unboxed types
- Pattern match on unboxed sum incorrect
- Missing kind annotation for unboxed sum

## How to Fix

### 1. Enable UnboxedSums

```haskell
{-# LANGUAGE UnboxedSums #-}
{-# LANGUAGE UnboxedTuples #-}

-- WRONG: No extension
-- type MaybeUnbox a = (# a | () #)

-- CORRECT
type MaybeUnbox a = (# a | () #)
```

### 2. Use correct pattern syntax

```haskell
{-# LANGUAGE UnboxedSums #-}

fromMaybeUnbox :: MaybeUnbox Int -> Int
fromMaybeUnbox (# x | #) = x
fromMaybeUnbox (# | _ #) = 0
```

## Examples

```haskell
{-# LANGUAGE UnboxedSums #-}
{-# LANGUAGE UnboxedTuples #-}

type MaybeInt = (# Int | () #)

just :: Int -> MaybeInt
just x = (# x | #)

nothing :: MaybeInt
nothing = (# | () #)

fromMaybeInt :: MaybeInt -> Int
fromMaybeInt (# x | #) = x
fromMaybeInt (# | _ #) = 0

main :: IO ()
main = print (fromMaybeInt (just 42))
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Kind error](/languages/haskell/haskell-colon-kind)
