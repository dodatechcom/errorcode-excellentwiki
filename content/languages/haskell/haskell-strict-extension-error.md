---
title: "[Solution] Haskell Strict Extension Error"
description: "Fix Haskell Strict extension errors when applying strict evaluation to all bindings in a module."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

Strict extension errors occur when the Strict extension forces evaluation of all bindings, causing unexpected bottom forcing.

## Common Causes

- Strict extension forces all let/where bindings
- Infinite loops exposed by strict evaluation
- Missing bottom handling in strict code
- Strict extension conflicts with performance

## How to Fix

### 1. Handle bottoms in strict code

```haskell
{-# LANGUAGE Strict #-}

-- WRONG: May force bottom
-- let x = error "oops" in x

-- CORRECT: Guard against bottom
let x = error "oops"
in x `seq` x  -- still errors, but explicit
```

### 2. Use StrictData instead

```haskell
{-# LANGUAGE StrictData #-}

-- Only strict data fields, not all bindings
data Foo = Foo !Int !String
```

## Examples

```haskell
{-# LANGUAGE Strict #-}

data StrictPair = StrictPair !Int !String
  deriving (Show)

main :: IO ()
main = print (StrictPair 42 "hello")
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Bang pattern error](/languages/haskell/haskell-bang-pattern)
