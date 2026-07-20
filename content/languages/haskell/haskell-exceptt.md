---
title: "[Solution] Haskell ExceptT — Exception Transformer Errors"
description: "Fix ExceptT monad transformer errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1017
---

`ExceptT` (from `transformers`) is a monad transformer that adds typed exception handling to a base monad. Errors involve using the wrong error type, forgetting to `throwE` or `catchE`, or confusing `ExceptT` with `ErrorT`.

## Common Causes

- `ExceptT` replaced `ErrorT` in `transformers` 0.3+; using `ErrorT` triggers deprecation
- The error type parameter does not match between `throwE` and `catchE`
- Not unwrapping `ExceptT` before using IO actions directly
- Using `EitherT` from a different package instead of `ExceptT`

## How to Fix

### 1. Use ExceptT, not ErrorT

```haskell
import Control.Monad.Trans.Except (ExceptT, throwE, runExceptT)

type AppError = ExceptT String IO

failAction :: AppError ()
failAction = throwE "something went wrong"
```

### 2. Match error types in throwE and catchE

```haskell
import Control.Monad.Trans.Except

example :: ExceptT String IO ()
example = do
  result <- catchE failingAction handler
  liftIO $ print result
  where
    failingAction = throwE "error" :: ExceptT String IO ()
    handler msg = do
      liftIO $ putStrLn ("Caught: " ++ msg)
      return ()
```

### 3. Run the ExceptT to get the Either result

```haskell
import Control.Monad.Trans.Except

run :: IO (Either String Int)
run = runExceptT $ do
  x <- return 42
  if x > 0
    then return x
    else throwE "must be positive"
```

### 4. Use MonadError from mtl for cleaner code

```haskell
import Control.Monad.Except (MonadError, throwError, catchError)

example :: MonadError String m => m Int
example = do
  x <- return 42
  if x > 0 then return x else throwError "bad"
```

### 5. Combine ExceptT with other transformers

```haskell
import Control.Monad.Trans.Except
import Control.Monad.Trans.State.Strict

type App a = ExceptT String (StateT Int IO) a

modifyOrThrow :: App ()
modifyOrThrow = do
  lift $ modify (+1)
  val <- lift get
  when (val > 100) $ throwE "overflow"
```

## Examples

A file-reading function with ExceptT:

```haskell
import Control.Monad.Trans.Except
import Control.Monad.Trans.Class (lift)
import System.IO

readFileE :: FilePath -> ExceptT String IO String
readFileE path = do
  exists <- lift $ doesFileExist path
  if not exists
    then throwE ("File not found: " ++ path)
    else lift $ readFile path
```

## Related Errors

- [Haskell StateT Error](../haskell-statt)
- [Haskell ReaderT Error](../haskell-readert)
- [Haskell MonadTrans Error](../haskell-monad-trans)
