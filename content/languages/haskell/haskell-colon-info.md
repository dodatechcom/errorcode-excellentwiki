---
title: "[Solution] Haskell :info — Type Information in GHCi"
description: "Fix :info command errors in GHCi. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1042
---

The `:info` (or `:i`) command in GHCi shows the type signature, instances, and source location of a name. Errors involve looking up names that do not exist or requesting info on names with ambiguous scope.

## Common Causes

- Typing a name that is not in scope (not imported or defined)
- Conflicting names from multiple modules
- Using `:info` on a type that has many instances (output is long)
- Name does not exist in the current GHCi session

## How to Fix

### 1. Make sure the name is in scope

```haskell
Prelude> :i filter
-- Shows the type and source

-- If not in scope, import it
import Data.Map
Prelude Data.Map> :i Map
```

### 2. Use fully qualified names to disambiguate

```haskell
Prelude> :i Data.Map.Map
```

### 3. Check instances of a typeclass

```haskell
Prelude> :i Functor
-- Shows all Functor instances in scope
```

### 4. Use :info on operators

```haskell
Prelude> :i (++)
-- Shows type and fixity
```

### 5. Combine with :type for deeper inspection

```haskell
:t length    -- shows type
:i length    -- shows type + source + instances
```

## Examples

Useful `:info` queries:

```haskell
-- Check a typeclass and its instances
:i Eq
:i Show
:i Functor

-- Check a specific function
:i head
:i foldl

-- Check a data type
:i Maybe
:i Either
:i IO
```

## Related Errors

- [Haskell :type Error](../haskell-colon-type)
- [Haskell :kind Error](../haskell-colon-kind)
- [Haskell Not In Scope](../haskell-not-in-scope)
