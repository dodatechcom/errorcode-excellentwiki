---
title: "[Solution] Haskell MutableArray — Mutable Array Errors"
description: "Fix MutableArray errors in ST and IO. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1026
---

Mutable arrays (`STUArray`, `IOUArray`, `MArray`) provide efficient in-place array updates. Errors involve bounds violations, wrong element types for unboxed arrays, or attempting to use mutable arrays outside their monad scope.

## Common Causes

- Array index out of bounds (no automatic bounds checking for unboxed arrays)
- Using the wrong monad type variable in `STUArray s` when `s` escapes `runST`
- Confusing boxed `Array` with unboxed `UArray` / `STUArray`
- Forgetting to `freeze` or `thaw` arrays when converting between mutable and immutable

## How to Fix

### 1. Check array bounds before indexing

```haskell
import Data.Array.ST
import Control.Monad.ST

example :: STUArray s Int Int -> ST s (Maybe Int)
example arr = do
  (_, hi) <- getBounds arr
  if hi >= 0
    then Just <$> readArray arr 0
    else return Nothing
```

### 2. Use thaw and freeze to convert between mutable and immutable

```haskell
import Data.Array.Unboxed
import Data.Array.ST
import Control.Monad.ST

modifyArray :: UArray Int Int -> UArray Int Int
modifyArray arr = runST $ do
  marr <- thaw arr
  writeArray marr 0 999
  freeze marr
```

### 3. Use newArray for initialization

```haskell
import Data.Array.ST
import Control.Monad.ST

initArray :: STUArray s Int Int
initArray = undefined  -- must be inside ST

example = do
  arr <- newArray (0, 9) 0 :: STUArray s Int Int
  writeArray arr 5 42
  val <- readArray arr 5
  return val
```

### 4. Use getElems to extract all values

```haskell
import Data.Array.ST

getAll :: STUArray s Int Int -> ST s [Int]
getAll arr = getElems arr
```

### 5. Use listArray for initialization from a list

```haskell
import Data.Array.Unboxed

arr :: UArray Int Int
arr = listArray (0, 4) [10, 20, 30, 40, 50]
```

## Examples

An in-place array reversal:

```haskell
import Data.Array.ST
import Control.Monad.ST

reverseArray :: UArray Int Int -> UArray Int Int
reverseArray arr = runST $ do
  let (lo, hi) = bounds arr
  marr <- thaw arr
  let swap i j = do
        a <- readArray marr i
        b <- readArray marr j
        writeArray marr i b
        writeArray marr j a
  mapM_ (\i -> swap i (hi - i + lo)) [lo..(lo + hi) `div` 2]
  freeze marr
```

## Related Errors

- [Haskell ST Monad Error](../haskell-st-monad)
- [Haskell ForeignPtr Error](../haskell-foreignptr)
- [Haskell Bounds Error](../haskell-bounds)
