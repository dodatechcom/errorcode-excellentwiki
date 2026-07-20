---
title: "[Solution] Haskell OverlappingInstances — Conflicting Typeclass Instances"
description: "Fix OverlappingInstances errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1007
---

`OverlappingInstances` allows GHC to choose the most specific typeclass instance when multiple instances could apply to a type. Without it, any overlap is an error. In GHC 8+, the more precise `OverlappingInstances` and `IncoherentInstances` pragmas are per-instance.

## Common Causes

- Defining instances for both a general type `a` and a specific type `Int`
- Library instances conflicting with your own instances
- Using type variables in instance heads that can overlap with concrete types

## How to Fix

### 1. Use the OVERLAPPING pragma on the specific instance

```haskell
instance {-# OVERLAPPING #-} Show [Char] where
  show xs = "Custom string: " ++ xs
```

### 2. Use OVERLAPPABLE on the general instance

```haskell
instance {-# OVERLAPPABLE #-} Show a => Show [a] where
  show xs = show (length xs) ++ " elements"
```

### 3. Avoid overlap by restructuring

```haskell
-- Instead of overlapping instances, use a typeclass with a default
class MyShow a where
  myShow :: a -> String

instance MyShow Int where
  myShow n = "Int: " ++ show n

instance MyShow Double where
  myShow d = "Double: " ++ show d
```

### 4. Use closed type families as an alternative

```haskell
{-# LANGUAGE TypeFamilies #-}

type family ShowResult a where
  ShowResult Int    = String
  ShowResult Double = String
  ShowResult a      = Show a => String
```

### 5. Mark instances with INCOHERENT when order does not matter

```haskell
instance {-# INCOHERENT #-} Show a where
  show _ = "<anything>"
```

## Examples

Two instances that overlap without the extension:

```haskell
{-# LANGUAGE OverlappingInstances #-}

class Describable a where
  describe :: a -> String

instance Describable String where
  describe s = "String: " ++ s

instance {-# OVERLAPPING #-} Describable [Char] where
  describe s = "Chars: " ++ s

main = print (describe "hello" :: String)
-- Chars: hello
```

## Related Errors

- [Haskell FlexibleInstances](../haskell-flexible-instances)
- [Haskell No Instance For](../haskell-no-instance-for)
- [Haskell Typeclass Conflict](../haskell-typeclass-conflict)
