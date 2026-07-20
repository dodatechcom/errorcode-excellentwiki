---
title: "[Solution] Haskell TVar — Transactional Variable Errors"
description: "Fix TVar STM errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1023
---

`TVar` is the STM equivalent of an `IORef`—a mutable variable that can only be read and written inside an STM transaction. Errors involve using TVar outside `atomically`, race conditions from non-atomic reads, or deadlock from retry.

## Common Causes

- Reading a TVar with `readTVarIO` in a non-atomic context when consistency is needed
- Non-atomic read-then-write causing race conditions
- Forgetting that TVar operations must be inside `STM`, not `IO`
- Circular dependencies between TVars causing deadlock via `retry`

## How to Fix

### 1. Always use atomically for multi-TVar operations

```haskell
import Control.Concurrent.STM

-- WRONG: race condition
bad from to = do
  val <- readTVarIO from  -- IO, not atomic
  atomically $ modifyTVar to (+ val)

-- CORRECT: atomic transaction
good from to = atomically $ do
  val <- readTVar from
  modifyTVar to (+ val)
  modifyTVar from (subtract val)
```

### 2. Use TVar functions in STM, not IO

```haskell
import Control.Concurrent.STM

example :: STM ()
example = do
  tv <- newTVar 0
  val <- readTVar tv
  writeTVar tv (val + 1)
```

### 3. Use retry carefully to avoid deadlock

```haskell
import Control.Concurrent.STM

-- This will deadlock if nobody writes to tv
waitUntilPositive :: TVar Int -> STM Int
waitUntilPositive tv = do
  val <- readTVar tv
  if val > 0 then return val else retry
```

### 4. Use newTVarIO for initial creation outside atomically

```haskell
import Control.Concurrent.STM

main :: IO ()
main = do
  tv <- newTVarIO 0  -- OK to create outside atomically
  atomically $ modifyTVar tv (+1)
```

### 5. Use modifyTVar' for strict updates

```haskell
import Control.Concurrent.STM

incrementStrict :: TVar Int -> STM ()
incrementStrict tv = modifyTVar' tv (+1)
```

## Examples

A thread-safe bank account:

```haskell
import Control.Concurrent.STM

type Account = TVar Int

newAccount :: Int -> IO Account
newAccount bal = newTVarIO bal

transfer :: Account -> Account -> Int -> STM ()
transfer from to amount = do
  balFrom <- readTVar from
  if balFrom >= amount
    then do
      writeTVar from (balFrom - amount)
      modifyTVar to (+ amount)
    else retry
```

## Related Errors

- [Haskell STM Error](../haskell-stm-error)
- [Haskell MVar Error](../haskell-mvar)
- [Haskell IORef Error](../haskell-ioref)
