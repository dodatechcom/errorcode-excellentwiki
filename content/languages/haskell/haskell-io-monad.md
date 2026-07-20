---
title: "[Solution] Haskell IO Monad — Imperative Action Errors"
description: "Fix IO monad errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1020
---

The IO monad sequences side effects in Haskell. Errors typically involve trying to use an IO action in a pure context, or forgetting that IO values are descriptions, not results.

## Common Causes

- Using an IO action where a pure value is expected (e.g., `print` returns `IO ()`, not `String`)
- Forgetting the `do` notation or monadic bind (`>>=`)
- Trying to return an IO action without executing it
- Mismatch between IO and pure contexts in transformer stacks

## How to Fix

### 1. Use do-notation or >>= to sequence IO

```haskell
-- WRONG
main = putStrLn "hello" putStrLn "world"

-- CORRECT
main = do
  putStrLn "hello"
  putStrLn "world"
```

### 2. Extract values from IO with <- in do blocks

```haskell
main = do
  name <- getLine
  putStrLn ("Hello, " ++ name)
```

### 3. Use liftIO when in a transformer stack

```haskell
import Control.Monad.IO.Class (liftIO)

action :: StateT Int IO ()
action = do
  liftIO (putStrLn "in a transformer")
  modify (+1)
```

### 4. Do not use IO actions in pure functions

```haskell
-- WRONG: print is IO, cannot be used in a pure expression
result = print 42 + 1

-- CORRECT
main = do
  print 42
  return ()
```

### 5. Use unsafePerformIO only as a last resort

```haskell
import System.IO.Unsafe (unsafePerformIO)

-- Only when you are certain the operation is referentially transparent
globalCounter :: IORef Int
globalCounter = unsafePerformIO (newIORef 0)
{-# NOINLINE globalCounter #-}
```

## Examples

A simple file copier:

```haskell
import System.IO

main :: IO ()
main = do
  contents <- readFile "input.txt"
  writeFile "output.txt" contents
  putStrLn "Done"
```

## Related Errors

- [Haskell IO Error](../haskell-io-error)
- [Haskell ST Monad Error](../haskell-st-monad)
- [Haskell STM Error](../haskell-stm-error)
