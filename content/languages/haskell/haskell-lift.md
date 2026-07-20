---
title: "[Solution] Haskell lift — Lifting Actions Through Transformers"
description: "Fix lift errors in monad transformer stacks. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1016
---

The `lift` function from `MonadTrans` takes an action from an inner monad and wraps it to work in a transformer layer above it. Forgetting `lift` is one of the most common transformer errors.

## Common Causes

- Using an IO action directly in a `StateT` or `ReaderT` without `lift`
- Incorrect number of `lift` calls for deep transformer stacks
- Using `lift` when `liftIO` from `MonadIO` is needed
- Conflicting imports of `lift` from different packages

## How to Fix

### 1. Count the transformer layers and use the right number of lifts

```haskell
-- One layer: StateT over IO
doSomething :: StateT Int IO ()
doSomething = do
  lift (putStrLn "one lift")  -- correct

-- Two layers: ReaderT over StateT over IO
doSomething2 :: ReaderT Env (StateT Int IO) ()
doSomething2 = do
  lift (putStrLn "two lifts needed")  -- WRONG, only lifts through ReaderT
  lift (lift (putStrLn "correct"))     -- lifts through ReaderT then StateT
```

### 2. Use `liftIO` for cleaner IO lifting

```haskell
import Control.Monad.IO.Class (liftIO)

doSomething :: StateT Int IO ()
doSomething = do
  liftIO (putStrLn "uses liftIO, no counting needed")
  modify (+1)
```

### 3. Check for missing MonadTrans import

```haskell
-- WRONG: lift is not in scope
import Control.Monad.Trans.State.Strict (StateT)

-- CORRECT
import Control.Monad.Trans.Class (lift)
import Control.Monad.Trans.State.Strict (StateT)
```

### 4. Create helper functions to reduce boilerplate

```haskell
logMsg :: MonadIO m => String -> m ()
logMsg = liftIO . putStrLn

action :: StateT Int IO ()
action = do
  logMsg "automatic lift"
  modify (+1)
```

### 5. Use `embed` from `MonadBaseControl` for complex cases

```haskell
import Control.Monad.Trans.Control (MonadBaseControl, liftBase)

action :: StateT Int IO ()
action = liftBase (putStrLn "via liftBase")
```

## Examples

Three-level transformer stack with precise lifting:

```haskell
import Control.Monad.Trans.Class (lift)
import Control.Monad.Trans.State.Strict
import Control.Monad.Trans.Reader

type App a = ReaderT Env (StateT St IO) a

example :: App ()
example = do
  env <- ask                          -- ReaderT level
  lift $ modify (+1)                  -- lifts to StateT level
  lift $ lift $ putStrLn "at IO"      -- lifts to IO level
```

## Related Errors

- [Haskell MonadTrans Error](../haskell-monad-trans)
- [Haskell ExceptT Error](../haskell-exceptt)
- [Haskell StateT Error](../haskell-statt)
