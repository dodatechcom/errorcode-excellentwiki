---
title: "[Solution] Haskell KindErrors Extension"
description: "Fix Haskell kind-related compilation errors when type-level and kind-level programming conflicts arise."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

Kind errors occur when type-level programming constructs have mismatched kinds, often seen with DataKinds or TypeInType extensions.

## Common Causes

- Inferred kind does not match expected kind
- Promoted constructor used at wrong kind level
- Missing DataKinds or TypeFamilies extension
- Kind variable escape in type signature

## How to Fix

### 1. Add kind signatures

```haskell
{-# LANGUAGE KindSignatures #-}
{-# LANGUAGE DataKinds #-}

import Data.Kind (Type)

data SNat (n :: Type) where
  SZ :: SNat 0
  SS :: SNat n -> SNat (n + 1)
```

### 2. Enable required extensions

```haskell
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE KindSignatures #-}
{-# LANGUAGE TypeOperators #-}
{-# LANGUAGE TypeFamilies #-}
```

## Examples

```haskell
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE KindSignatures #-}
{-# LANGUAGE TypeOperators #-}
{-# LANGUAGE TypeFamilies #-}

import Data.Kind (Type)

type family Plus (a :: Type) (b :: Type) :: Type where
  Plus 0 b = b
  Plus a b = a  -- simplified

main :: IO ()
main = print "Kind errors demo"
```

## Related Errors

- [Kind error](/languages/haskell/haskell-colon-kind)
- [Type error](/languages/haskell/haskell-type-error)
- [DataKinds error](/languages/haskell/haskell-data-kinds)
