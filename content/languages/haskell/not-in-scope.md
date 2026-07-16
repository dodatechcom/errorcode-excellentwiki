---
title: "Variable not in scope"
description: "A variable not in scope error occurs when referencing an undefined variable or function."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["variable", "scope", "not-in-scope", "haskell"]
weight: 5
---

## What This Error Means

A `not in scope` error occurs when you reference a variable, function, or constructor that hasn't been defined or imported in the current scope. This is a common compile-time error.

## Common Causes

- Missing import declaration
- Typo in name
- Wrong module qualified name
- Private function accessed from outside

## How to Fix

```haskell
-- WRONG: Not importing module
main = print (sort [3, 1, 2])  -- Variable not in scope: sort

-- CORRECT: Import the module
import Data.List (sort)
main = print (sort [3, 1, 2])
```

```haskell
-- WRONG: Wrong qualified name
import qualified Data.Map as M
main = print (Map.lookup "key" M.empty)  -- not in scope: Map

-- CORRECT: Use correct qualification
main = print (M.lookup "key" M.empty)
```

## Examples

```haskell
-- Example 1: Missing import
main = print (nub [1, 2, 2, 3])  -- not in scope: nub

-- Example 2: Typo
myFunc = myFucn 1  -- not in scope: myFucn

-- Example 3: Wrong module
import qualified Data.Set as S
main = print (Set.empty)  -- not in scope: Set
```

## Related Errors

- [Variable not in scope](/languages/haskell/variable-not-in-scope)
- [GHC compilation error](/languages/haskell/ghc-error)
