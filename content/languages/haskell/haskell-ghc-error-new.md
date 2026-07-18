---
title: "[Solution] Haskell: GHC runtime system error"
description: "Diagnose GHC runtime errors including stack overflows, heap exhaustion, and internal compiler crashes."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["critical"]
weight: 5
---

## What This Error Means

A GHC runtime system error occurs during program execution when the Haskell runtime encounters a condition it cannot handle. These errors include stack overflows from deep recursion, heap exhaustion from excessive memory allocation, and internal compiler errors (ICE) where GHC itself crashes. The runtime system manages memory, garbage collection, and thread scheduling, so errors at this level indicate serious issues. Error messages may include `stack overflow`, `heap exhausted`, `exception called from`, or `GHC: panic` for compiler crashes.

## Why It Happens

GHC runtime errors have diverse causes. Stack overflow occurs when recursive functions do not have proper tail-call optimization, or when recursion is genuinely too deep for the default stack size. In Haskell, lazy evaluation can sometimes cause space leaks where thunks accumulate and consume all available heap memory before being evaluated. Division by zero at runtime produces an exception. The `error` and `undefined` functions explicitly throw runtime exceptions. Pattern match failures on incomplete patterns cause exceptions. Internal compiler errors (ICE) are GHC bugs, often triggered by advanced language extensions, complex type-level programming, or specific optimization flags. Memory pressure from large data structures or retaining references to old data can also exhaust the heap.

## How to Fix It

**Fix stack overflow with proper tail recursion or accumulation:**

```haskell
-- WRONG: not tail-recursive, causes stack overflow
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- CORRECT: tail-recursive with accumulator
factorial :: Integer -> Integer
factorial n = go n 1
  where
    go 0 acc = acc
    go n acc = go (n - 1) (n * acc)
```

**Control stack size for deep recursion:**

```bash
# Increase stack size at runtime
./MyProgram +RTS -K100M -RTS

# Or compile with larger default stack
ghc -rtsopts MyFile.hs
```

**Fix space leaks by forcing strict evaluation:**

```haskell
import Data.List (foldl')

-- WRONG: lazy fold causes thunk buildup
-- sumList xs = foldl (+) 0 xs

-- CORRECT: strict fold
sumList :: [Int] -> Int
sumList xs = foldl' (+) 0 xs

-- Or use BangPatterns
{-# LANGUAGE BangPatterns #-}
sumList' :: [Int] -> Int
sumList' = go 0
  where
    go !acc [] = acc
    go !acc (x:xs) = go (acc + x) xs
```

**Handle runtime exceptions gracefully:**

```haskell
import Control.Exception (catch, SomeException)

safeDivide :: Double -> Double -> Either String Double
safeDivide x y
  | y == 0 = Left "Division by zero"
  | otherwise = Right (x / y)

-- Or use try/catch
safeRead :: String -> Either String Int
safeRead s = case reads s of
  [(n, "")] -> Right n
  _ -> Left "Parse error"
```

**Monitor memory usage:**

```bash
# Run with memory statistics
./MyProgram +RTS -s -RTS

# Set heap limit
./MyProgram +RTS -H256M -RTS


## Common Mistakes

- Using `foldl` instead of `foldl'` for strict accumulation
- Not enabling `-rtsopts` when compiling, preventing RTS flag usage
- Ignoring compiler warnings about incomplete patterns that cause runtime exceptions
- Using `error` or `undefined` as placeholder code and forgetting to replace it
- Not testing with large inputs to catch space leaks and stack overflows early

## Related Pages

- [Non-exhaustive patterns in Haskell](/languages/haskell/haskell-pattern-synonym-new)
- [Infinite type error in Haskell](/languages/haskell/haskell-infinite-type-new)
- [Type error in Haskell](/languages/haskell/haskell-type-error-new)
- [Parse error in Haskell](/languages/haskell/haskell-parse-error-new)
