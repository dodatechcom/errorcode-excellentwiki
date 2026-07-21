---
title: "[Solution] Haskell UnboxedTuples Error"
description: "Fix Haskell UnboxedTuples errors when using unboxed tuples for efficient pair representations."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

UnboxedTuples errors occur when the UnboxedTuples extension is not enabled or when unboxed tuples are incorrectly constructed or pattern matched.

## Common Causes

- UnboxedTuples extension not enabled
- Unboxed tuple returned from non-IO function
- Pattern match on unboxed tuple incorrect
- Unboxed tuple used in foreign import

## How to Fix

### 1. Enable UnboxedTuples

```haskell
{-# LANGUAGE UnboxedTuples #-}

-- WRONG: No extension
-- f :: (# Int, Int #)

-- CORRECT
f :: (# Int, Int #)
f = (# 1, 2 #)
```

### 2. Use correct syntax

```haskell
{-# LANGUAGE UnboxedTuples #-}

swap :: (# a, b #) -> (# b, a #)
swap (# a, b #) = (# b, a #)
```

## Examples

```haskell
{-# LANGUAGE UnboxedTuples #-}

pair :: (# Int, String #)
pair = (# 42, "hello" :: String #)

first :: (# a, b #) -> a
first (# a, _ #) = a

main :: IO ()
main = print (first pair)
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Kind error](/languages/haskell/haskell-colon-kind)
