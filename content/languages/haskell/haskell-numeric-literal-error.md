---
title: "[Solution] Haskell NumSmallBits Error"
description: "Fix Haskell NumSuperstar and numeric extension errors when using extended numeric literal syntax."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

Numeric extension errors occur when NumLiteral or similar extensions are used incorrectly or when numeric literal syntax conflicts.

## Common Causes

- Numeric extension not enabled
- Literal syntax incompatible with target type
- Overloaded numeric literal ambiguity
- Missing Num instance for custom type

## How to Fix

### 1. Ensure Num instance exists

```haskell
data MyNum = MyNum Int

instance Num MyNum where
    (MyNum a) + (MyNum b) = MyNum (a + b)
    (MyNum a) * (MyNum b) = MyNum (a * b)
    abs (MyNum a) = MyNum (abs a)
    signum (MyNum a) = MyNum (signum a)
    fromInteger n = MyNum (fromInteger n)
    negate (MyNum a) = MyNum (negate a)
```

### 2. Use Overloaded literals

```haskell
{-# LANGUAGE OverloadedNumPrels #-}

zero :: MyNum
zero = 0  -- uses fromInteger
```

## Examples

```haskell
newtype Dollars = Dollars Int
  deriving (Show, Eq, Num)

price :: Dollars
price = Dollars 100

tax :: Dollars
tax = price * 8  -- uses Num instance

main :: IO ()
main = print tax
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [No instance for](/languages/haskell/haskell-no-instance-for)
- [Compile error](/languages/haskell/haskell-ghc-error)
