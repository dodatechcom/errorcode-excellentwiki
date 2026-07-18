---
title: "[Solution] Haskell: type error - could not match expected type with actual type"
description: "Fix Haskell type errors by aligning expected and actual types with annotations and signatures."
languages: ["haskell"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Haskell type error occurs when the compiler finds a mismatch between the type it expects and the type it actually encounters. Haskell uses a powerful static type system with type inference, meaning types are deduced automatically. When two expressions that should share the same type do not, the compiler emits an error like `Couldn't match expected type 'X' with actual type 'Y'`. This is one of the most common compile-time errors in Haskell and is usually straightforward to resolve once you understand the type relationships in your code.

## Why It Happens

Type errors typically arise from several situations. You may be passing an argument of the wrong type to a function. For example, passing a `String` where an `Int` is expected. Another common cause is forgetting that numeric literals are polymorphic in Haskell. The literal `42` has type `Num a => a`, not `Int`, so it can cause mismatches if the context expects a concrete type. Mixing different numeric types like `Int` and `Double` without explicit conversion is also a frequent culprit. Polymorphic functions may fail to unify when their type variables are constrained in incompatible ways. Additionally, using the wrong operator for a given type, such as applying string concatenation to integers, triggers this error.

## How to Fix It

**Add explicit type annotations** to resolve ambiguity:

```haskell
-- WRONG: ambiguous numeric type
x = 42 + 3.14

-- CORRECT: annotate both values
x = (42 :: Int) + (3 :: Int)
y = (42 :: Double) + 3.14
```

**Use type signatures on functions** to clarify intent:

```haskell
-- WRONG: inferred type may not match your expectation
add x y = x + y

-- CORRECT: explicit signature
add :: Int -> Int -> Int
add x y = x + y
```

**Convert between numeric types explicitly:**

```haskell
-- WRONG: mixing Int and Double
result = (5 :: Int) + (3.2 :: Double)

-- CORRECT: convert first
result = fromIntegral (5 :: Int) + (3.2 :: Double)
```

**Fix type class mismatches by adding constraints:**

```haskell
-- WRONG: Show constraint missing for custom type
-- printMyValue x = print x

-- CORRECT: add Show constraint
printMyValue :: Show a => a -> IO ()
printMyValue x = print x
```

**Use the `:t` command in GHCi** to inspect types interactively:

```haskell
ghci> :t 'a'
'a' :: Char
ghci> :t "hello"
"hello" :: [Char]
```

## Common Mistakes

- Assuming numeric literals are always `Int` or `Double`
- Forgetting that `[Char]` and `String` are the same type
- Not realizing that `read` returns a polymorphic type and needs annotation
- Mixing up `Maybe a` with `a` without unwrapping with pattern matching
- Ignoring that list operations require elements of the same type

## Related Pages

- [Ambiguous type variable in Haskell](/languages/haskell/haskell-ambiguous-type-new)
- [Variable not in scope in Haskell](/languages/haskell/haskell-not-in-scope-new)
- [No instance for Show in Haskell](/languages/haskell/haskell-no-instance-new)
- [Infinite type error in Haskell](/languages/haskell/haskell-infinite-type-new)
