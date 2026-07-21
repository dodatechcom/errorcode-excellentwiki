---
title: "[Solution] Haskell TupleSections Error"
description: "Fix Haskell TupleSections errors when using section syntax for partial tuple application."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

TupleSections errors occur when the extension is not enabled or when partial tuple application syntax is incorrectly used.

## Common Causes

- TupleSections extension not enabled
- Wrong number of underscores in section
- Using tuple section where full tuple expected
- Type inference failure with tuple sections

## How to Fix

### 1. Enable TupleSections

```haskell
{-# LANGUAGE TupleSections #-}

-- Partial application of tuple
addPair = (+) *** (+)
-- Or with tuple sections
addPair = (,) <$> (+ 1) <*> (* 2)
```

### 2. Use correct syntax

```haskell
{-# LANGUAGE TupleSections #-}

-- WRONG: Missing parens
-- (, x)  -- syntax error

-- CORRECT
(, 42)  -- produces \y -> (y, 42)
```

## Examples

```haskell
{-# LANGUAGE TupleSections #-}

applyTuple :: Int -> (Int, Int)
applyTuple = (, 10)

pairs :: [Int] -> [(Int, String)]
pairs = map (\x -> (x, show x))

main :: IO ()
main = print (applyTuple 5, pairs [1,2,3])
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Syntax error](/languages/haskell/haskell-parse-error)
