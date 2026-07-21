---
title: "[Solution] Haskell StandaloneDeriving Error"
description: "Fix Haskell StandaloneDeriving errors when manually specifying deriving clauses outside data declarations."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

StandaloneDeriving errors occur when the StandaloneDeriving extension is not enabled or when the derived instance cannot be generated.

## Common Causes

- StandaloneDeriving extension not enabled
- Instance cannot be derived for the type
- Context too specific or too general
- Conflict with stock deriving

## How to Fix

### 1. Enable StandaloneDeriving

```haskell
{-# LANGUAGE StandaloneDeriving #-}

data Foo = Foo Int

deriving instance Show Foo
```

### 2. Add necessary context

```haskell
{-# LANGUAGE StandaloneDeriving #-}

data Bar a = Bar [a]

deriving instance Show a => Show (Bar a)
```

## Examples

```haskell
{-# LANGUAGE StandaloneDeriving #-}

data Wrapper a = Wrapper a

deriving instance Eq a => Eq (Wrapper a)
deriving instance Show a => Show (Wrapper a)

main :: IO ()
main = print (Wrapper 42)
```

## Related Errors

- [Deriving error](/languages/haskell/haskell-deriving-error)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
