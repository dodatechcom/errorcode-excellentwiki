---
title: "[Solution] Haskell GADT — Generalized Algebraic Data Types"
description: "Fix GADT extension errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1011
---

GADTs (Generalized Algebraic Data Types) let you specify the exact return type of each data constructor, enabling type-safe embedded DSLs. Errors arise when pattern matching does not bring the right type equalities into scope, or when GADT syntax conflicts with standard ADT syntax.

## Common Causes

- Pattern matching on a GADT constructor does not refine the type properly
- Missing `GADTs` or `GADTSyntax` extension
- Using `deriving` clauses that are incompatible with GADTs
- Forgetting that `MonoLocalBinds` is implied by `GADTs`

## How to Fix

### 1. Enable the required extensions

```haskell
{-# LANGUAGE GADTs #-}
-- GADTs implies MonoLocalBinds, TypeFamilies, KindSignatures
```

### 2. Write GADT declarations with explicit types

```haskell
data Expr a where
  LitInt  :: Int -> Expr Int
  LitBool :: Bool -> Expr Bool
  Add     :: Expr Int -> Expr Int -> Expr Int
  If      :: Expr Bool -> Expr a -> Expr a -> Expr a
```

### 3. Pattern match to bring type equalities into scope

```haskell
eval :: Expr a -> a
eval (LitInt n)    = n
eval (LitBool b)   = b
eval (Add x y)     = eval x + eval y
eval (If c t e)
  | eval c        = eval t
  | otherwise     = eval e
```

### 4. Do not derive Eq/Show without appropriate constraints

```haskell
data Expr a where
  LitInt :: Int -> Expr Int

-- WRONG: cannot derive Show for Expr a because a varies
-- deriving Show

-- CORRECT: define manually or constrain
instance Show (Expr a) where
  show (LitInt n) = show n
```

### 5. Use kind signatures for clarity

```haskell
{-# LANGUAGE GADTs #-}
{-# LANGUAGE KindSignatures #-}

data Expr :: * -> * where
  LitInt :: Int -> Expr Int
  LitBool :: Bool -> Expr Bool
```

## Examples

A type-safe expression evaluator:

```haskell
{-# LANGUAGE GADTs #-}

data Expr a where
  Val   :: Int -> Expr Int
  Plus  :: Expr Int -> Expr Int -> Expr Int
  IsZero :: Expr Int -> Expr Bool
  If    :: Expr Bool -> Expr a -> Expr a -> Expr a

eval :: Expr a -> a
eval (Val n)       = n
eval (Plus x y)    = eval x + eval y
eval (IsZero x)    = eval x == 0
eval (If c t e)    = if eval c then eval t else eval e
```

## Related Errors

- [Haskell TypeFamilies Error](../haskell-type-families)
- [Haskell DataKinds Error](../haskell-data-kinds)
- [Haskell ExistentialQuantification](../haskell-existential)
