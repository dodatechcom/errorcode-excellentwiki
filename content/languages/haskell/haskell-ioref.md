---
title: "[Solution] Haskell IORef — Mutable Reference Errors"
description: "Fix IORef errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1025
---

`IORef` provides mutable references inside the IO monad. Errors involve using IORef in pure code, race conditions from concurrent access, or forgetting that IORef operations are in IO, not STM.

## Common Causes

- Using IORef in pure code (it requires IO or ST)
- Race conditions when multiple threads access the same IORef
- Forgetting to use `atomicModifyIORef'` for strict concurrent updates
- Using `readIORef` outside the IO monad

## How to Fix

### 1. Use IORef only inside IO or ST

```haskell
import Data.IORef

-- WRONG: cannot use IORef in pure code
-- pureFunc = do
--   ref <- newIORef 0
--   readIORef ref

-- CORRECT: use inside IO
main = do
  ref <- newIORef 0
  val <- readIORef ref
  print val
```

### 2. Use atomicModifyIORef' for thread-safe updates

```haskell
import Data.IORef

increment :: IORef Int -> IO ()
increment ref = atomicModifyIORef' ref (\n -> (n + 1, ()))
```

### 3. Use newIORef for initialization

```haskell
import Data.IORef

main = do
  ref <- newIORef []
  modifyIORef ref (++ ["hello"])
  val <- readIORef ref
  print val
```

### 4. Use writeIORef for direct writes

```haskell
import Data.IORef

reset :: IORef Int -> IO ()
reset ref = writeIORef ref 0
```

### 5. Use modifyIORef' (strict) to avoid space leaks

```haskell
import Data.IORef

-- WRONG: lazy, causes space leak
bad ref = modifyIORef ref (+1)

-- CORRECT: strict
good ref = modifyIORef' ref (+1)
```

## Examples

A simple counter using IORef:

```haskell
import Data.IORef

main :: IO ()
main = do
  counter <- newIORef 0
  mapM_ (\_ -> modifyIORef' counter (+1)) [1..1000]
  val <- readIORef counter
  putStrLn ("Count: " ++ show val)  -- Count: 1000
```

## Related Errors

- [Haskell STM Error](../haskell-stm-error)
- [Haskell TVar Error](../haskell-tvar)
- [Haskell MVar Error](../haskell-mvar)
