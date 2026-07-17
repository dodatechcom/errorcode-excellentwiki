---
title: "MonadFail Error in Haskell"
description: "Haskell raises MonadFail errors when pattern matching fails inside do-notation for monads"
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["monad", "fail", "do-notation", "pattern", "bind"]
weight: 5
---

## What This Error Means

A `MonadFail` error occurs when pattern matching fails inside `do`-notation for monads that implement `MonadFail`. This happens when a pattern match in a `let` or `<-` binding doesn't match the value.

## Common Causes

- Irrefutable pattern match in do block
- Using `<-` with pattern that may fail
- Missing MonadFail instance for custom monad
- Partial pattern matching in let binding

## How to Fix

Use irrefutable patterns:

```haskell
-- WRONG: may fail
do
    (x, y) <- return (1, 2)  -- works
    (a, b) <- return Nothing  -- fails

-- Correct: handle failure
do
    result <- getValue
    case result of
        Just (x, y) -> process x y
        Nothing -> handleError
```

Use case in do block:

```haskell
do
    value <- getValue
    case value of
        Just x -> process x
        Nothing -> return default
```

Implement MonadFail:

```haskell
import Control.Monad.Fail

instance MonadFail Maybe where
    fail _ = Nothing
```

## Examples

```haskell
main = do
    Just x <- return Nothing
    print x
-- Pattern match failure in a do block: Maybe is not an instance of MonadFail
```

## Related Errors

- [Pattern match failure]({{< relref "/languages/haskell/pattern-match" >}})
- [Type error]({{< relref "/languages/haskell/type-error" >}})
