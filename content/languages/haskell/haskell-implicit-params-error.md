---
title: "[Solution] Haskell ImplicitParams Error"
description: "Fix Haskell ImplicitParams errors when using implicit parameter types for dependency injection patterns."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

ImplicitParams errors occur when the ImplicitParams extension is not enabled or when implicit parameters are not properly bound in calling contexts.

## Common Causes

- ImplicitParams extension not enabled
- Implicit parameter not bound at call site
- Type mismatch in implicit parameter type
- Conflicting implicit parameter bindings

## How to Fix

### 1. Enable ImplicitParams

```haskell
{-# LANGUAGE ImplicitParams #-}

func :: (?threshold :: Double) => [Double] -> [Double]
func = filter (> ?threshold)
```

### 2. Bind implicit at call site

```haskell
let ?threshold = 0.5 in func [0.1, 0.6, 0.3, 0.8]
```

## Examples

```haskell
{-# LANGUAGE ImplicitParams #-}

type HasVerbosity = (?verbosity :: Int)

logMessage :: HasVerbosity => String -> IO ()
logMessage msg
  | ?verbosity > 0 = putStrLn msg
  | otherwise = return ()

main :: IO ()
main = let ?verbosity = 2 in logMessage "Debug info"
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Not in scope](/languages/haskell/haskell-not-in-scope)
- [Compile error](/languages/haskell/haskell-ghc-error)
