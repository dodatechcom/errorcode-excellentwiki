---
title: "[Solution] Haskell Template Haskell Splice Error"
description: "Fix Haskell Template Haskell splice errors when using $(...) or [||...||] quasi-quotation syntax incorrectly."
languages: ["haskell"]
error-types: ["compile-error"]
severities: ["error"]
---

Template Haskell splice errors occur when splices are incorrectly placed, the TH extension is not enabled, or spliced code contains errors.

## Common Causes

- TemplateHaskell extension not enabled
- Splice used at top level without declaration
- Spliced expression has type errors
- Missing TH library imports

## How to Fix

### 1. Enable TemplateHaskell

```haskell
{-# LANGUAGE TemplateHaskell #-}
import Language.Haskell.TH

-- WRONG: No extension
-- $(return [])

-- CORRECT
$(return [])
```

### 2. Place splices correctly

```haskell
{-# LANGUAGE TemplateHaskell #-}

import Language.Haskell.TH (lift)

-- Must be at top level or in a do block
val = $(lift (1 + 2))
```

## Examples

```haskell
{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE QuasiQuotes #-}

import Language.Haskell.TH (lift)

double :: Int -> Int
double x = x * 2

main :: IO ()
main = print $(lift (double 21))
```

## Related Errors

- [Template Haskell error](/languages/haskell/haskell-template-haskell)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Type error](/languages/haskell/haskell-type-error)
