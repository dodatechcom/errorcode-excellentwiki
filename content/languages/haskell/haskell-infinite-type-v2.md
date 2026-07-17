---
title: "[Solution] Haskell Infinite Type Occurs Check"
description: "Fix Haskell infinite type errors when the occurs check fails. Understand recursive types and type variable constraints."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An infinite type error occurs when the Haskell compiler detects that a type variable would need to be infinitely recursive to satisfy a constraint. This happens when a type occurs inside itself.

## Common Causes

- Accidentally making a list contain itself
- Incorrect type annotation forcing infinite recursion
- Unifying a type variable with a type containing that variable
- Circular type definitions

## How to Fix

```haskell
-- WRONG: Trying to put a list inside itself
f :: [a] -> [a]
f x = x : x  -- Error: infinite type a ~ [a]

-- CORRECT: Use nested list type
f :: [[a]] -> [[a]]
f xs = xs ++ xs
-- Or: f xs = concat [xs, xs]
```

```haskell
-- WRONG: Incorrect type for recursive structure
data Tree a = Node a (Tree a) | Leaf

-- WRONG annotation
flatten :: Tree a -> a  -- Error: infinite type

-- CORRECT: Return list
flatten :: Tree a -> [a]
flatten Leaf = []
flatten (Node x left) = x : flatten left
```

```haskell
-- WRONG: Accidental self-reference
let x = x in x  -- Infinite type

-- CORRECT: Use fixed-point combinator if needed
import Data.Function (fix)
let x = const 5 in x  -- Or: fix (const 5)
```

## Examples

```haskell
-- Example 1: Common infinite type mistake
-- WRONG: bad = id bad  -- Would loop, type is OK but runtime hangs

-- Example 2: Correct recursive type
data Nat = Zero | Succ Nat

add :: Nat -> Nat -> Nat
add Zero n     = n
add (Succ m) n = Succ (add m n)

-- Example 3: Finite recursion is fine
countDown :: Int -> [Int]
countDown 0 = [0]
countDown n = n : countDown (n - 1)
```

## Related Errors

- [haskell-type-error]({{< relref "/languages/haskell/haskell-type-error" >}}) — type mismatch
- [haskell-ambiguous-type]({{< relref "/languages/haskell/haskell-ambiguous-type" >}}) — ambiguous type
- [haskell-pattern-match]({{< relref "/languages/haskell/haskell-pattern-match" >}}) — pattern match
