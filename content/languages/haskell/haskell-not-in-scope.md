---
title: "Variable Not in Scope in Haskell"
description: "Haskell raises scope errors when a variable or function name is not defined in the current scope"
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["scope", "variable", "undefined", "not-in-scope", "import"]
weight: 5
---

## What This Error Means

A "Variable not in scope" error occurs when a function or variable name is referenced but not defined or imported in the current scope. This is a compile-time error.

## Common Causes

- Typo in variable/function name
- Missing import statement
- Variable defined in different module
- Shadowed variable in nested scope
- Missing top-level definition

## How to Fix

Import the module:

```haskell
import Data.List (nub, sort)

uniqueSorted = sort . nub
```

Check spelling:

```haskell
-- WRONG
myFunciton x = x + 1

-- Correct
myFunction x = x + 1
```

Use qualified imports:

```haskell
import qualified Data.Map as Map

lookupKey key = Map.lookup key myMap
```

Define missing functions:

```haskell
-- If you use a function, define it
helper :: Int -> Int
helper x = x * 2

mainFunc x = helper x + 1
```

## Examples

```haskell
main = print (myFunction 5)
-- Error: Variable not in scope: myFunction
```

## Related Errors

- [Type error]({{< relref "/languages/haskell/type-error" >}})
- [Missing module]({{< relref "/languages/haskell/missing-module" >}})
