---
title: "[Solution] Haskell Type Mismatch — Expected vs Actual Types"
description: "Fix Haskell type mismatches. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1002
---

A type mismatch means GHC inferred a type for an expression that differs from what the context expects. The compiler shows you the expected type and the actual inferred type so you can reconcile them.

## Common Causes

- Passing an argument of the wrong type to a function
- Forgetting to apply a function (returning a function value where a concrete value is expected)
- Using numeric literals without a type annotation when polymorphism is ambiguous
- Returning the wrong type from a branch of an `if` or `case`

## How to Fix

### 1. Read the expected vs actual types carefully

GHC prints both types. Compare them character by character—often only one constructor differs:

```haskell
foo :: Int -> Int
foo x = x + "hello"
-- Expected: Int
-- Actual:   String
```

### 2. Add explicit type annotations

Help GHC narrow down polymorphic types:

```haskell
-- WRONG: ambiguous
read "42" + 1

-- CORRECT
(read "42" :: Int) + 1
```

### 3. Use `:t` in GHCi to inspect types

Load your module in GHCi and query the type of the problematic expression:

```haskell
Prelude> :t map
map :: (a -> b) -> [a] -> [b]
```

### 4. Check function composition and application

A common mistake is forgetting to apply the last argument:

```haskell
-- WRONG: takes two args but only given one
applyToFive f = f 5

result = applyToFive (+)  -- type is Int -> Int, not Int
```

### 5. Make sure branches of `if`/`case` agree

```haskell
-- WRONG: branches return different types
f x = if x > 0 then "positive" else (-1)

-- CORRECT: both branches return the same type
f x = if x > 0 then "positive" else "non-positive"
```

## Examples

A classic mismatch with lists:

```haskell
-- WRONG
head [1, 2, 3] == "1"

-- CORRECT
head [1, 2, 3] == 1
```

## Related Errors

- [Haskell Couldn't Match Type](../haskell-couldnt-match)
- [Haskell Ambiguous Type Variable](../haskell-ambiguous-type-var)
- [Haskell No Instance For](../haskell-no-instance-for)
