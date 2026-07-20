---
title: "[Solution] Haskell StateT — State Transformer Errors"
description: "Fix StateT monad transformer errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1018
---

`StateT` adds mutable state to a monad transformer stack. Errors typically involve mixing strict and lazy variants, forgetting that `StateT` is a newtype, or using state functions in the wrong transformer layer.

## Common Causes

- Mixing `Control.Monad.Trans.State.Strict` and `Control.Monad.Trans.State.Lazy` in the same project
- Using `State` instead of `StateT` when you need IO at the bottom
- Forgetting to use `lift` when performing IO inside StateT
- The state type does not match between `get`/`put` and the type signature

## How to Fix

### 1. Pick one variant (strict or lazy) consistently

```haskell
-- Prefer strict for production code
import Control.Monad.Trans.State.Strict

-- Lazy is fine for prototyping
import Control.Monad.Trans.State.Lazy
```

### 2. Define the state type clearly

```haskell
import Control.Monad.Trans.State.Strict

data AppState = AppState
  { count :: Int
  , items :: [String]
  }

example :: StateT AppState IO ()
example = do
  st <- get
  put (st { count = count st + 1 })
  lift $ putStrLn "updated"
```

### 3. Use modify' for strict updates

```haskell
import Control.Monad.Trans.State.Strict
import Control.Monad.Trans.Class (lift)

example :: StateT Int IO ()
example = do
  modify' (+1)  -- strict, avoids space leaks
  n <- get
  lift $ print n
```

### 4. Run the StateT to extract the result

```haskell
import Control.Monad.Trans.State.Strict

runDemo :: IO (Int, Int)
runDemo = runStateT computation 0
  where
    computation = do
      modify (+10)
      get

-- Returns (10, 10): (final value, final state)
```

### 5. Use evalStateT / execStateT for convenience

```haskell
import Control.Monad.Trans.State.Strict

result :: IO Int
result = evalStateT computation 0  -- returns just the value

finalState :: IO Int
finalState = execStateT computation 0  -- returns just the state
```

## Examples

A counting state with IO:

```haskell
import Control.Monad.Trans.State.Strict
import Control.Monad.Trans.Class (lift)

type Counter = StateT Int IO

increment :: Counter ()
increment = modify' (+1)

logCount :: Counter ()
logCount = do
  n <- get
  lift $ putStrLn ("Count is: " ++ show n)

runCounter :: IO ()
runCounter = do
  (_, final) <- runStateT (increment >> logCount >> increment >> logCount) 0
  putStrLn ("Final: " ++ show final)
```

## Related Errors

- [Haskell ReaderT Error](../haskell-readert)
- [Haskell ExceptT Error](../haskell-exceptt)
- [Haskell MonadTrans Error](../haskell-monad-trans)
