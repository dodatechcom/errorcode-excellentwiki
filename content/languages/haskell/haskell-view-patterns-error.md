---
title: "[Solution] Haskell ViewPatterns Error"
description: "Fix Haskell ViewPatterns errors when using view patterns for pattern matching with function application."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

ViewPatterns errors occur when the ViewPatterns extension is not enabled or when the view function type does not match the pattern.

## Common Causes

- ViewPatterns extension not enabled
- View function returns wrong type
- Circular dependency in view function
- View pattern producing non-exhaustive patterns

## How to Fix

### 1. Enable ViewPatterns

```haskell
{-# LANGUAGE ViewPatterns #-}

getLength :: [a] -> Int
getLength = length

process :: (getLength -> Int) -> String -> String
process (getLength -> 0) = "empty"
process (getLength -> n) = "length " ++ show n
```

### 2. Ensure view function type is correct

```haskell
{-# LANGUAGE ViewPatterns #-}

import Data.Char (toUpper)

upperCase :: String -> String
upperCase = map toUpper

greet :: (upperCase -> String) -> String
greet (upperCase -> "HELLO") = "greeting"
greet _ = "other"
```

## Examples

```haskell
{-# LANGUAGE ViewPatterns #-}

import Data.List (isPrefixOf)

normalize :: String -> String
normalize = map toUpper

checkInput :: (normalize -> String) -> String
checkInput (normalize -> "ERROR") = "error detected"
checkInput (normalize -> "WARN")  = "warning detected"
checkInput _                      = "ok"

main :: IO ()
main = print (checkInput "error")
```

## Related Errors

- [Pattern match error](/languages/haskell/haskell-pattern-match)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Type error](/languages/haskell/haskell-type-error)
