---
title: "[Solution] Haskell HexFloatLiterals Error"
description: "Fix Haskell HexFloatLiterals errors when using hexadecimal floating-point literal syntax."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

HexFloatLiterals errors occur when the extension is not enabled or when hexadecimal float syntax is incorrectly formatted.

## Common Causes

- HexFloatLiterals extension not enabled
- Invalid hexadecimal float format
- Missing exponent in hex float
- Type mismatch with hex float literal

## How to Fix

### 1. Enable HexFloatLiterals

```haskell
{-# LANGUAGE HexFloatLiterals #-}

-- WRONG: No extension
-- x = 0x1.0p10

-- CORRECT
x :: Double
x = 0x1.0p10
```

### 2. Use correct format

```haskell
{-# LANGUAGE HexFloatLiterals #-}

val :: Double
val = 0xF.Fp2  -- 15.9375 * 4
```

## Examples

```haskell
{-# LANGUAGE HexFloatLiterals #-}

main :: IO ()
main = do
  let hex = 0x1.0p4 :: Double
  putStrLn $ "Hex float: " ++ show hex
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Numeric error](/languages/haskell/haskell-type-error)
