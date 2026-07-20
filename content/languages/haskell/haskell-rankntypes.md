---
title: "[Solution] Haskell RankNTypes — Higher-Rank Polymorphism"
description: "Fix RankNTypes errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1010
---

Rank-N types allow type variables to appear on the left of function arrows in arguments, enabling higher-rank polymorphism. Without the `RankNTypes` extension, GHC restricts type variables to rank 1 (they can only appear at the outermost level of arguments).

## Common Causes

- Writing a function that takes a polymorphic function as an argument
- Trying to pass a `forall`-quantified type as a parameter
- Library code that requires `RankNTypes` but the extension is not enabled

## How to Fix

### 1. Enable the extension

```haskell
{-# LANGUAGE RankNTypes #-}
```

### 2. Use the right syntax for rank-2 arguments

```haskell
-- WRONG without RankNTypes: GHC infers rank-1
applyToFive :: (forall a. a -> a) -> Int
applyToFive f = f 5

-- With RankNTypes, this compiles
```

### 3. Use RankNTypes with lenses

```haskell
import Control.Lens

type Lens s t a b = forall f. Functor f => (a -> f b) -> s -> f t
```

### 4. Avoid unnecessary rank-2 types

Sometimes you can restructure to avoid rank-2:

```haskell
-- Instead of passing a polymorphic function, pass a constrained one
applyShow :: (Int -> String) -> Int -> String
applyShow f x = f x
```

### 5. Combine with ExistentialQuantification for existentials

```haskell
{-# LANGUAGE RankNTypes #-}
{-# LANGUAGE ExistentialQuantification #-}

data Showable = forall a. Show a => Showable a
```

## Examples

A practical use of RankNTypes with a continuation-passing style:

```haskell
{-# LANGUAGE RankNTypes #-}

withFile :: forall r. (FilePath -> IO r) -> (Handle -> IO r) -> r
withFile path action = unsafePerformIO $ do
  h <- openFile path ReadMode
  result <- action h
  hClose h
  return result
```

## Related Errors

- [Haskell ScopedTypeVariables](../haskell-scoped-type-vars)
- [Haskell ExistentialQuantification](../haskell-existential)
- [Haskell Lens Error](../haskell-lens-error)
