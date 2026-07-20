---
title: "[Solution] Haskell ReaderT — Reader Transformer Errors"
description: "Fix ReaderT monad transformer errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1019
---

`ReaderT` carries a read-only environment through a transformer stack. Errors involve using the wrong environment type, forgetting that `ReaderT` is `r -> m a`, or confusing `ReaderT` with `Reader`.

## Common Causes

- The environment type in the signature does not match the actual record type
- Using `ask` when you need `asks` to extract a field
- Forgetting to `lift` IO actions inside `ReaderT`
- Confusing `ReaderT r IO` with `IO r`

## How to Fix

### 1. Define the environment as a record

```haskell
import Control.Monad.Trans.Reader

data Env = Env
  { envPort :: Int
  , envHost :: String
  }

type App a = ReaderT Env IO a
```

### 2. Use asks to extract fields

```haskell
import Control.Monad.Trans.Reader

getPort :: ReaderT Env IO Int
getPort = asks envPort

getHost :: ReaderT Env IO String
getHost = asks envHost
```

### 3. Use withReaderT to modify the environment

```haskell
import Control.Monad.Trans.Reader

withPort :: Int -> ReaderT Env IO a -> ReaderT Env IO a
withPort p = withReaderT (\env -> env { envPort = p })
```

### 4. Run ReaderT with runReaderT

```haskell
import Control.Monad.Trans.Reader

runApp :: Env -> App a -> IO a
runApp env app = runReaderT app env
```

### 5. Combine ReaderT with StateT

```haskell
import Control.Monad.Trans.Reader
import Control.Monad.Trans.State.Strict
import Control.Monad.Trans.Class (lift)

type App a = ReaderT Env (StateT Int IO) a

example :: App ()
example = do
  port <- asks envPort
  lift $ modify (+port)
```

## Examples

A web request handler using ReaderT:

```haskell
import Control.Monad.Trans.Reader
import Control.Monad.Trans.Class (lift)

data Config = Config { maxRetries :: Int, timeout :: Int }
type Handler a = ReaderT Config IO a

fetchData :: String -> Handler String
fetchData url = do
  cfg <- ask
  lift $ putStrLn ("Fetching " ++ url ++ " (retries=" ++ show (maxRetries cfg) ++ ")")
  return "data"
```

## Related Errors

- [Haskell StateT Error](../haskell-statt)
- [Haskell ExceptT Error](../haskell-exceptt)
- [Haskell MonadTrans Error](../haskell-monad-trans)
