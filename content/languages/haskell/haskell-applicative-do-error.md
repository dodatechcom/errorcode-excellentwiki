---
title: "[Solution] Haskell ApplicativeDo Error"
description: "Fix Haskell ApplicativeDo errors when using do-notation with Applicative operations."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

ApplicativeDo errors occur when the ApplicativeDo extension is not enabled or when do-notation cannot be properly desugared to Applicative.

## Common Causes

- ApplicativeDo extension not enabled
- Do block uses monadic operations that cannot be Applicative
- Missing Applicative instance for type
- Incorrect sequencing in Applicative do block

## How to Fix

### 1. Enable ApplicativeDo

```haskell
{-# LANGUAGE ApplicativeDo #-}

-- WRONG: No extension
-- result = do
--   x <- getX
--   y <- getY
--   return (x, y)

-- CORRECT
result = do
  x <- getX
  y <- getY
  pure (x, y)
```

### 2. Ensure independence of computations

```haskell
{-# LANGUAGE ApplicativeDo #-}

-- Computation y must not depend on x
getBoth :: IO (String, Int)
getBoth = do
  name <- getName
  age  <- getAge
  pure (name, age)
```

## Examples

```haskell
{-# LANGUAGE ApplicativeDo #-}

import Control.Applicative (liftA2)

paired :: IO (String, Int)
paired = do
  s <- getLine
  n <- readLn
  pure (s, n)

main :: IO ()
main = do
  (s, n) <- paired
  putStrLn $ s ++ " " ++ show n
```

## Related Errors

- [Monad error](/languages/haskell/haskell-monad-error)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
