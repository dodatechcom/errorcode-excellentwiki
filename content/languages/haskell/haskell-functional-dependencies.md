---
title: "[Solution] Haskell FunctionalDependencies — Type-Level Functional Relations"
description: "Fix FunctionalDependencies errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1008
---

Functional dependencies specify that one type parameter uniquely determines another in a multi-parameter typeclass. When GHC cannot satisfy the dependency, it reports an error. This extension is common in libraries like `lens` and `persist`.

## Common Causes

- A functional dependency cannot be satisfied because the determining types are ambiguous
- Missing fundep in the class definition leads to unsolvable constraints
- Two instances conflict with the declared functional dependency
- Forgetting to enable `MultiParamTypeClasses` alongside `FunctionalDependencies`

## How to Fix

### 1. Enable both extensions

```haskell
{-# LANGUAGE MultiParamTypeClasses #-}
{-# LANGUAGE FunctionalDependencies #-}
```

### 2. Check that the fundep can be uniquely determined

```haskell
class Collection c e | c -> e where
  insert :: e -> c -> c
  toList :: c -> [e]

-- The fundep | c -> e means the element type is determined by the collection type
```

### 3. Make sure instances satisfy the fundep

```haskell
instance Collection [Int] Int where
  insert x xs = x : xs
  toList = id
```

### 4. Use UndecidableInstances if GHC cannot verify termination

```haskell
{-# LANGUAGE FunctionalDependencies #-}
{-# LANGUAGE UndecidableInstances #-}

class Convert a b | a -> b where
  convert :: a -> b
```

### 5. Verify no two instances map the same determining types differently

```haskell
-- WRONG: two instances with same c but different e
instance Collection [Int] Int where ...
instance Collection [Int] String where ...

-- CORRECT: unique mapping
instance Collection [Int] Int where ...
instance Collection [String] String where ...
```

## Examples

A practical fundep for a key-value store:

```haskell
{-# LANGUAGE MultiParamTypeClasses #-}
{-# LANGUAGE FunctionalDependencies #-}

class Store s k v | s -> k, s -> v where
  put :: k -> v -> s -> s
  get :: k -> s -> Maybe v

data MapStore k v = MapStore (Map k v)

instance Ord k => Store (MapStore k v) k v where
  put k v (MapStore m) = MapStore (Map.insert k v m)
  get k (MapStore m)   = Map.lookup k m
```

## Related Errors

- [Haskell MultiParamTypeClasses](../haskell-multiparam)
- [Haskell Type Families Error](../haskell-type-families)
- [Haskell UndecidableInstances](../haskell-undecidable)
