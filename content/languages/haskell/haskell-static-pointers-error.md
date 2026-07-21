---
title: "[Solution] Haskell StaticPointers Error"
description: "Fix Haskell StaticPointers errors when using distributed computing static references."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

StaticPointers errors occur when the StaticPointers extension is not enabled or when static references point to non-static expressions.

## Common Causes

- StaticPointers extension not enabled
- Static reference to non-top-level binding
- Static reference to value with dynamic type
- Missing Cloud Haskell or distributed package

## How to Fix

### 1. Enable StaticPointers

```haskell
{-# LANGUAGE StaticPointers #-}

-- WRONG: No extension
-- f = static (+ 1)

-- CORRECT
f = static (+ 1)
```

### 2. Only reference top-level bindings

```haskell
{-# LANGUAGE StaticPointers #-}

myFunc :: Int -> Int
myFunc x = x + 1

ref = static myFunc  -- OK: top-level
```

## Examples

```haskell
{-# LANGUAGE StaticPointers #-}

staticAdd :: Static (Int -> Int -> Int)
staticAdd = static (+)

main :: IO ()
main = print "Static pointers demo"
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Not in scope](/languages/haskell/haskell-not-in-scope)
- [Compile error](/languages/haskell/haskell-ghc-error)
