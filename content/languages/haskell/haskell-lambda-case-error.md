---
title: "[Solution] Haskell LambdaCase Error"
description: "Fix Haskell LambdaCase errors when using anonymous case expressions with the LambdaCase extension."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

LambdaCase errors occur when the LambdaCase extension is not enabled or when lambda-case syntax is incorrectly formed.

## Common Causes

- LambdaCase extension not enabled
- Missing backslash before case keyword
- Incomplete patterns in lambda case
- Lambda case used where regular lambda expected

## How to Fix

### 1. Enable LambdaCase

```haskell
{-# LANGUAGE LambdaCase #-}

-- WRONG: No extension
-- \case { Nothing -> 0; Just x -> x }

-- CORRECT
\case
    Nothing -> 0
    Just x  -> x
```

### 2. Ensure complete patterns

```haskell
{-# LANGUAGE LambdaCase #-}

handleMaybe :: Maybe Int -> Int
handleMaybe = \case
    Nothing -> 0
    Just x  -> x
```

## Examples

```haskell
{-# LANGUAGE LambdaCase #-}

main :: IO ()
main = mapM_ (\case
    0 -> putStrLn "zero"
    n -> putStrLn $ "number " ++ show n
    ) [0, 1, 2, 3]
```

## Related Errors

- [Pattern match error](/languages/haskell/haskell-pattern-match)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Parse error](/languages/haskell/haskell-parse-error)
