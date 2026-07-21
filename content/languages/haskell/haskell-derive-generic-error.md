---
title: "[Solution] Haskell DeriveGeneric Error"
description: "Fix Haskell DeriveGeneric errors when deriving Generic instances for type class default implementations."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

DeriveGeneric errors occur when the DeriveGeneric extension is not enabled or when Generic/Generic1 instances are incorrectly derived.

## Common Causes

- DeriveGeneric extension not enabled
- GHC.Generics not imported
- Generic instance required but not derived
- Conflicting Generic and stock deriving

## How to Fix

### 1. Enable DeriveGeneric

```haskell
{-# LANGUAGE DeriveGeneric #-}
import GHC.Generics (Generic)

data Foo = Foo Int String
  deriving (Show, Generic)
```

### 2. Import GHC.Generics

```haskell
{-# LANGUAGE DeriveGeneric #-}
import GHC.Generics (Generic, Generic1)

data Bar a = Bar a
  deriving (Show, Generic, Generic1)
```

## Examples

```haskell
{-# LANGUAGE DeriveGeneric #-}

import GHC.Generics (Generic)

data Point = Point { x :: Double, y :: Double }
  deriving (Show, Generic)

main :: IO ()
main = print (Point 1.0 2.0)
```

## Related Errors

- [Deriving error](/languages/haskell/haskell-deriving-error)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
