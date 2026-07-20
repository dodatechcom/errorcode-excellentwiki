---
title: "[Solution] Haskell QuasiQuotes — Custom Syntax Errors"
description: "Fix quasiquoter errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1032
---

QuasiQuoters let you embed custom syntax in Haskell source code. Errors involve using the `{-# LANGUAGE QuasiQuotes #-}` extension incorrectly, QQ functions returning the wrong quote type, or bracket syntax `[quoter| ... |]` not matching the quoter's definition.

## Common Causes

- Missing `QuasiQuotes` extension
- The quoter function returns the wrong quote type (e.g. `quoteExp` instead of `quotePat`)
- Malformed bracket syntax or unbalanced `|]` delimiters
- Using a quoter in a position it does not support (e.g. expression quoter in a type slot)

## How to Fix

### 1. Enable the extension

```haskell
{-# LANGUAGE QuasiQuotes #-}
```

### 2. Define quoters with all four quote functions

```haskell
import Language.Haskell.TH.Quote

myQQ :: QuasiQuoter
myQQ = QuasiQuoter
  { quoteExp  = \s -> [e| $(litE (stringL s)) |]
  , quotePat  = \s -> [p| $(litP (stringP s)) |]  -- or error
  , quoteType = error "type quoting not supported"
  , quoteDec  = error "declaration quoting not supported"
  }
```

### 3. Use the correct bracket syntax

```haskell
-- Expression quoter
result = $(myQQ "hello")

-- Pattern quoter
case val of
  $(myQQ pat) -> "matched"
```

### 4. Import the right modules

```haskell
import Language.Haskell.TH.Quote (QuasiQuoter(..))
import Language.Haskell.TH.Syntax (Q, Lift(..))
```

### 5. Use existing quasiquoters from libraries

```haskell
-- text-qq
{-# LANGUAGE QuasiQuotes #-}
import Text.QQ (text)

greeting :: String
greeting = [text|Hello, World!|]
```

## Examples

A JSON quasiquoter:

```haskell
{-# LANGUAGE QuasiQuotes #-}
{-# LANGUAGE TemplateHaskell #-}

import Language.Haskell.TH.Quote
import Language.Haskell.TH.Syntax (Q, lift)

json :: QuasiQuoter
json = QuasiQuoter
  { quoteExp = \s -> [e| $(lift s) |]
  , quotePat = error "not supported"
  , quoteType = error "not supported"
  , quoteDec = error "not supported"
  }

main = print $(json "{\"key\": \"value\"}")
```

## Related Errors

- [Haskell Template Haskell Error](../haskell-template-haskell)
- [Haskell Splice Error](../haskell-splice)
- [Haskell QQ Error](../haskell-qq-error)
