---
title: "Ambiguous Type Variable in Haskell"
description: "Haskell raises ambiguous type variable errors when the compiler cannot determine a unique type"
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An ambiguous type variable error occurs when Haskell's type checker cannot determine a unique type for an expression. The type variable is not resolved by the context.

## Common Causes

- Overloaded literals without type annotation
- Polymorphic function with no constraining context
- Missing type signature for polymorphic values
- Multiple type class instances matching

## How to Fix

Add type annotations:

```haskell
-- WRONG: ambiguous
-- x = 42

-- Correct: annotated
x = 42 :: Int
```

Constrain polymorphic functions:

```haskell
-- WRONG: ambiguous
-- f x = show x

-- Correct: Show constraint
f :: Show a => a -> String
f x = show x
```

Use defaulting rules:

```haskell
-- Default rules apply to numeric literals
x = 42  -- Defaults to Integer or Int
```

Specify target type:

```haskell
result = read "42" :: Int
```

## Examples

```haskell
main = print (read "hello")
-- Error: Ambiguous type variable 'a' arising from a use of 'read'
```

## Related Errors

- [Type error]({{< relref "/languages/haskell/type-error" >}})
- [Not in scope]({{< relref "/languages/haskell/not-in-scope" >}})
