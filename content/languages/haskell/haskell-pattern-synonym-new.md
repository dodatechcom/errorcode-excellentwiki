---
title: "[Solution] Haskell: non-exhaustive patterns in function"
description: "Fix Haskell non-exhaustive pattern errors by adding missing cases and using catch-all patterns."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A non-exhaustive patterns error in Haskell means that a function or pattern match does not handle all possible cases for a given type. At runtime, when a value is encountered that no pattern matches, the program crashes with a `Pattern match failure` exception. Unlike many languages, Haskell requires you to consider every variant of a data type when writing pattern matching functions. The compiler warns about non-exhaustive patterns with `-Wall`, but the error only manifests at runtime if the unmatched case is actually reached.

## Why It Happens

This error occurs when a function defined by pattern matching omits one or more cases. For example, a function that pattern matches on `Just x` but not on `Nothing` for a `Maybe a` value will crash when given `Nothing`. Similarly, a function that handles only positive integers but not zero or negative values will fail on those inputs. Incomplete list pattern matching is another common source: matching `[x, y]` but not `[]` or `[x]`. Using `head` or `tail` on empty lists is a well-known example of non-exhaustive patterns in library functions. Case expressions that do not include a catch-all pattern are also vulnerable. Record pattern matching that omits fields can trigger this error as well.

## How to Fix It

**Add all missing pattern cases:**

```haskell
-- WRONG: only handles Just
safeDivide :: Double -> Double -> Maybe Double
safeDivide _ 0 = Nothing
safeDivide x y = Just (x / y)

-- Actually this is correct. WRONG would be:
-- safeDivide x y = Just (x / y)  -- ignores divide by zero
```

**Use a catch-all pattern:**

```haskell
-- WRONG: no catch-all for unexpected values
describe :: Int -> String
describe 1 = "one"
describe 2 = "two"

-- CORRECT: add catch-all
describe :: Int -> String
describe 1 = "one"
describe 2 = "two"
describe _ = "something else"
```

**Handle Maybe and Either completely:**

```haskell
-- WRONG: partial function
fromMaybe :: Maybe a -> a
fromMaybe (Just x) = x
-- Missing Nothing case!

-- CORRECT: provide default
fromMaybe :: a -> Maybe a -> a
fromMaybe def Nothing = def
fromMaybe _ (Just x) = x
```

**Handle all list patterns:**

```haskell
-- WRONG: assumes non-empty list
secondElement :: [a] -> a
secondElement (x:y:_) = y

-- CORRECT: handle all cases
secondElement :: [a] -> Maybe a
secondElement (_:y:_) = Just y
secondElement _ = Nothing
```

**Enable compiler warnings to catch issues early:**

```bash
ghc -Wall -Werror MyFile.hs
# -Wall enables all warnings including non-exhaustive patterns
# -Werror turns warnings into errors
```

**Use GHCi to test edge cases:**

```haskell
ghci> :t \f -> case f of { 1 -> "one"; 2 -> "two" }
-- Warning: non-exhaustive patterns
ghci> (\f -> case f of { 1 -> "one"; 2 -> "two"; _ -> "other" }) 3
"other"
```

## Common Mistakes

- Relying on `head`, `tail`, or `(!!)` without checking for empty lists
- Forgetting that `Bool` has two constructors: `True` and `False`
- Not handling the `Nothing` case for `Maybe` values
- Using incomplete case expressions in interactive GHCi sessions where errors are less visible
- Assuming compiler warnings are not important and ignoring `-Wall` output

## Related Pages

- [Type error in Haskell](/languages/haskell/haskell-type-error-new)
- [Infinite type error in Haskell](/languages/haskell/haskell-infinite-type-new)
- [GHC runtime error in Haskell](/languages/haskell/haskell-ghc-error-new)
- [Variable not in scope in Haskell](/languages/haskell/haskell-not-in-scope-new)
