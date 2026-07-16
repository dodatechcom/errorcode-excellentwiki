---
title: "GHC compilation error"
description: "A GHC compilation error occurs when the Glasgow Haskell Compiler encounters errors during compilation."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["ghc", "compilation", "compiler", "haskell"]
weight: 5
---

## What This Error Means

A GHC compilation error is a general category of errors that occur when the Glasgow Haskell Compiler cannot compile your code. These can range from syntax errors to type errors to missing modules.

## Common Causes

- Syntax errors
- Type mismatches
- Missing imports
- Missing dependencies in .cabal or stack.yaml

## How to Fix

```haskell
-- WRONG: Syntax error
add x y = x + y  -- missing type signature (warning, but can lead to issues)
-- Actually this works, but:

-- WRONG: Missing module
import NonExistent.Module  -- can't find module

-- CORRECT: Add to dependencies and import
-- In .cabal file: build-depends: base >=4.9
import Data.List
```

```haskell
-- WRONG: Circular imports
-- Module A imports Module B
-- Module B imports Module A

-- CORRECT: Restructure modules
-- Move shared code to a third module
```

## Examples

```haskell
-- Example 1: Missing module
import Data.Foo  -- can't find module: Data.Foo

-- Example 2: Syntax error
if True then "yes"  -- parse error on input 'then'

-- Example 3: Type error
True :: Int  -- Couldn't match type 'Bool' with 'Int'
```

## Related Errors

- [Variable not in scope](/languages/haskell/variable-not-in-scope)
- [Type mismatch](/languages/haskell/type-mismatch2)
