---
title: "Type Error in Haskell"
description: "Haskell compiler raises type errors when expressions don't match expected types"
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["type", "inference", "mismatch", "typeerror", "compilation"]
weight: 5
---

## What This Error Means

Haskell type errors occur at compile time when the type checker finds a mismatch between expected and inferred types. Haskell's strong static type system catches these before runtime.

## Common Causes

- Type mismatch in function application
- Missing type signature causing ambiguous types
- Incorrect use of type class
- Polymorphic function used with incompatible types

## How to Fix

Add explicit type signatures:

```haskell
-- Without signature, type inference might be wrong
addNumbers :: Int -> Int -> Int
addNumbers x y = x + y
```

Check type class constraints:

```haskell
-- WRONG: Num constraint missing
-- show (1 + 2)  -- Won't work without Show constraint

-- Correct
show (1 + 2 :: Int)  -- "3"
```

Use type annotations:

```haskell
x = 42 :: Int
y = 3.14 :: Double
```

Fix common type mismatches:

```haskell
-- WRONG: mixing types
-- x = 1 + "hello"

-- Correct: same types
x = 1 + 2 :: Int
```

## Examples

```haskell
add :: Int -> Int -> Int
add x y = x + y

result = add 1 "hello"
-- Type error: Expected Int, got String
```

## Related Errors

- [Ambiguous type variable]({{< relref "/languages/haskell/ambiguous-type" >}})
- [Not in scope]({{< relref "/languages/haskell/not-in-scope" >}})
