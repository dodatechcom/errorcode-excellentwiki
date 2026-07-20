---
title: "[Solution] Haskell :type — Type Inquery in GHCi"
description: "Fix :type command errors in GHCi. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1041
---

The `:type` (or `:t`) command in GHCi shows the type of an expression. Errors involve ambiguous types, missing typeclass instances, or expressions that GHC cannot type-check at all.

## Common Causes

- The expression has an ambiguous type (e.g., `read "42"` without annotation)
- The expression does not type-check so its type cannot be shown
- Forgetting that `:type` does not evaluate, it only type-checks
- Using `:type` on an expression that requires extensions not enabled in GHCi

## How to Fix

### 1. Provide type annotations for ambiguous expressions

```haskell
:t read "42"
-- ERROR: Ambiguous type variable

:t (read "42" :: Int)
-- Int
```

### 2. Enable extensions before using :type

```haskell
:set -XOverloadedStrings
:t "hello"  -- now works as IsString s => s
```

### 3. Use :type with explicit type applications

```haskell
:set -XTypeApplications
:t read @Int
-- String -> Int
```

### 4. Check types of constructors and functions

```haskell
:t Nothing    -- Maybe a
:t Just       -- a -> Maybe a
:t either     -- (a -> c) -> (b -> c) -> Either a b -> c
```

### 5. Use :type on partial applications

```haskell
:t map (+1)      -- Num b => [b] -> [b]
:t filter (> 0)  -- (Num a, Ord a) => [a] -> [a]
```

## Examples

Common GHCi type queries:

```haskell
:t (+)          -- Num a => a -> a -> a
:t (.)          -- (b -> c) -> (a -> b) -> a -> c
:t id           -- a -> a
:t const        -- a -> b -> a
:t flip         -- (a -> b -> c) -> b -> a -> c

-- With extensions
:set -XScopedTypeVariables
:t (id @Int)    -- Int -> Int
```

## Related Errors

- [Haskell :info Error](../haskell-colon-info)
- [Haskell :kind Error](../haskell-colon-kind)
- [Haskell Ambiguous Type Variable](../haskell-ambiguous-type-var)
