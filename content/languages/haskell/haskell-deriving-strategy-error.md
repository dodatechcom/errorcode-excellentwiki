---
title: "[Solution] Haskell Deriving Strategy Error"
description: "Fix Haskell DerivingStrategy errors when specifying explicit deriving strategies for type class instances."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

Deriving strategy errors occur when the DerivingStrategies extension is used but the specified strategy is incompatible with the type.

## Common Causes

- DerivingStrategies extension not enabled
- Using stock deriving for non-stock type class
- GeneralizedNewtypeDeriving on data types
- Multiple deriving clauses conflicting

## How to Fix

### 1. Enable DerivingStrategies

```haskell
{-# LANGUAGE DerivingStrategies #-}
{-# LANGUAGE GeneralizedNewtypeDeriving #-}

newtype Age = Age Int
  deriving stock (Show, Eq)
  deriving newtype (Num, Ord)
```

### 2. Use appropriate strategy

```haskell
-- WRONG: Newtype deriving on data type
data Foo = Foo Int
  deriving newtype (Show)  -- error!

-- CORRECT: Stock deriving for data types
data Foo = Foo Int
  deriving stock (Show)
```

## Examples

```haskell
{-# LANGUAGE DerivingStrategies #-}
{-# LANGUAGE GeneralizedNewtypeDeriving #-}

newtype Dollars = Dollars Int
  deriving stock (Show, Eq, Ord)
  deriving newtype (Num)

main :: IO ()
main = print (Dollars 100)
```

## Related Errors

- [Deriving error](/languages/haskell/haskell-deriving-error)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
