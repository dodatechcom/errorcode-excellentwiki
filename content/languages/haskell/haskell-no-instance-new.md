---
title: "[Solution] Haskell: no instance for type class arising from use"
description: "Fix Haskell no instance errors by defining type class instances and adding missing constraints."
languages: ["haskell"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `No instance for (SomeClass X) arising from a use of` error in Haskell means that a type class instance has not been defined for a specific type. Type classes in Haskell define interfaces that types must implement. When you try to use a function that requires a particular type class constraint on a type that does not have an instance for that class, the compiler reports this error. For example, trying to `show` a custom type without defining a `Show` instance produces this message.

## Why It Happens

This error occurs in several situations. The most straightforward is using a type with a type class function without defining the required instance. For example, calling `print` on a custom data type without a `Show` instance. Another cause is missing type class constraints in function signatures. If a function uses `==` on a type parameter, the signature must include an `Eq` constraint. Orphan instances, where an instance is defined in a module that defines neither the class nor the type, can cause problems when the instance is not in scope. You may also encounter this error when a type has an instance defined but it is not imported into the current module. Additionally, newtype wrappers sometimes need separate instances even if the underlying type already has one.

## How to Fix It

**Define the required type class instance:**

```haskell
data Color = Red | Green | Blue

-- WRONG: no Show instance defined
-- main = print Red

-- CORRECT: derive or define Show
data Color = Red | Green | Blue deriving (Show, Eq)
main = print Red  -- prints "Red"
```

**Manual instance definition for more control:**

```haskell
data Point = Point Double Double

instance Show Point where
  show (Point x y) = "(" ++ show x ++ ", " ++ show y ++ ")"

instance Eq Point where
  (Point x1 y1) == (Point x2 y2) = x1 == x2 && y1 == y2
```

**Add missing type class constraints to function signatures:**

```haskell
-- WRONG: missing Eq constraint
-- uniqueValues xs = nub xs

-- CORRECT: add the constraint
uniqueValues :: Eq a => [a] -> [a]
uniqueValues = nub
```

**Import orphan instances when needed:**

```haskell
-- If an orphan Show instance is in module OrphanInstances
import OrphanInstances ()  -- import just the instances
```

**Use GeneralizedNewtypeDeriving for newtypes:**

```haskell
newtype Age = Age Int deriving (Show, Eq, Ord, Num)
```

**Check that the instance is in scope:**

```haskell
-- Instance defined in Lib module
module Lib where
data MyType = MyType Int
instance Show MyType where
  show (MyType n) = "MyType " ++ show n

-- Main module must import Lib
module Main where
import Lib
main = print (MyType 42)
```

## Common Mistakes

- Forgetting that derived instances use default implementations that may not be ideal
- Not realizing that `deriving (Eq)` on sum types with record fields requires careful implementation
- Defining orphan instances that conflict with upstream library instances
- Missing the `Eq` constraint when using a type in a `Map` or `Set`
- Assuming `deriving all` works in older GHC versions without `DeriveAnyClass`

## Related Pages

- [Type error in Haskell](/languages/haskell/haskell-type-error-new)
- [Ambiguous type variable in Haskell](/languages/haskell/haskell-ambiguous-type-new)
- [Module not found in Haskell](/languages/haskell/haskell-module-not-found-new)
- [Variable not in scope in Haskell](/languages/haskell/haskell-not-in-scope-new)
