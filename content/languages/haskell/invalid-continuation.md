---
title: "Invalid character in name"
description: "An invalid character error occurs when using characters that aren't allowed in Haskell identifiers."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["character", "identifier", "syntax", "haskell"]
weight: 5
---

## What This Error Means

An `Invalid character in name` error occurs when you use characters that aren't allowed in Haskell identifiers. Haskell has specific rules about what characters can appear in variable and type names.

## Common Causes

- Using special characters in identifiers
- Unicode characters in code
- Reserved words used as identifiers
- Invalid operator characters

## How to Fix

```haskell
-- WRONG: Invalid character in identifier
my-var = 10  -- Invalid character: -

-- CORRECT: Use valid characters
myVar = 10
```

```haskell
-- WRONG: Using reserved word
data = [1, 2, 3]  -- 'data' is reserved

-- CORRECT: Use different name
myData = [1, 2, 3]
```

## Examples

```haskell
-- Example 1: Hyphen in name
my-function = 10  -- Invalid character

-- Example 2: Special character
var@name = 10  -- Invalid character: @

-- Example 3: Unicode
café = "coffee"  -- may cause issues in some compilers
```

## Related Errors

- [Variable not in scope](/languages/haskell/variable-not-in-scope)
- [GHC compilation error](/languages/haskell/ghc-error)
