---
title: "[Solution] Haskell Ambiguous Type Variable"
description: "Fix Haskell ambiguous type variable errors. Add type annotations and constrain polymorphic functions."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An ambiguous type variable error occurs when the compiler cannot determine a unique type for a polymorphic variable. The type is not sufficiently constrained by the context.

## Common Causes

- Polymorphic function used without context
- Missing type annotation on polymorphic values
- Type class constraint insufficient to determine type
- Read/show functions without type context

## How to Fix

```haskell
-- WRONG: Ambiguous type
result = read "42"  -- What type should this be?

-- CORRECT: Add type annotation
result = read "42" :: Int
```

```haskell
-- WRONG: Polymorphic function with no context
x = id  -- Type: a -> a, but what is a?

-- CORRECT: Constrain or annotate
x :: Int -> Int
x = id
-- Or use in context that determines type
main = print (id 42)
```

```haskell
-- WRONG: Ambiguous show
main = print (show x)  -- What type is x?

-- CORRECT: Be specific
main = print (show (42 :: Int))
```

## Examples

```haskell
-- Example 1: Ambiguous default
-- default () could be ambiguous
-- Fix: specify numeric type
x :: Int
x = 42

-- Example 2: Type class ambiguity
-- class Show a where show :: a -> String
-- show could work on many types

process :: (Show a) => a -> String
process x = "Value: " ++ show x

-- Example 3: With OverloadedStrings
{-# LANGUAGE OverloadedStrings #-}
-- Strings become polymorphic, may need annotation
x :: String
x = "hello"
```

## Related Errors

- [haskell-type-error]({{< relref "/languages/haskell/haskell-type-error" >}}) — type mismatch
- [haskell-infinite-type]({{< relref "/languages/haskell/haskell-infinite-type" >}}) — infinite type
- [haskell-not-in-scope]({{< relref "/languages/haskell/haskell-not-in-scope" >}}) — not in scope
