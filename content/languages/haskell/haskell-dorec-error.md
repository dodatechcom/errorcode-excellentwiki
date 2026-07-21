---
title: "[Solution] Haskell DoRec Error"
description: "Fix Haskell DoRec and RecursiveDo errors when using recursive monadic bindings."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

DoRec/RecursiveDo errors occur when the RecursiveDo extension is not enabled or when recursive bindings are incorrectly formed in monadic contexts.

## Common Causes

- RecursiveDo extension not enabled
- rec block used outside do-notation
- Recursive binding does not actually require recursion
- Missing MonadFix instance for type

## How to Fix

### 1. Enable RecursiveDo

```haskell
{-# LANGUAGE RecursiveDo #-}

-- WRONG: No extension
-- rec x <- getLine; print x

-- CORRECT
rec x <- getLine
    putStrLn x
```

### 2. Ensure MonadFix instance exists

```haskell
{-# LANGUAGE RecursiveDo #-}

import Control.Monad.Fix (fix)

demo :: IO ()
demo = mdo
    ref <- newIORef 0
    let update = modifyIORef' ref (+1)
    update
    val <- readIORef ref
    print val
```

## Examples

```haskell
{-# LANGUAGE RecursiveDo #-}

fibStep :: (Int, Int) -> (Int, Int)
fibStep (a, b) = (b, a + b)

fib :: Int -> [Int]
fib n = take n $ map fst $ iterate fibStep (0, 1)

main :: IO ()
main = print (fib 10)
```

## Related Errors

- [Monad error](/languages/haskell/haskell-monad-error)
- [Type error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
