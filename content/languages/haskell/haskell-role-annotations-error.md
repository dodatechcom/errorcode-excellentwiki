---
title: "[Solution] Haskell RoleAnnotations Error"
description: "Fix Haskell RoleAnnotations errors when specifying nominal, representational, or phantom roles for type parameters."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

RoleAnnotations errors occur when the extension is not enabled or when role annotations conflict with the type definition.

## Common Causes

- RoleAnnotations extension not enabled
- Role annotation does not match type usage
- Phantom role used for parameter that has structure
- Conflicting role annotations

## How to Fix

### 1. Enable RoleAnnotations

```haskell
{-# LANGUAGE RoleAnnotations #-}

type role Map nominal representational
data Map k v = ...
```

### 2. Match roles to usage

```haskell
{-# LANGUAGE RoleAnnotations #-}

type role MyType nominal representational phantom
data MyType a b c = MyType a b
```

## Examples

```haskell
{-# LANGUAGE RoleAnnotations #-}

type role Container nominal
data Container a = Container [a]

main :: IO ()
main = print "Role annotations demo"
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Kind error](/languages/haskell/haskell-colon-kind)
- [Compile error](/languages/haskell/haskell-ghc-error)
