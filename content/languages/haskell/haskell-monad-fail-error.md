---
title: "[Solution] Haskell MonadFailDesugaring Error"
description: "Fix Haskell MonadFailDesugaring errors when pattern match failures in do-notation require MonadFail."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

MonadFailDesugaring errors occur when the extension is enabled but the monad does not have a MonadFail instance.

## Common Causes

- Pattern match failure in do-notation
- Monad does not implement MonadFail
- Missing import for MonadFail
- Let pattern binding failure in do block

## How to Fix

### 1. Add MonadFail instance

```haskell
import Control.Monad.Fail

data MyMonad a = MyMonad a

instance Functor MyMonad where
  fmap f (MyMonad a) = MyMonad (f a)

instance Applicative MyMonad where
  pure = MyMonad
  (MyMonad f) <*> (MyMonad a) = MyMonad (f a)

instance Monad MyMonad where
  MyMonad a >>= f = f a

instance MonadFail MyMonad where
  fail _ = error "MonadFail"
```

### 2. Use irrefutable patterns or case

```haskell
-- Instead of:
-- do Just x <- return Nothing

-- Use:
do result <- return Nothing
   case result of
     Just x -> return x
     Nothing -> return default
```

## Examples

```haskell
import Control.Monad.Fail (MonadFail)

safeHead :: MonadFail m => [a] -> m a
safeHead [] = fail "empty list"
safeHead (x:_) = return x

main :: IO ()
main = do
  result <- safeHead [1, 2, 3]
  print result
```

## Related Errors

- [Monad error](/languages/haskell/haskell-monad-error)
- [Pattern match error](/languages/haskell/haskell-pattern-match)
- [Compile error](/languages/haskell/haskell-ghc-error)
