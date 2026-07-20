---
title: "[Solution] Haskell MVar — Mutable Variable Concurrency Errors"
description: "Fix MVar concurrency errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1024
---

`MVar` is a mutable variable that can be empty or full, providing blocking synchronization. Errors include deadlocks from mismatched `putMVar`/`takeMVar` calls, using the wrong variant (`newEmptyMVar` vs `newMVar`), or forgetting that MVar operations are in IO.

## Common Causes

- Deadlock: all threads blocked on `takeMVar` with nobody putting
- Using `putMVar` on a full MVar (blocks) or `takeMVar` on empty (blocks)
- Forgetting that `takeMVar` removes the value (unlike STM's `readTVar`)
- Race conditions from non-atomic read-modify-write sequences

## How to Fix

### 1. Balance put and take operations

```haskell
import Control.Concurrent.MVar

-- WRONG: deadlock - nobody puts
bad = do
  mv <- newEmptyMVar
  takeMVar mv  -- blocks forever

-- CORRECT
good = do
  mv <- newEmptyMVar
  putMVar mv 42
  val <- takeMVar mv
  print val
```

### 2. Use modifyMVar for atomic read-modify-write

```haskell
import Control.Concurrent.MVar

updateCounter :: MVar Int -> IO ()
updateCounter mv = modifyMVar_ mv (return . (+1))
```

### 3. Use tryTakeMVar / tryPutMVar for non-blocking operations

```haskell
import Control.Concurrent.MVar

nonBlocking :: MVar Int -> IO (Maybe Int)
nonBlocking mv = tryTakeMVar mv
```

### 4. Use newMVar when you want an initial value

```haskell
import Control.Concurrent.MVar

main = do
  mv <- newMVar 0
  val <- readMVar mv
  print val  -- 0
```

### 5. Use withMVar for read-only access

```haskell
import Control.Concurrent.MVar

printContents :: MVar [String] -> IO ()
printContents mv = withMVar mv print
```

## Examples

A thread-safe queue using MVar:

```haskell
import Control.Concurrent.MVar
import Control.Concurrent (forkIO, threadDelay)

type Queue a = MVar [a]

newQueue :: IO (Queue a)
newQueue = newMVar []

enqueue :: Queue a -> a -> IO ()
enqueue q x = modifyMVar_ q (return . (++ [x]))

dequeue :: Queue a -> IO a
dequeue q = modifyMVar q (\(x:xs) -> return (xs, x))

main :: IO ()
main = do
  q <- newQueue
  forkIO $ enqueue q "task1"
  forkIO $ enqueue q "task2"
  threadDelay 100000
  val <- dequeue q
  putStrLn val
```

## Related Errors

- [Haskell IORef Error](../haskell-ioref)
- [Haskell TVar Error](../haskell-tvar)
- [Haskell Concurrency Error](../haskell-concurrency)
