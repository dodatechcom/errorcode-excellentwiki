---
title: "[Solution] Haskell NegativeLiterals Error"
description: "Fix Haskell NegativeLiterals errors when using negative numeric literal syntax."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

NegativeLiterals errors occur when the extension is not enabled or when negative literal syntax conflicts with standard negation.

## Common Causes

- NegativeLiterals extension not enabled
- Ambiguous negative literal vs negation
- Type inference failure with negative literals
- Incompatible with other numeric extensions

## How to Fix

### 1. Enable NegativeLiterals

```haskell
{-# LANGUAGE NegativeLiterals #-}

-- WRONG: No extension treats -42 as literal
-- x :: Int; x = -42

-- CORRECT: NegativeLiterals allows -42 as literal
x :: Int
x = -42
```

### 2. Provide type annotation

```haskell
{-# LANGUAGE NegativeLiterals #-}

process :: Int -> Int
process x = x + (-42)
```

## Examples

```haskell
{-# LANGUAGE NegativeLiterals #-}

negatives :: [Int]
negatives = [-1, -2, -3, -42]

main :: IO ()
main = print negatives
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Numeric error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
