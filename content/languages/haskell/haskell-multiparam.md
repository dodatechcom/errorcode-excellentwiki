---
title: "[Solution] Haskell MultiParamTypeClasses — Multi-Parameter Typeclasses"
description: "Fix MultiParamTypeClasses errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1014
---

Multi-parameter typeclasses allow a class to relate two or more types. Errors typically involve ambiguous type resolution when GHC cannot determine which instance to use because the parameters are not sufficiently constrained.

## Common Causes

- GHC cannot infer which instance to use when multiple type parameters are polymorphic
- Missing `FlexibleInstances` for non-standard instance heads
- Functional dependencies are needed but not declared
- Two instances have overlapping type parameter combinations

## How to Fix

### 1. Enable the extension

```haskell
{-# LANGUAGE MultiParamTypeClasses #-}
```

### 2. Add functional dependencies to guide inference

```haskell
{-# LANGUAGE MultiParamTypeClasses #-}
{-# LANGUAGE FunctionalDependencies #-}

class Convert a b | a -> b where
  convert :: a -> b
```

### 3. Use FlexibleInstances for concrete types

```haskell
{-# LANGUAGE MultiParamTypeClasses #-}
{-# LANGUAGE FlexibleInstances #-}

class HasField s a where
  getField :: s -> a

instance HasField Person String where
  getField (Person n _) = n
```

### 4. Provide explicit type annotations at use sites

```haskell
convert @Int @String 42
```

### 5. Consider using associated types instead

```haskell
-- Multi-param with fundep
class Container c e | c -> e where ...

-- Cleaner alternative with associated type
class Container c where
  type Elem c
  insert :: Elem c -> c -> c
```

## Examples

A printable collection class:

```haskell
{-# LANGUAGE MultiParamTypeClasses #-}

class PrintableCollection c a where
  prettyPrint :: c -> a -> String

instance PrintableCollection [Int] Int where
  prettyPrint xs x = show x ++ " in " ++ show xs
```

## Related Errors

- [Haskell FunctionalDependencies](../haskell-functional-dependencies)
- [Haskell FlexibleInstances](../haskell-flexible-instances)
- [Haskell Typeclass Conflict](../haskell-typeclass-conflict)
