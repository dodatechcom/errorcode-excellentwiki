---
title: "[Solution] Haskell QuantifiedConstraints Error"
description: "Fix Haskell QuantifiedConstraints errors when using universal quantification in type class constraints."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

QuantifiedConstraints errors occur when the extension is not enabled or when quantified constraints are incorrectly formed.

## Common Causes

- QuantifiedConstraints extension not enabled
- Quantified constraint syntax incorrect
- Missing context for quantified constraint
- Circular quantified constraint

## How to Fix

### 1. Enable QuantifiedConstraints

```haskell
{-# LANGUAGE QuantifiedConstraints #-}

class (forall a. Eq a => Eq (f a)) => Eq1 f where
```

### 2. Provide instance

```haskell
{-# LANGUAGE QuantifiedConstraints #-}

class (forall a. Show a => Show (f a)) => Show1 f where
  show1 :: Show a => f a -> String
```

## Examples

```haskell
{-# LANGUAGE QuantifiedConstraints #-}

class (forall a. Eq a => Eq (f a)) => Eq1 f where
  eq1 :: Eq a => f a -> f a -> Bool

data Wrapper a = Wrapper a

instance Eq1 Wrapper where
  eq1 (Wrapper a) (Wrapper b) = a == b

main :: IO ()
main = print "QuantifiedConstraints demo"
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Type class error](/languages/haskell/haskell-type-class-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
