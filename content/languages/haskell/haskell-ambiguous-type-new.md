---
title: "[Solution] Haskell: ambiguous type variable error"
description: "Resolve Haskell ambiguous type variable errors by adding annotations and constraining polymorphic types."
languages: ["haskell"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An ambiguous type variable error in Haskell means the compiler cannot determine a unique type for a particular variable based on the available context. The error message identifies the ambiguous variable and the constraints that fail to resolve it. Haskell's type inference engine tries to deduce concrete types, but sometimes there is not enough information to narrow down a polymorphic variable to a single type. This is a compile-time error that prevents the program from building.

## Why It Happens

Ambiguous type variables arise in several situations. The most common is using a polymorphic function where the type cannot be inferred from the arguments or return type. For example, calling `read` without specifying the result type leaves the compiler unable to determine what type to parse into. Numeric literals like `42` have type `Num a => a`, and if the context does not constrain `a` to a specific numeric type, it remains ambiguous. Using overloaded functions like `mempty` without specifying the monoid type is another frequent cause. Type class functions that can return multiple types, such as `fromJust` or `toEnum`, may also be ambiguous if the result type is not constrained. Additionally, functions that take polymorphic arguments but the call site does not provide enough type information will trigger this error.

## How to Fix It

**Add explicit type annotations to resolve ambiguity:**

```haskell
-- WRONG: read is ambiguous, type unknown
-- result = read "42"

-- CORRECT: annotate the type
result :: Int
result = read "42"

-- Or use type application syntax (GHC 8+)
result = read @Int "42"
```

**Specify numeric types for literals:**

```haskell
-- WRONG: ambiguous Num constraint
-- x = 42

-- CORRECT: constrain the type
x :: Int
x = 42

x :: Double
x = 42.0
```

**Resolve ambiguous monoid or functor types:**

```haskell
-- WRONG: which Monoid?
-- x = mempty

-- CORRECT: specify the type
x :: [Int]
x = mempty  -- []

x :: String
x = mempty  -- ""
```

**Use TypeApplications extension for explicit type arguments:**

```haskell
{-# LANGUAGE TypeApplications #-}

-- Specify type directly on function application
result = read @Int "42"
result = fromList @[(Int, String)] []
```

**Add type signatures to top-level bindings:**

```haskell
-- WRONG: compiler cannot infer concrete type
-- process x = decode x

-- CORRECT: provide complete signature
process :: ByteString -> Maybe Config
process = decode
```

**Use GHCi to diagnose ambiguous types:**

```haskell
ghci> :t read "42"
read "42" :: Read a => a  -- ambiguous
ghci> :t read "42" :: Int
read "42" :: Int  -- concrete
```

## Common Mistakes

- Forgetting that `read` always needs a type annotation or context
- Assuming `fromInteger` and `fromRational` can infer their target type automatically
- Not realizing that `mempty` is polymorphic across many monoid types
- Leaving type variables unconstrained in complex expressions with multiple polymorphic functions
- Using `default` declarations to work around ambiguity instead of fixing the root cause

## Related Pages

- [Type error in Haskell](/languages/haskell/haskell-type-error-new)
- [No instance for type class in Haskell](/languages/haskell/haskell-no-instance-new)
- [Variable not in scope in Haskell](/languages/haskell/haskell-not-in-scope-new)
- [Infinite type error in Haskell](/languages/haskell/haskell-infinite-type-new)
