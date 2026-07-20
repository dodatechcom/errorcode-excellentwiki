---
title: "[Solution] Haskell FlexibleInstances — Non-Standard Instance Declarations"
description: "Fix FlexibleInstances extension errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1006
---

The `FlexibleInstances` extension allows typeclass instances where the instance head contains type variables in positions other than the leftmost, or uses concrete types like `[Char]` instead of `[a]`. Without it, GHC restricts instances to the Haskell 98 form.

## Common Causes

- Defining an instance for a specific type application like `Maybe Int` instead of `Maybe a`
- Writing `instance Show [Char]` instead of `instance Show a => Show [a]`
- Overlapping-like patterns that GHC 98 forbids

## How to Fix

### 1. Enable the extension

```haskell
{-# LANGUAGE FlexibleInstances #-}
```

Or in your cabal file:

```cabal
default-extensions: FlexibleInstances
```

### 2. Use the standard form when possible

```haskell
-- Instead of
instance Show [Char] where ...

-- Prefer
instance Show Char where ...
-- which automatically covers [Char] via Show a => Show [a]
```

### 3. Combine with UndecidableInstances when needed

```haskell
{-# LANGUAGE FlexibleInstances #-}
{-# LANGUAGE UndecidableInstances #-}

instance Show a => Show (Wrapper a) where
  show (Wrapper x) = "Wrapper(" ++ show x ++ ")"
```

### 4. Avoid orphan instances

An orphan instance lives in a module that defines neither the class nor the type:

```haskell
-- In module MyOrphans (an orphan)
instance Eq MyType where ...

-- Better: put it with the type definition
-- In module MyTypes
data MyType = ...
instance Eq MyType where ...
```

### 5. Check for overlapping instances

```haskell
{-# LANGUAGE FlexibleInstances #-}

class Doubler a where
  doubler :: a -> a

instance Doubler Int where
  doubler x = x * 2

instance Doubler [a] where
  doubler xs = xs ++ xs
```

## Examples

A practical FlexibleInstances use case with a custom wrapper:

```haskell
{-# LANGUAGE FlexibleInstances #-}

newtype MyString = MyString String

instance Show MyString where
  show (MyString s) = "MyString: " ++ s

main = print (MyString "hello")
-- MyString: hello
```

## Related Errors

- [Haskell OverlappingInstances](../haskell-overlapping-instances)
- [Haskell MultiParamTypeClasses](../haskell-multiparam)
- [Haskell Orphan Instance Warning](../haskell-orphan-instance)
