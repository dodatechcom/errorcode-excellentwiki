---
title: "[Solution] Haskell Variable Not in Scope Error"
description: "Fix Haskell 'variable not in scope' error when names aren't accessible. Check imports, module exports, and variable definitions."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The error `Variable not in scope: X` occurs when a variable or function name is referenced but hasn't been defined or imported in the current scope. This is a compile-time error in Haskell.

## Common Causes

- Variable defined in different module without import
- Typo in variable name
- Missing import statement
- Variable not exported from module
- Shadowing issues with local bindings

## How to Fix

```haskell
-- WRONG: Missing import
module Main where
main = print (Data.List.sort [3,1,2])  -- Not in scope: sort

-- CORRECT: Import required module
import Data.List (sort)
main = print (sort [3,1,2])
```

```haskell
-- WRONG: Variable defined in where clause accessed outside
f x = y + x
  where y = 10
print y  -- Not in scope: y

-- CORRECT: Use the function or define y at top level
f x = y + x
  where y = 10
main = print (f 5)
```

```haskell
-- WRONG: Typo in function name
myFunction :: Int -> Int
myFunction x = x + 1

main = print (myFuncion 5)  -- Not in scope: myFuncion

-- CORRECT: Check spelling
main = print (myFunction 5)
```

## Examples

```haskell
-- Example 1: Import specific functions
import Data.Map (Map, fromList, lookup)

-- Example 2: Qualified imports
import qualified Data.Map as Map
main = print (Map.lookup "key" myMap)

-- Example 3: Module exports
module MyModule
    ( myFunction
    , MyType(..)
    ) where
-- Only myFunction and MyType are exported
```

## Related Errors

- [haskell-type-error]({{< relref "/languages/haskell/haskell-type-error" >}}) — type error
- [haskell-pattern-match]({{< relref "/languages/haskell/haskell-pattern-match" >}}) — pattern match
- [haskell-missing-module]({{< relref "/languages/haskell/haskell-missing-module" >}}) — missing module
