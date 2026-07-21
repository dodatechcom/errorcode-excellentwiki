---
title: "[Solution] Haskell DataKinds Kind Error"
description: "Fix Haskell DataKinds errors when promoting data constructors to types for type-level programming."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

DataKinds kind errors occur when promoted data constructors are used incorrectly at the type level.

## Common Causes

- DataKinds extension not enabled
- Promoted constructor used at term level
- Kind mismatch between promoted and regular types
- Missing kind signature for promoted type

## How to Fix

### 1. Enable DataKinds

```haskell
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE KindSignatures #-}

data BoolKind = TrueKind | FalseKind

data SBool (b :: BoolKind) where
  STrue  :: SBool 'TrueKind
  SFalse :: SBool 'FalseKind
```

### 2. Use promoted constructors correctly

```haskell
{-# LANGUAGE DataKinds #-}

data Nat = Z | S Nat

type One = 'S 'Z
type Two = 'S ('S 'Z)
```

## Examples

```haskell
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE KindSignatures #-}

data Length = Short | Long

data Door (s :: Length) where
  Open  :: Door 'Short
  Closed :: Door 'Long

main :: IO ()
main = print "DataKinds demo"
```

## Related Errors

- [Kind error](/languages/haskell/haskell-colon-kind)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
