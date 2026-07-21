---
title: "[Solution] Haskell MagicHash Error"
description: "Fix Haskell MagicHash errors when using unboxed types with the # suffix for low-level GHC operations."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

MagicHash errors occur when the MagicHash extension is not enabled or when unboxed types with # suffix are used incorrectly.

## Common Causes

- MagicHash extension not enabled
- Unboxed type used in wrong context
- Missing UnboxedTuples or other extensions
- Incorrect kind for magic hash type

## How to Fix

### 1. Enable MagicHash

```haskell
{-# LANGUAGE MagicHash #-}

-- WRONG: No extension
-- x = 42#

-- CORRECT
import GHC.Exts

x :: Int#
x = 42#
```

### 2. Use with GHC.Exts

```haskell
{-# LANGUAGE MagicHash #-}

import GHC.Exts

plusInt :: Int# -> Int# -> Int#
plusInt x y = x +# y
```

## Examples

```haskell
{-# LANGUAGE MagicHash #-}

import GHC.Exts

fibonacciFast :: Int# -> Int#
fibonacciFast n = go n 0# 1#
  where
    go 0# a _ = a
    go 1# _ b = b
    go m a b = go (m -# 1#) b (a +# b)

main :: IO ()
main = print "Magic hash demo"
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Kind error](/languages/haskell/haskell-colon-kind)
