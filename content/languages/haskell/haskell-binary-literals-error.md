---
title: "[Solution] Haskell BinaryLiterals Error"
description: "Fix Haskell BinaryLiterals errors when using 0b prefix for binary numeric literals."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

BinaryLiterals errors occur when the extension is not enabled or when binary literal syntax is incorrectly used.

## Common Causes

- BinaryLiterals extension not enabled
- Invalid binary digit (not 0 or 1)
- Binary literal too large for target type
- Missing type annotation for binary literal

## How to Fix

### 1. Enable BinaryLiterals

```haskell
{-# LANGUAGE BinaryLiterals #-}

-- WRONG: No extension
-- x = 0b1010

-- CORRECT
x :: Int
x = 0b1010  -- 10 in decimal
```

### 2. Provide type annotation

```haskell
{-# LANGUAGE BinaryLiterals #-}

flags :: Int
flags = 0b10101010
```

## Examples

```haskell
{-# LANGUAGE BinaryLiterals #-}

main :: IO ()
main = do
  let pattern = 0b11110000 :: Int
  putStrLn $ "Binary pattern: " ++ show pattern
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Numeric literal error](/languages/haskell/haskell-numeric-literal-error)
