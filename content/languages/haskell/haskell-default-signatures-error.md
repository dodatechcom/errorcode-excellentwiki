---
title: "[Solution] Haskell DefaultSignatures Error"
description: "Fix Haskell DefaultSignatures errors when providing default implementations for type class methods."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

DefaultSignatures errors occur when the extension is not enabled or when default signature types do not match the method signature.

## Common Causes

- DefaultSignatures extension not enabled
- Default signature type does not match method type
- Generic default signature uses wrong type
- Missing Generic constraint on default

## How to Fix

### 1. Enable DefaultSignatures

```haskell
{-# LANGUAGE DefaultSignatures #-}

class MyClass a where
    myMethod :: a -> String
    default myMethod :: Show a => a -> String
    myMethod = show
```

### 2. Ensure type matches

```haskell
{-# LANGUAGE DefaultSignatures #-}
{-# LANGUAGE DeriveGeneric #-}

import GHC.Generics (Generic)

class MyShow a where
    myShow :: a -> String
    default myShow :: (Generic a, GShow (Rep a)) => a -> String
    myShow = gshow . from
```

## Examples

```haskell
{-# LANGUAGE DefaultSignatures #-}

class Describable a where
    describe :: a -> String
    default describe :: Show a => a -> String
    describe = show

data Color = Red | Green | Blue
  deriving (Show)

instance Describable Color

main :: IO ()
main = print (describe Red)
```

## Related Errors

- [Type class error](/languages/haskell/haskell-type-class-error)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
