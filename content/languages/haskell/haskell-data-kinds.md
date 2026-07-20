---
title: "[Solution] Haskell DataKinds — Type-Level Data Constructors"
description: "Fix DataKinds extension errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1012
---

`DataKinds` promotes data constructors into type constructors, allowing you to use types at the type level. This is essential for type-level programming with natural numbers, vectors of known length, and similar constructs.

## Common Causes

- Using a promoted constructor in a type without enabling `DataKinds`
- Kind mismatches between promoted and unpromoted constructors
- Forgetting that promoted constructors are distinct from value constructors
- Mixing up `Symbol` (type-level string) and `Char` kinds

## How to Fix

### 1. Enable DataKinds

```haskell
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE KindSignatures #-}
{-# LANGUAGE PolyKinds #-}
```

### 2. Use promoted constructors in type signatures

```haskell
data Nat = Zero | Succ Nat

data Vec :: Nat -> * -> * where
  Nil  :: Vec Zero a
  Cons :: a -> Vec n a -> Vec (Succ n) a
```

### 3. Use the tick syntax for promoted constructors (Haskell 2010 compatibility)

```haskell
-- In older GHC versions you may need the tick
type MyList = '[ 'True, 'False ]
```

### 4. Match kinds carefully in type families

```haskell
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE TypeFamilies #-}

type family Length (xs :: [a]) :: Nat where
  Length '[]       = 'Zero
  Length (x ': xs) = 'Succ (Length xs)
```

### 5. Use GADTSyntax alongside for cleaner definitions

```haskell
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE GADTSyntax #-}

data Bool = True | False

-- Promoted: 'True and 'False have kind Bool
-- The promoted kind is also called Bool
```

## Examples

A length-indexed vector using DataKinds:

```haskell
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE GADTs #-}

data Nat = Z | S Nat

data Vec :: Nat -> * -> * where
  VNil  :: Vec 'Z a
  VCons :: a -> Vec n a -> Vec ('S n) a

head' :: Vec ('S n) a -> a
head' (VCons x _) = x
```

## Related Errors

- [Haskell GADT Error](../haskell-gadt)
- [Haskell TypeFamilies Error](../haskell-type-families)
- [Haskell Kind Error](../haskell-kind-error)
