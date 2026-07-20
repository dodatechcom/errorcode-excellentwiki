---
title: "[Solution] Haskell Parse Error — Syntax Failure in Source"
description: "Fix Haskell parse errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1001
---

A parse error occurs when GHC cannot make sense of your source code's syntax. The compiler stops as soon as it encounters tokens it cannot reduce according to the grammar rules, so the reported line is often the first place the parser gave up.

## Common Causes

- Missing `in` keyword after a `let` block in do-notation or expressions
- Indentation errors: GHC's layout rules require blocks to be consistently indented
- Unmatched parentheses, brackets, or braces
- Using reserved words as identifiers (e.g. `where` or `module` as a variable name)
- Tabs mixed with spaces causing unpredictable layout interpretation

## How to Fix

### 1. Check indentation consistency

GHC uses a layout rule similar to Python. Every block under `let`, `where`, `do`, or case alternatives must start in the same column or to the right of the parent:

```haskell
-- WRONG: second line is less indented
do
  let x = 1
 y = 2
    print x

-- CORRECT
do
  let x = 1
      y = 2
  print x
```

### 2. Match parentheses and brackets

A common oversight is a forgotten closing paren in a long expression:

```haskell
-- WRONG
result = filter (> 0) (map (*2) [1..10]

-- CORRECT
result = filter (> 0) (map (*2) [1..10])
```

### 3. Avoid reserved words as identifiers

Words like `where`, `let`, `in`, `case`, `of`, `do`, `module`, `import` are reserved:

```haskell
-- WRONG
where = 5

-- CORRECT
where' = 5
```

### 4. Enable helpful extensions that change syntax

Some extensions alter parsing behavior. Make sure you have a `default-extensions` stanza in your cabal file or LANGUAGE pragmas:

```haskell
{-# LANGUAGE FlexibleContexts #-}
-- This pragma itself is fine, but mismatched extensions can confuse parsers
```

### 5. Use GHC's exact error location

Read the caret (`^`) in the error output carefully. It points to the first token the parser could not consume:

```
Main.hs:12:5: error: parse error on input ‘=’
```

This means line 12, column 5 is wrong. Often the real mistake is on a preceding line.

## Examples

A typical parse error in a where-clause:

```haskell
fizzBuzz n
  | n `mod` 15 == 0 = "FizzBuzz"
  | n `mod` 3  == 0 = "Fizz"
  | n `mod` 5  == 0 = "Buzz"
  | otherwise        = show n
  where helper x = x * 2  -- WRONG: 'where' not aligned with equations above

-- CORRECT: align 'where' under the first equation
fizzBuzz n
  | n `mod` 15 == 0 = "FizzBuzz"
  | n `mod` 3  == 0 = "Fizz"
  | n `mod` 5  == 0 = "Buzz"
  | otherwise        = show n
  where
    helper x = x * 2
```

## Related Errors

- [Haskell Type Mismatch](../haskell-type-error)
- [Haskell Not In Scope](../haskell-not-in-scope)
- [Haskell Indentation Error](../haskell-indentation-error)
