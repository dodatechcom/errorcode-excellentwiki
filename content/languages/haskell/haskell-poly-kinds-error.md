---
title: "[Solution] Haskell PolyKinds Error"
description: "Fix Haskell PolyKinds errors when using polymorphic kinds in type-level programming."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

PolyKinds errors occur when the extension is not enabled or when kind variables are not properly bound.

## Common Causes

- PolyKinds extension not enabled
- Kind variable not bound in type signature
- Missing kind signature for polymorphic kind
- Conflicting kind inference

## How to Fix

### 1. Enable PolyKinds

```haskell
{-# LANGUAGE PolyKinds #-}

-- WRONG: No extension
-- data Proxy a = Proxy

-- CORRECT
data Proxy (a :: k) = Proxy
```

### 2. Bind kind variables explicitly

```haskell
{-# LANGUAGE PolyKinds #-}
{-# LANGUAGE KindSignatures #-}

data Proxy (a :: k) = Proxy

getProxy :: Proxy (a :: k) -> Proxy (a :: k)
getProxy Proxy = Proxy
```

## Examples

```haskell
{-# LANGUAGE PolyKinds #-}

data Proxy a = Proxy

main :: IO ()
main = print (Proxy :: Proxy 42)
```

## Related Errors

- [Kind error](/languages/haskell/haskell-colon-kind)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
