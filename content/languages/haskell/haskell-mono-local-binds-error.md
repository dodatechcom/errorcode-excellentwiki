---
title: "[Solution] Haskell MonoLocalBinds Error"
description: "Fix Haskell MonoLocalBinds errors when local bindings escape their scope due to generalization."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

MonoLocalBinds errors occur when local bindings are inadvertently generalized, causing type variables to escape their scope.

## Common Causes

- Let or where bindings inferred to be polymorphic
- MonoLocalBinds extension interfering with type inference
- Missing type signature on local binding
- Polymorphic local used across different types

## How to Fix

### 1. Add explicit type signatures

```haskell
-- WRONG: Inferred type too general
let f x = x + 1
in (f 1, f "hello")  -- error

-- CORRECT: Add signature
let f :: Int -> Int
    f x = x + 1
in (f 1, f (2::Int))
```

### 2. Use MonoLocalBinds appropriately

```haskell
{-# LANGUAGE MonoLocalBinds #-}

-- Prevents generalization of local bindings
```

## Examples

```haskell
{-# LANGUAGE MonoLocalBinds #-}

process :: Int -> String
process n =
  let f x = x * 2
  in show (f n)

main :: IO ()
main = print (process 21)
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Not in scope](/languages/haskell/haskell-not-in-scope)
- [Compile error](/languages/haskell/haskell-ghc-error)
