---
title: "[Solution] Haskell KindSignatures Error"
description: "Fix Haskell KindSignatures errors when annotating type parameters with their kinds."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

KindSignatures errors occur when the extension is not enabled or when kind signatures do not match the actual kind of the type.

## Common Causes

- KindSignatures extension not enabled
- Kind signature does not match inferred kind
- Missing import for Constraint kind
- Using * where Type is required

## How to Fix

### 1. Enable KindSignatures

```haskell
{-# LANGUAGE KindSignatures #-}

data Proxy (a :: * ) = Proxy
```

### 2. Import Data.Kind for Type

```haskell
{-# LANGUAGE KindSignatures #-}
import Data.Kind (Type)

data Proxy (a :: Type) = Proxy
```

## Examples

```haskell
{-# LANGUAGE KindSignatures #-}
import Data.Kind (Type)

class MyClass (a :: Type) where
  myMethod :: a -> String

main :: IO ()
main = print "KindSignatures demo"
```

## Related Errors

- [Kind error](/languages/haskell/haskell-colon-kind)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
