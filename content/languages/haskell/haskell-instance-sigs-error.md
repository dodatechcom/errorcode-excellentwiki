---
title: "[Solution] Haskell InstanceSigs Error"
description: "Fix Haskell InstanceSigs errors when providing type signatures for type class method implementations."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

InstanceSigs errors occur when the extension is not enabled or when instance method signatures do not match the class definition.

## Common Causes

- InstanceSigs extension not enabled
- Instance signature does not match class method type
- Missing or extra type parameters in instance signature
- Context mismatch between class and instance

## How to Fix

### 1. Enable InstanceSigs

```haskell
{-# LANGUAGE InstanceSigs #-}

class MyClass a where
  myMethod :: a -> String

instance MyClass Int where
  myMethod :: Int -> String
  myMethod = show
```

### 2. Match signature exactly

```haskell
{-# LANGUAGE InstanceSigs #-}

class Container c where
  empty :: c a
  insert :: a -> c a -> c a

instance Container [] where
  empty :: [a]
  empty = []
  insert :: a -> [a] -> [a]
  insert x xs = x : xs
```

## Examples

```haskell
{-# LANGUAGE InstanceSigs #-}

class Describable a where
  describe :: a -> String

instance Describable Int where
  describe :: Int -> String
  describe n = "Number " ++ show n

main :: IO ()
main = print (describe (42 :: Int))
```

## Related Errors

- [Type class error](/languages/haskell/haskell-type-class-error)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
