---
title: "[Solution] Haskell: occurs check - cannot construct the infinite type"
description: "Fix Haskell infinite type errors by understanding unification limits and recursive type constraints."
languages: ["haskell"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `Occurs check: cannot construct the infinite type` error in Haskell occurs during type unification when the compiler detects that resolving a type constraint would require constructing an infinitely nested type. For example, trying to unify type `a` with `[a]` (a list of `a`) would create an infinite type `[a]`, `[[a]]`, `[[[a]]]`, and so on. The occurs check prevents this infinite recursion, protecting against types that cannot be represented in Haskell's type system.

## Why It Happens

This error typically arises from incorrect type signatures or problematic function implementations. The most common scenario is writing a function where the return type appears to be a recursive expansion of the input type. For instance, if you write a function that should return the same type as its input but accidentally constructs a value that wraps the input in a list or tuple. Another cause is using polymorphic recursion, where a recursive call uses a different type than the original function signature allows. Operator precedence issues can also cause this error. For example, using `.` (function composition) where ` $ ` (function application) was intended, or vice versa, can lead to unexpected type unification that triggers the occurs check. Self-referential type constraints in type class instances can also produce this error.

## How to Fix It

**Review the types being unified:**

```haskell
-- WRONG: occurs check failure
-- f x = [x] ++ x
-- This tries to unify [a] with a, creating infinite type

-- CORRECT: if you want to duplicate elements
f :: a -> [a]
f x = [x, x]
```

**Check for missing type annotations:**

```haskell
-- WRONG: ambiguous recursive type
-- badFn x = if True then [x] else x
-- Occurs check: [a] and a

-- CORRECT: clarify the intended type
goodFn :: a -> [a]
goodFn x = [x]
```

**Fix operator precedence issues:**

```haskell
-- WRONG: function composition where application was intended
-- badFn f = show . f
-- if f has unexpected type, this may trigger occurs check

-- CORRECT: use parentheses or $ operator
goodFn f = show $ f
goodFn f = show (f)
```

**Use GHCi to inspect problematic types:**

```haskell
ghci> :t \x -> [x] ++ x
-- Shows the occurs check error directly
ghci> :t \x -> [x] ++ [x]
\x -> [x] ++ [x] :: [a] -> [a]  -- works fine


## Common Mistakes

- Confusing `[a]` with `a` when writing list operations
- Using `.` (composition) instead of `$` (application) in type-sensitive contexts
- Writing recursive functions that change the type structure at each recursion
- Forgetting that tuples and lists wrap types, creating new types
- Not providing type signatures for functions with complex type relationships

## Related Pages

- [Type error in Haskell](/languages/haskell/haskell-type-error-new)
- [Ambiguous type variable in Haskell](/languages/haskell/haskell-ambiguous-type-new)
- [No instance for type class in Haskell](/languages/haskell/haskell-no-instance-new)
- [Parse error in Haskell](/languages/haskell/haskell-parse-error-new)
