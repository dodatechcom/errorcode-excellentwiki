---
title: "[Solution] Haskell Empty Case Error"
description: "Fix Haskell EmptyCase errors when using case expressions with no alternatives for empty types."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

Empty case errors occur when case expressions have no alternatives or when EmptyCase extension is not enabled for void types.

## Common Causes

- EmptyCase extension not enabled
- Case expression with no alternatives on non-void type
- Missing pattern match for all constructors
- Using case with uninhabited type

## How to Fix

### 1. Enable EmptyCase extension

```haskell
{-# LANGUAGE EmptyCase #-}

absurd :: Void -> a
absurd x = case x of {}
```

### 2. Add at least one alternative

```haskell
-- WRONG: No alternatives
case value of {}

-- CORRECT: Add patterns
case value of
    Nothing  -> "empty"
    Just x   -> show x
```

## Examples

```haskell
{-# LANGUAGE EmptyCase #-}

data Void

absurd :: Void -> a
absurd v = case v of {}

main :: IO ()
main = print "Empty case demo"
```

## Related Errors

- [Pattern match error](/languages/haskell/haskell-pattern-match)
- [Non-exhaustive pattern](/languages/haskell/haskell-non-exhaustive)
- [Compile error](/languages/haskell/haskell-ghc-error)
