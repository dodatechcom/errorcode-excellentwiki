---
title: "[Solution] Haskell :kind — Kind Inquiry in GHCi"
description: "Fix :kind command errors in GHCi. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1043
---

The `:kind` (or `:k`) command in GHCi shows the kind of a type. Errors involve type constructors with unsatisfied parameters, or asking for the kind of a term-level name.

## Common Causes

- Using `:kind` on a term-level name (function or value)
- Type constructor needs parameters to have a valid kind
- Missing PolyKinds or KindSignatures extensions
- Asking for the kind of a type that does not exist in scope

## How to Fix

### 1. Use :kind only on types

```haskell
:k Int       -- *
:k Maybe     -- * -> *
:k Either    -- * -> * -> *
:k IO        -- * -> *
```

### 2. Provide partial application for kind inference

```haskell
:k Either Int     -- * -> *
:k Either Int Bool -- *
```

### 3. Enable PolyKinds for kind polymorphism

```haskell
:set -XPolyKinds
:k Proxy          -- forall k. k -> *
```

### 4. Use :kind with DataKinds for promoted types

```haskell
:set -XDataKinds
:k 'True          -- Bool (the promoted kind)
:k 'Just          -- forall a. Maybe a (promoted)
```

### 5. Check kind signatures of type families

```haskell
:set -XTypeFamilies
:k F    -- if type family F is defined, shows its kind
```

## Examples

Kind exploration in GHCi:

```haskell
:k Bool         -- *
:k Maybe        -- * -> *
:k Maybe Bool   -- *
:k Const        -- * -> * -> *
:k Const Int    -- * -> *
:k Proxy        -- * -> *
:k Const Int Bool -- *

-- With DataKinds
:set -XDataKinds
:k 'Nothing          -- Maybe a (promoted)
:k '(['True, 'False]) -- [Bool] (promoted list)
```

## Related Errors

- [Haskell :type Error](../haskell-colon-type)
- [Haskell :info Error](../haskell-colon-info)
- [Haskell Kind Error](../haskell-kind-error)
