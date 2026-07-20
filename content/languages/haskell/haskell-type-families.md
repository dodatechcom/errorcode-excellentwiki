---
title: "[Solution] Haskell TypeFamilies — Associated Type Computation"
description: "Fix TypeFamilies extension errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1013
---

Type families allow you to define type-level functions that compute types from other types. Errors usually involve non-exhaustive patterns at the type level or unsatisfiable type equality constraints.

## Common Causes

- A type family equation is missing for some type constructor
- The type family result is ambiguous due to injectivity issues
- Open type families allow overlapping equations that GHC cannot resolve
- Closed type families have overlapping patterns without a fallback

## How to Fix

### 1. Enable TypeFamilies and TypeOperators if needed

```haskell
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE TypeOperators #-}
```

### 2. Make type family equations exhaustive

```haskell
type family F a where
  F Int    = Bool
  F Char   = Int
  F String = Double
  F a      = ()  -- catch-all
```

### 3. Use associated types in typeclasses

```haskell
class Container c where
  type Elem c
  empty :: c
  insert :: Elem c -> c -> c
```

### 4. Check kind consistency

```haskell
-- All equations must produce the same kind
type family Grep a where
  Grep Int    = Bool    -- kind *
  Grep Char   = Int     -- kind *
  Grep String = [Char]  -- kind *
```

### 5. Use type families with GADTs for dependent-like programming

```haskell
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE GADTs #-}

data family Sing a

data instance Sing (a :: Bool) where
  STrue  :: Sing 'True
  SFalse :: Sing 'False
```

## Examples

A simple type-level addition:

```haskell
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE TypeOperators #-}

data Nat = Z | S Nat

type family Add (a :: Nat) (b :: Nat) :: Nat where
  Add 'Z     b = b
  Add ('S a) b = 'S (Add a b)

type Three = 'S ('S ('S 'Z))
type Five  = Add Three ('S ('S 'Z))  -- Five ~ 'S ('S ('S ('S ('S 'Z))))
```

## Related Errors

- [Haskell GADT Error](../haskell-gadt)
- [Haskell DataKinds Error](../haskell-data-kinds)
- [Haskell Kind Error](../haskell-kind-error)
