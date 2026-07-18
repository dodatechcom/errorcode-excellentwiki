---
title: "[Solution] Haskell: parse error on input"
description: "Fix Haskell parse errors by correcting syntax, indentation, and missing keywords in code."
languages: ["haskell"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Haskell parse error occurs when the compiler encounters tokens that do not conform to the language grammar. The error message reads `parse error on input 'X'` and points to the location where parsing failed. Haskell's syntax has specific rules about keywords, operators, indentation-based layout blocks, and expression structure. Parse errors are detected before type checking, so they represent fundamental syntax problems in the source code.

## Why It Happens

Parse errors stem from a variety of syntax mistakes. Missing or extra keywords like `where`, `let`, `in`, `do`, or `of` are frequent causes. Incorrect indentation is particularly common in Haskell because it uses significant whitespace for defining code blocks. A `where` clause or `let` block must be indented further than the enclosing declaration. Mismatched parentheses, brackets, or braces will also cause parse errors. Using reserved words as variable names (such as `data`, `type`, `class`, or `import` as identifiers) triggers this error. Missing `=` signs in declarations, using `==` where `=` was intended, or omitting the `then` keyword in an `if` expression are other typical causes. The `$` operator used in unexpected positions or incorrect operator fixity declarations can also produce parse errors.

## How to Fix It

**Fix indentation issues in where and let blocks:**

```haskell
-- WRONG: where clause not indented enough
-- f x = x + y
-- where
-- y = 10

-- CORRECT: where clause indented past the equation
f x = x + y
  where
    y = 10
```

**Add missing keywords:**

```haskell
-- WRONG: missing 'then' keyword
-- f x = if x > 0 "positive" "negative"

-- CORRECT:
f x = if x > 0 then "positive" else "negative"
```

**Fix do-notation syntax:**

```haskell
-- WRONG: missing 'do' keyword
-- main = putStrLn "hello"
--         name <- getLine

-- CORRECT: use 'do' for monadic sequencing
main = do
  putStrLn "hello"
  name <- getLine
  putStrLn name
```

**Correct parentheses and operator usage:**

```haskell
-- WRONG: missing closing parenthesis
-- result = (1 + 2 * 3

-- CORRECT:
result = (1 + 2) * 3
result = 1 + (2 * 3)
```

**Avoid using reserved words as identifiers:**

```haskell
-- WRONG: 'data' is a reserved word
-- data = 42

-- CORRECT: use a different name
myData = 42
```

**Fix list and tuple syntax:**

```haskell
-- WRONG: mismatched brackets
-- xs = [1, 2, 3)

-- CORRECT:
xs = [1, 2, 3]
xs = (1, 2, 3)  -- tuple
```

## Common Mistakes

- Forgetting that Haskell uses layout rules instead of explicit braces (though braces are optional)
- Using `=` instead of `==` in boolean expressions within if-then-else
- Missing `in` keyword after `let` expressions outside of `do` blocks
- Indenting case alternatives inconsistently
- Writing multi-line strings without proper line continuation

## Related Pages

- [Type error in Haskell](/languages/haskell/haskell-type-error-new)
- [Variable not in scope in Haskell](/languages/haskell/haskell-not-in-scope-new)
- [Import error in Haskell](/languages/haskell/haskell-import-error-new)
- [GHC runtime error in Haskell](/languages/haskell/haskell-ghc-error-new)
