---
title: "[Solution] Haskell StrictData Error"
description: "Fix Haskell StrictData errors when using strict fields in data declarations for bang-pattern behavior."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

StrictData errors occur when the StrictData extension is not enabled or when strict data fields conflict with lazy evaluation.

## Common Causes

- StrictData extension not enabled
- Strict field causes bottom to be forced
- Missing StrictData extension for strict fields
- Strict fields in lazy data type

## How to Fix

### 1. Enable StrictData

```haskell
{-# LANGUAGE StrictData #-}

-- WRONG: No extension
-- data Foo = Foo !Int !String

-- CORRECT
data Foo = Foo !Int !String
```

### 2. Selective strictness

```haskell
{-# LANGUAGE StrictData #-}

data Config = Config
  { host :: !String
  , port :: !Int
  , debug :: !Bool
  }
```

## Examples

```haskell
{-# LANGUAGE StrictData #-}

data Point = Point !Double !Double
  deriving (Show)

distance :: Point -> Point -> Double
distance (Point x1 y1) (Point x2 y2) =
  sqrt ((x2-x1)**2 + (y2-y1)**2)

main :: IO ()
main = print (distance (Point 0 0) (Point 3 4))
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Pattern match error](/languages/haskell/haskell-pattern-match)
