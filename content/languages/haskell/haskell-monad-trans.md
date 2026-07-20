---
title: "[Solution] Haskell MonadTrans — Monad Transformer Stack Errors"
description: "Fix monad transformer errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1015
---

Monad transformers compose different monadic effects (state, exceptions, reading environment) into a single stack. Errors arise from using functions in the wrong monad layer, forgetting to `lift`, or misordering the transformer stack.

## Common Causes

- Calling a base monad function without `lift` in a transformed stack
- The transformer order prevents a natural operation from working
- Missing import of `Control.Monad.Trans.Class` for `lift`
- `MonadTrans` instance does not exist for a custom transformer

## How to Fix

### 1. Import the right modules

```haskell
import Control.Monad.Trans.Class (lift)
import Control.Monad.Trans.State.Strict (StateT, get, put)
import Control.Monad.Trans.Reader (ReaderT, ask)
import Control.Monad.Trans.Except (ExceptT, throwE)
```

### 2. Use `lift` to access underlying layers

```haskell
import Control.Monad.Trans.Class (lift)
import Control.Monad.Trans.State.Strict

increment :: StateT Int IO ()
increment = do
  lift (putStrLn "Incrementing")  -- IO action
  modify (+1)                      -- StateT action
```

### 3. Order transformers correctly

```haskell
-- ReaderT on top of StateT: can read AND have state
type App a = ReaderT Env (StateT St IO) a

-- StateT on top of ReaderT: state can read but reader cannot see state
type App2 a = StateT St (ReaderT Env IO) a
```

### 4. Use `liftIO` for IO in a transformer stack

```haskell
import Control.Monad.IO.Class (liftIO)

action :: StateT Int IO ()
action = do
  liftIO (putStrLn "hello")
  modify (+1)
```

### 5. Define MonadTrans for custom transformers

```haskell
import Control.Monad.Trans.Class (MonadTrans(..))

newtype MyT m a = MyT { runMyT :: m (Maybe a) }

instance MonadTrans MyT where
  lift m = MyT (fmap Just m)
```

## Examples

A complete transformer stack:

```haskell
import Control.Monad.Trans.State.Strict
import Control.Monad.Trans.Reader
import Control.Monad.Trans.Class (lift)

type App a = ReaderT Config (StateT AppState IO) a

data Config = Config { port :: Int }
data AppState = AppState { count :: Int }

handleRequest :: App ()
handleRequest = do
  cfg <- ask
  lift $ modify (\s -> s { count = count s + 1 })
  lift . lift $ putStrLn ("Server on port " ++ show (port cfg))
```

## Related Errors

- [Haskell ExceptT Error](../haskell-exceptt)
- [Haskell StateT Error](../haskell-statt)
- [Haskell ReaderT Error](../haskell-readert)
