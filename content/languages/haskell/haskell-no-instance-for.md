---
title: "[Solution] Haskell No Instance For — Missing Typeclass Instance"
description: "Fix GHC 'No instance for' errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1004
---

The "No instance for" error means you are using a typeclass method on a type that has no instance for that class. GHC lists the missing instance in the error message.

## Common Causes

- Calling a typeclass method (like `show`, `==`, or `fmap`) on a custom type without deriving or defining the instance
- Using a library type with a class it does not support
- Forgetting to import the module that defines the instance
- Overlapping or orphan instances causing GHC to pick the wrong one

## How to Fix

### 1. Derive the instance automatically

```haskell
data Color = Red | Green | Blue
  deriving (Show, Eq, Ord)
```

### 2. Write a manual instance

```haskell
data Shape = Circle Double | Rect Double Double

instance Show Shape where
  show (Circle r) = "Circle " ++ show r
  show (Rect w h) = "Rect " ++ show w ++ "x" ++ show h
```

### 3. Import the module containing the instance

```haskell
-- WRONG: Data.Map does not have Foldable in scope
-- when using an older base
import Data.Map.Strict (Map)

-- CORRECT: make sure the instance is available
import Data.Map.Strict (Map)
-- Foldable (Map k) is defined in Data.Map
```

### 4. Enable FlexibleInstances for custom types

```haskell
{-# LANGUAGE FlexibleInstances #-}

instance Show [Char] where
  show xs = "Chars: " ++ xs
```

### 5. Use newtype wrappers for orphan instances

```haskell
newtype Insensitive = Insensitive String

instance Eq Insensitive where
  (Insensitive a) == (Insensitive b) = map toLower a == map toLower b
```

## Examples

A typical "No instance" with a user-defined type:

```haskell
data Point = Point Double Double

-- WRONG
print (Point 1.0 2.0 == Point 1.0 3.0)
-- No instance for (Eq Point)

-- CORRECT
data Point = Point Double Double deriving (Eq)

print (Point 1.0 2.0 == Point 1.0 3.0)  -- False
```

## Related Errors

- [Haskell Typeclass Instance Error](../haskell-typeclass-instance)
- [Haskell FlexibleInstances](../haskell-flexible-instances)
- [Haskell Orphan Instance Warning](../haskell-orphan-instance)
