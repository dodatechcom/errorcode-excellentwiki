---
title: "[Solution] Haskell OverloadedStrings Error"
description: "Fix Haskell OverloadedStrings errors when string literals are used with non-String types."
languages: ["haskell"]
error-types: ["type-error"]
severities: ["error"]
---

OverloadedStrings errors occur when the extension is not enabled or when string literals cannot be converted to the expected type.

## Common Causes

- OverloadedStrings extension not enabled
- String literal used with type that lacks IsString instance
- Ambiguous type from string literal
- Missing import for IsString

## How to Fix

### 1. Enable OverloadedStrings

```haskell
{-# LANGUAGE OverloadedStrings #-}

import Data.Text (Text)

-- WRONG: No extension
-- greeting :: Text
-- greeting = "hello"

-- CORRECT
greeting :: Text
greeting = "hello"
```

### 2. Provide type annotation

```haskell
{-# LANGUAGE OverloadedStrings #-}

-- Ambiguous without annotation
let x = "hello" in (x :: Text, x :: ByteString)
```

## Examples

```haskell
{-# LANGUAGE OverloadedStrings #-}

import Data.Text (Text)

greet :: Text -> Text
greet name = "Hello, " <> name

main :: IO ()
main = print (greet "World")
```

## Related Errors

- [Type error](/languages/haskell/haskell-type-error)
- [No instance for](/languages/haskell/haskell-no-instance-for)
- [Compile error](/languages/haskell/haskell-ghc-error)
