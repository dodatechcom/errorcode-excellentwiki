---
title: "Variable not in scope"
description: "A variable not in scope error occurs when referencing an undefined variable."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `Variable not in scope` error occurs when you reference a variable that hasn't been defined in the current scope. This is a compile-time error in Haskell.

## Common Causes

- Typo in variable name
- Variable defined in different scope
- Missing import
- Forgetting to bind variable

## How to Fix

```haskell
-- WRONG: Typo in variable name
myValue = 10
print myVal  -- Variable not in scope: myVal

-- CORRECT: Match variable name exactly
myValue = 10
print myValue
```

```haskell
-- WRONG: Variable from outer scope
main = do
    let x = 10
    print y  -- Variable not in scope: y

-- CORRECT: Define variable in scope
main = do
    let x = 10
        y = 20
    print y
```

## Examples

```haskell
-- Example 1: Undefined variable
x = y + 1  -- Variable not in scope: y

-- Example 2: Wrong scope
let x = 10 in x + y  -- Variable not in scope: y

-- Example 3: Missing import
-- If Data.Map is not imported
lookup "key" map  -- Variable not in scope
```

## Related Errors

- [GHC compilation error](/languages/haskell/ghc-error)
- [Invalid character in name](/languages/haskell/invalid-continuation)
