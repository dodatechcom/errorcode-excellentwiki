---
title: "[Solution] Haskell ScopedTypeVariables — Lexically Scoped Type Variables"
description: "Fix ScopedTypeVariables errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1009
---

`ScopedTypeVariables` lets you refer to a type variable from a forall in a type signature within the body of the function. Without it, type variables in signatures are not in scope in the implementation, which can lead to confusing mismatched-type errors.

## Common Causes

- Trying to use a type variable from the signature in a `read` or `asTypeOf` call
- Pattern matching on types that GHC infers differently from what you wrote
- Forgetting to explicitly `forall` the variables you want to scope

## How to Fix

### 1. Enable the extension

```haskell
{-# LANGUAGE ScopedTypeVariables #-}
```

### 2. Add an explicit `forall` to bring variables into scope

```haskell
process :: forall a. (Show a, Read a) => String -> a
process s = read s :: a
```

### 3. Use `asTypeOf` with scoped variables

```haskell
import Data.Typeable (Typeable)

safeRead :: forall a. (Read a, Typeable a) => String -> Maybe a
safeRead s = case reads s of
  [(x, "")] -> Just (x `asTypeOf` (undefined :: a))
  _          -> Nothing
```

### 4. Use `Proxy` for type-level communication

```haskell
{-# LANGUAGE ScopedTypeVariables #-}
import Data.Proxy (Proxy(..))

process :: forall a. (Typeable a, Show a) => Proxy a -> String -> String
process (_ :: Proxy a) val = show (read val :: a)
```

### 5. Combine with AllowAmbiguousTypes for advanced cases

```haskell
{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE AllowAmbiguousTypes #-}
{-# LANGUAGE TypeApplications #-}

dispatch :: forall a. (Show a, Typeable a) => String -> String
dispatch input = show (read input :: a)
```

## Examples

ScopedTypeVariables in a recursive function:

```haskell
{-# LANGUAGE ScopedTypeVariables #-}

count :: forall a. (Eq a) => a -> [a] -> Int
count target = go
  where
    go :: [a] -> Int
    go [] = 0
    go (x:xs)
      | x == target = 1 + go xs
      | otherwise   = go xs
```

## Related Errors

- [Haskell Ambiguous Type Variable](../haskell-ambiguous-type-var)
- [Haskell Type Application Error](../haskell-type-application)
- [Haskell RankNTypes Error](../haskell-rankntypes)
