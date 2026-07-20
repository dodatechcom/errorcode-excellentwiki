---
title: "[Solution] Haskell Template Haskell — Metaprogramming Errors"
description: "Fix Template Haskell errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1031
---

Template Haskell enables compile-time code generation in Haskell. Errors involve staging restrictions, TH splices in wrong positions, or missing `$(...)` syntax for running expressions.

## Common Causes

- Using TH splices (`$(...)`) in a module that does not enable the extension
- Stage restriction: cannot use a value from the same stage in a splice
- TH code that generates ill-typed expressions
- Forgetting that TH runs at compile time and cannot access runtime values

## How to Fix

### 1. Enable TemplateHaskell

```haskell
{-# LANGUAGE TemplateHaskell #-}
```

### 2. Understand the stage restriction

```haskell
{-# LANGUAGE TemplateHaskell #-}
import Language.Haskell.TH

-- WRONG: x is defined in the same stage as the splice
x = 5
y = $(return (LitE (IntegerL (toInteger x))))

-- CORRECT: use a top-level splice with a TH-generated value
y = $(litE 5)
```

### 3. Use Quote for safer code generation

```haskell
{-# LANGUAGE TemplateHaskell #-}
import Language.Haskell.TH.Syntax (Q, lift)

myVal :: Q [Dec]
myVal = [d| x = 42 |]
```

### 4. Use quasiQuoters for custom syntax

```haskell
{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE QuasiQuotes #-}

import Language.Haskell.TH.Quote

json :: QuasiQuoter
json = QuasiQuoter
  { quoteExp = \s -> [e| $(litE (stringL s)) |]
  , quotePat = error "no pattern"
  , quoteType = error "no type"
  , quoteDec = error "no dec"
  }

main = print $(json "hello")
```

### 5. Debug TH with `pprint`

```haskell
{-# LANGUAGE TemplateHaskell #-}
import Language.Haskell.TH

debug :: Q ()
debug = do
  expr <- [e| 1 + 2 |]
  report True (pprint expr)
```

## Examples

Generating a Show instance with TH:

```haskell
{-# LANGUAGE TemplateHaskell #-}
import Language.Haskell.TH

data Color = Red | Green | Blue

deriveShow :: Name -> Q [Dec]
deriveShow name = do
  Info <- reify name
  -- simplified: just use the built-in
  [d| deriving Show |]
```

## Related Errors

- [Haskell QuasiQuote Error](../haskell-quasiquotes)
- [Haskell Quasiquoter Error](../haskell-quasiquoter)
- [Haskell Splice Error](../haskell-splice)
