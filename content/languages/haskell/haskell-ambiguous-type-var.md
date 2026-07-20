---
title: "[Solution] Haskell Ambiguous Type Variable — Cannot Deduce Concrete Type"
description: "Fix ambiguous type variable errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1005
---

An ambiguous type variable error means GHC knows a variable must satisfy some constraint but cannot determine which concrete type to use. This most often happens with polymorphic functions like `read` or `default` values.

## Common Causes

- Using `read` without a type annotation (GHC does not know what type to parse into)
- Calling `mempty` or `mconcat` on a type that has multiple `Monoid` instances in scope
- Numeric literals that could be `Int`, `Integer`, `Double`, etc.
- Class methods that return a type parameter with no way to infer it

## How to Fix

### 1. Add a type annotation

```haskell
-- WRONG
x = read "42"

-- CORRECT
x = read "42" :: Int
```

### 2. Use ScopedTypeVariables with explicit forall

```haskell
{-# LANGUAGE ScopedTypeVariables #-}

process :: forall a. (Show a, Read a) => a -> String
process x = show (read (show x) :: a)
```

### 3. Provide the type at the call site with TypeApplications

```haskell
{-# LANGUAGE TypeApplications #-}

x = read @Int "42"
```

### 4. Use a more specific type in the signature

```haskell
-- WRONG: too polymorphic
getValue = mempty

-- CORRECT: pinned type
getValue :: [Int]
getValue = mempty
```

### 5. Disable MonomorphismRestriction for inferred bindings

```haskell
{-# LANGUAGE NoMonomorphismRestriction #-}
-- Now GHC will infer the most general type for simple bindings
```

## Examples

The classic ambiguous `read`:

```haskell
main = print (read "hello")
-- Ambiguous type variable ‘a0’ arising from a use of ‘read’

-- Fix
main = print (read "hello" :: String)
```

## Related Errors

- [Haskell Type Mismatch](../haskell-type-error)
- [Haskell RankNTypes Error](../haskell-rankntypes)
- [Haskell Type Application Error](../haskell-type-application)
