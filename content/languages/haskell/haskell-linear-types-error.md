---
title: "[Solution] Haskell LinearTypes Error"
description: "Fix Haskell LinearTypes errors when using linear type annotations for resource safety."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

LinearTypes errors occur when the LinearTypes extension is not enabled or when linear type annotations conflict with usage.

## Common Causes

- LinearTypes extension not enabled
- Linear variable used more than once
- Linear variable not used at all
- Function signature does not match linear usage

## How to Fix

### 1. Enable LinearTypes

```haskell
{-# LANGUAGE LinearTypes #-}

-- WRONG: No extension
-- f :: a %1 -> a

-- CORRECT
f :: a %1 -> a
f x = x
```

### 2. Ensure linear usage

```haskell
{-# LANGUAGE LinearTypes #-}

consume :: a %1 -> ()
consume _ = ()
```

## Examples

```haskell
{-# LANGUAGE LinearTypes #-}

identity :: a %1 -> a
identity x = x

doubleUse :: a %1 -> (a, a)
doubleUse _ = error "Cannot duplicate linear value"

main :: IO ()
main = print "Linear types demo"
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Type class error](/languages/haskell/haskell-type-class-error)
