---
title: "Non-Exhaustive Patterns in Haskell"
description: "Haskell warns or errors on non-exhaustive patterns that may fail at runtime"
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Non-exhaustive patterns occur when a function definition doesn't cover all possible inputs. GHC typically warns about this, and at runtime it causes a pattern match failure exception.

## Common Causes

- Function missing cases for some constructors
- Guards that don't cover all conditions
- Incomplete case expressions
- Partial functions like `head`, `tail`

## How to Fix

Add missing cases:

```haskell
-- WRONG: only handles non-empty list
safeHead (x:_) = x

-- Correct: handles both cases
safeHead (x:_) = Just x
safeHead []    = Nothing
```

Use wildcard patterns:

```haskell
describe :: Int -> String
describe n
  | n > 0     = "positive"
  | n == 0    = "zero"
  | otherwise = "negative"
```

Use total functions:

```haskell
-- WRONG: partial
-- head [1,2,3]

-- Correct: total
safeHead (x:_) = Just x
safeHead []    = Nothing
```

Enable warnings:

```bash
ghc -Wall -Werror MyModule.hs
```

## Examples

```haskell
f 1 = "one"
f 2 = "two"
-- f 3 causes pattern match failure at runtime
```

## Related Errors

- [Pattern match failure]({{< relref "/languages/haskell/pattern-match" >}})
- [Infinite type]({{< relref "/languages/haskell/infinite-loop" >}})
