---
title: "[Solution] Haskell Type Error Couldn't Match Types"
description: "Fix Haskell type mismatch errors when the compiler can't unify different types. Understand type inference and type annotations."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A type error in Haskell occurs when the compiler finds two types that don't match and cannot be unified. Haskell's strong static type system catches these at compile time.

## Common Causes

- Mixing incompatible types (e.g., String and Int)
- Incorrect type annotations
- Polymorphic functions with ambiguous types
- Missing type class instances
- Wrong function signature

## How to Fix

```haskell
-- WRONG: Mixing String and Int
greet :: String -> String
greet name = "Hello, " ++ name
greet 42  -- Type error: Int is not String

-- CORRECT: Ensure correct types
greet :: String -> String
greet name = "Hello, " ++ name
greet "Alice"  -- Works
```

```haskell
-- WRONG: Incorrect type annotation
add :: Int -> Int -> Int
add x y = x ++ y  -- Type error: (++) needs lists, not Int

-- CORRECT: Match annotation to implementation
add :: [Int] -> [Int] -> [Int]
add x y = x ++ y
-- Or: add x y = x + y  with Int -> Int -> Int
```

```haskell
-- WRONG: Ambiguous type variable
show read "42"  -- Type ambiguous: what type to read?

-- CORRECT: Add type annotation
show (read "42" :: Int)  -- "42"
```

## Examples

```haskell
-- Example 1: Type annotation helps inference
sumList :: [Int] -> Int
sumList = foldl (+) 0

-- Example 2: Type class constraints
safeHead :: [a] -> Maybe a
safeHead [] = Nothing
safeHead (x:_) = Just x

-- Example 3: Polymorphic function
identity :: a -> a
identity x = x

-- Works with any type
result1 = identity 42       -- Int
result2 = identity "hello"  -- String
```

## Related Errors

- [haskell-ambiguous-type]({{< relref "/languages/haskell/haskell-ambiguous-type" >}}) — ambiguous type
- [haskell-infinite-type]({{< relref "/languages/haskell/haskell-infinite-type" >}}) — infinite type
- [haskell-pattern-match]({{< relref "/languages/haskell/haskell-pattern-match" >}}) — pattern match
