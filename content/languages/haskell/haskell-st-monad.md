---
title: "[Solution] Haskell ST Monad — Local Mutable State Errors"
description: "Fix ST monad errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1021
---

The ST monad provides safe mutable state and arrays within a scoped computation. Errors involve using `runST` incorrectly, leaking mutable references outside the ST scope, or forgetting that the rank-2 type of `runST` prevents escape.

## Common Causes

- Trying to return a mutable `STRef` or `STUArray` from `runST`
- Not enabling `RankNTypes` (required by `runST`'s type signature)
- Using `ST` when `IORef` would be simpler
- Confusing `ST s a` with `IO a`

## How to Fix

### 1. Enable RankNTypes if needed

```haskell
{-# LANGUAGE RankNTypes #-}
-- runST :: (forall s. ST s a) -> a
-- requires Rank2Types / RankNTypes to compile
```

### 2. Do not return mutable references from runST

```haskell
import Control.Monad.ST
import Data.STRef

-- WRONG: STRef escapes the ST scope
bad = runST $ do
  ref <- newSTRef 0
  return ref  -- STRef s Int, but s is bound locally

-- CORRECT: return the pure value
good = runST $ do
  ref <- newSTRef 0
  writeSTRef ref 42
  readSTRef ref  -- returns Int, pure
```

### 3. Use STUArray for unboxed arrays

```haskell
import Control.Monad.ST
import Data.Array.ST

sortST :: [Int] -> [Int]
sortST xs = runST $ do
  arr <- newListArray (0, length xs - 1) xs :: STUArray s Int Int
  -- sort the array in place
  elems arr
```

### 4. Use unsafeFreeze to convert mutable to immutable

```haskell
import Control.Monad.ST
import Data.Array.ST
import Data.Array.Unboxed (UArray, listArray)

copyAndModify :: UArray Int Int -> UArray Int Int
copyAndModify arr = runST $ do
  marr <- thaw arr
  writeArray marr 0 999
  freeze marr
```

### 5. Prefer IORef for top-level mutable state

```haskell
import Data.IORef

globalRef :: IORef Int
globalRef = unsafePerformIO (newIORef 0)
{-# NOINLINE globalRef #-}
```

## Examples

An in-place sorting algorithm using ST:

```haskell
import Control.Monad.ST
import Data.Array.ST
import Data.Array.Unboxed

bubbleSort :: UArray Int Int -> UArray Int Int
bubbleSort arr = runST $ do
  let (lo, hi) = bounds arr
  marr <- thaw arr
  let swap i j = do
        a <- readArray marr i
        b <- readArray marr j
        writeArray marr i b
        writeArray marr j a
  -- simplified single pass
  mapM_ (\i -> do
    a <- readArray marr i
    b <- readArray marr (i+1)
    when (a > b) (swap i (i+1))
    ) [lo..hi-1]
  freeze marr
```

## Related Errors

- [Haskell IO Monad Error](../haskell-io-monad)
- [Haskell MutableArray Error](../haskell-mutable-array)
- [Haskell ForeignPtr Error](../haskell-foreignptr)
