---
title: "[Solution] Haskell Type Class Instance Error"
description: "Fix Haskell type class instance errors when implementing orphan instances or overlapping type class definitions."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

Type class instance errors occur when orphan instances conflict, overlapping instances are detected, or instance declarations have incorrect types.

## Common Causes

- Orphan instance defined in module different from both type and class
- Overlapping instance declarations
- Instance context too specific or too general
- Missing FlexibleInstances extension

## How to Fix

### 1. Avoid orphan instances

```haskell
-- WRONG: Orphan instance
module Bad where
import MyTypes
import MyClasses
instance MyClass MyType where  -- orphan!

-- CORRECT: Define in module with type or class
module MyTypes where
import MyClasses
instance MyClass MyType where ...
```

### 2. Enable required extensions

```haskell
{-# LANGUAGE FlexibleInstances #-}
instance MyClass [Char] where ...
```

## Examples

```haskell
{-# LANGUAGE FlexibleInstances #-}

classDescribable :: String
classDescribable = "Type class instance demo"

class Greetable a where
    greet :: a -> String

instance Greetable String where
    greet s = "Hello, " ++ s

instance Greetable Int where
    greet n = "Hello, number " ++ show n
```

## Related Errors

- [Overlapping instances error](/languages/haskell/haskell-overlapping-instances)
- [No instance for](/languages/haskell/haskell-no-instance-for)
- [Flexible instances error](/languages/haskell/haskell-flexible-instances)
