---
title: "[Solution] Haskell TypeInType Error"
description: "Fix Haskell TypeInType errors when unifying Type and * kinds in type-level programming."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

TypeInType errors occur when the extension is not enabled or when Type and * kind are used inconsistently.

## Common Causes

- TypeInType extension not enabled
- Using * instead of Type inconsistently
- Missing KindSignatures extension
- Kind variable not properly bound

## How to Fix

### 1. Enable TypeInType

```haskell
{-# LANGUAGE TypeInType #-}

-- WRONG: Old syntax
-- f :: * -> *

-- CORRECT
f :: Type -> Type
f x = x
```

### 2. Use consistent kind syntax

```haskell
{-# LANGUAGE TypeInType #-}
{-# LANGUAGE KindSignatures #-}

import Data.Kind (Type)

container :: Type -> Type
container a = [a]
```

## Examples

```haskell
{-# LANGUAGE TypeInType #-}
{-# LANGUAGE KindSignatures #-}

import Data.Kind (Type)

data Proxy (a :: k) = Proxy

main :: IO ()
main = print (Proxy :: Proxy 42)
```

## Related Errors

- [Kind error](/languages/haskell/haskell-colon-kind)
- [Star is type error](/languages/haskell/haskell-star-is-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
