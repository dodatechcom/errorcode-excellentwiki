---
title: "[Solution] Haskell TypeOperators Error"
description: "Fix Haskell TypeOperators errors when using custom infix type operators in type expressions."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

TypeOperators errors occur when the TypeOperators extension is not enabled or when type operators have incorrect fixity or precedence.

## Common Causes

- TypeOperators extension not enabled
- Type operator not defined before use
- Incorrect fixity declaration for type operator
- Ambiguous type expression with operators

## How to Fix

### 1. Enable TypeOperators

```haskell
{-# LANGUAGE TypeOperators #-}

data a :+: b = Inl a | Inr b

type family a <|> b
```

### 2. Define fixity

```haskell
{-# LANGUAGE TypeOperators #-}

data a :*: b = Pair a b

infixr 7 :*:
```

## Examples

```haskell
{-# LANGUAGE TypeOperators #-}

data a :+: b = L a | R b
  deriving (Show)

infixr 6 :+:

combine :: (Int :+: String) -> String
combine (L n) = show n
combine (R s) = s

main :: IO ()
main = print (combine (R "hello"))
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Kind error](/languages/haskell/haskell-colon-kind)
- [Compile error](/languages/haskell/haskell-ghc-error)
