---
title: "[Solution] Haskell OverloadedLabels Error"
description: "Fix Haskell OverloadedLabels errors when using #label syntax for overloaded label resolution."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

OverloadedLabels errors occur when the extension is not enabled or when IsLabel instance is missing for the target type.

## Common Causes

- OverloadedLabels extension not enabled
- Missing IsLabel instance for type
- Label syntax used with incompatible type
- Ambiguous label resolution

## How to Fix

### 1. Enable OverloadedLabels

```haskell
{-# LANGUAGE OverloadedLabels #-}

import GHC.OverloadedLabels (IsLabel(..))

data Foo = Foo

instance IsLabel "hello" Foo where
  fromLabel = Foo
```

### 2. Implement IsLabel instance

```haskell
{-# LANGUAGE OverloadedLabels #-}

data Rec = Rec { name :: String, value :: Int }

instance IsLabel "name" (Rec -> String) where
  fromLabel = name

instance IsLabel "value" (Rec -> Int) where
  fromLabel = value
```

## Examples

```haskell
{-# LANGUAGE OverloadedLabels #-}

import GHC.OverloadedLabels (IsLabel(..))

data MyRec = MyRec { myName :: String }

instance IsLabel "myName" (MyRec -> String) where
  fromLabel = myName

main :: IO ()
main = print (#myName (MyRec "hello"))
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Not in scope](/languages/haskell/haskell-not-in-scope)
- [Compile error](/languages/haskell/haskell-ghc-error)
