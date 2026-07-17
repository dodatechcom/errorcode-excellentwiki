---
title: "Infinite Type in Haskell"
description: "Haskell raises infinite type errors when type inference encounters recursive types without base case"
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An infinite type error occurs when Haskell's type inference algorithm tries to unify types and ends up with an infinitely recursive type. This means the type would need to contain itself.

## Common Causes

- Self-referential type definitions without recursion limit
- Incorrect type annotation causing infinite unification
- Missing base case in recursive type
- Polymorphic recursion without type signature

## How to Fix

Add explicit type signatures:

```haskell
-- WRONG: infinite type
-- let f x = f x

-- Correct: explicit type
f :: Int -> a
f x = f x  -- Still infinite loop, but type-checks with explicit annotation
```

Define recursive types properly:

```haskell
-- Correct: defined recursively with base case
data List a = Nil | Cons a (List a)
```

Fix type class instances:

```haskell
-- WRONG: causes infinite type
-- instance Show (a -> b) where

-- Correct: only for specific types
instance Show a => Show (Maybe a) where
  show (Just x) = "Just " ++ show x
  show Nothing = "Nothing"
```

## Examples

```haskell
f x = f (f x)
-- Error: Occurs check: Infinite type: a ~ a -> a
```

## Related Errors

- [Type error]({{< relref "/languages/haskell/type-error" >}})
- [Ambiguous type]({{< relref "/languages/haskell/ambiguous-type" >}})
