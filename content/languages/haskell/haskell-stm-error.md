---
title: "[Solution] Haskell STM — Software Transactional Memory Errors"
description: "Fix STM errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1022
---

STM (Software Transactional Memory) provides composable concurrency primitives. Errors arise from mixing IO and STM actions, using the wrong retry semantics, or attempting I/O inside an STM block.

## Common Causes

- Using `IO` actions inside `atomically` (STM blocks must be pure of IO)
- Forgetting that `retry` blocks the transaction until a TVar changes
- Using `STM` values outside `atomically` or `unsafeIOToSTM`
- Deadlock from circular TVar dependencies

## How to Fix

### 1. Never use IO inside atomically

```haskell
import Control.Concurrent.STM

-- WRONG
bad = atomically $ do
  putStrLn "hello"  -- IO action, not allowed
  return ()

-- CORRECT: use STM primitives only
good = atomically $ do
  tv <- newTVar 0
  modifyTVar tv (+1)
```

### 2. Use STM combinators for concurrency

```haskell
import Control.Concurrent.STM

transfer :: TVar Int -> TVar Int -> Int -> STM ()
transfer from to amount = do
  bal <- readTVar from
  if bal >= amount
    then do
      modifyTVar from (subtract amount)
      modifyTVar to (+ amount)
    else retry  -- wait until 'from' changes
```

### 3. Run STM with atomically

```haskell
import Control.Concurrent.STM
import Control.Concurrent (forkIO)

main = do
  account <- newTVarIO 100
  forkIO $ atomically $ modifyTVar account (+50)
  final <- readTVarIO account
  print final
```

### 4. Use TMVar and TQueue for communication

```haskell
import Control.Concurrent.STM

example :: IO ()
example = do
  q <- newTQueueIO
  atomically $ writeTQueue q "task1"
  msg <- atomically $ readTQueue q
  putStrLn msg
```

### 5. Handle exceptions with catchSTM

```haskell
import Control.Concurrent.STM
import Control.Exception (catch, SomeException)

safeTransfer :: TVar Int -> TVar Int -> Int -> IO ()
safeTransfer from to amt =
  atomically (transfer from to amt)
    `catch` \(_ :: SomeException) -> putStrLn "transfer failed"
```

## Examples

A thread-safe counter:

```haskell
import Control.Concurrent.STM
import Control.Concurrent (forkIO, threadDelay)

main :: IO ()
main = do
  counter <- newTVarIO 0
  forkIO $ atomically $ modifyTVar counter (+1)
  forkIO $ atomically $ modifyTVar counter (+1)
  threadDelay 100000
  val <- readTVarIO counter
  putStrLn ("Counter: " ++ show val)
```

## Related Errors

- [Haskell TVar Error](../haskell-tvar)
- [Haskell MVar Error](../haskell-mvar)
- [Haskell Concurrency Error](../haskell-concurrency)
