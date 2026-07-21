---
title: "[Solution] Haskell StarIsType Error"
description: "Fix Haskell StarIsType errors when using * as a kind for Types instead of Type."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

StarIsType errors occur when the deprecated * kind syntax is used in type signatures instead of the modern Type kind.

## Common Causes

- Using * instead of Type in kind signatures
- StarIsType extension needed for legacy code
- Kind annotations with deprecated syntax
- Conflicting kind syntax across modules

## How to Fix

### 1. Use Type instead of *

```haskell
-- WRONG: Deprecated
-- f :: * -> *

-- CORRECT: Modern syntax
{-# LANGUAGE KindSignatures #-}
import Data.Kind (Type)
f :: Type -> Type
f x = x
```

### 2. Enable StarIsType for compatibility

```haskell
{-# LANGUAGE StarIsType #-}
-- Allows * as synonym for Type
```

## Examples

```haskell
{-# LANGUAGE KindSignatures #-}
import Data.Kind (Type)

container :: Type -> Type
container a = [a]

main :: IO ()
main = print (container [1,2,3] :: [[Int]])
```

## Related Errors

- [Kind error](/languages/haskell/haskell-colon-kind)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
