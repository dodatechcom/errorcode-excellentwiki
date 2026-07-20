---
title: "[Solution] Haskell Couldn't Match Type — Type Equality Failure"
description: "Fix GHC 'Couldn't match type' errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["compile-time"]
severities: ["error"]
weight: 1003
---

The "Couldn't match type" error appears when two types that GHC expects to be equal turn out not to be. It always shows the two types and the context in which they were compared.

## Common Causes

- Using a newtype or type alias that hides a different underlying type
- Mixing up `String` and `Text`, or `ByteString` and `StrictByteString`
- Confusing a list type with a non-list type in a polymorphic context
- A type family or associated type reducing to an unexpected type

## How to Fix

### 1. Examine the full error message

GHC tells you exactly which two types it tried to unify:

```
Couldn't match type ‘Text’ with ‘[Char]’
Expected type: String
  Actual type: Data.Text.Text
```

### 2. Use explicit conversions

```haskell
import qualified Data.Text as T

-- WRONG
greeting :: String
greeting = T.pack "hello"

-- CORRECT
greeting :: T.Text
greeting = T.pack "hello"
-- OR
greeting :: String
greeting = T.unpack (T.pack "hello")
```

### 3. Check your imports

Different modules export types that look similar but are distinct:

```haskell
-- These are NOT the same type:
import Data.Map.Strict (Map)    -- Data.Map's Map
import Data.Map.Lazy   (Map)    -- also Data.Map, but a different module
```

### 4. Use type applications (GHC 8+)

```haskell
{-# LANGUAGE TypeApplications #-}

-- Force a specific type
show @Int 42
```

### 5. Add type signatures to narrow polymorphism

```haskell
-- WRONG: inferred as polymorphic
process x = show x

-- CORRECT: pinned to concrete types
process :: Int -> String
process x = show x
```

## Examples

A common `Couldn't match` with monad transformers:

```haskell
import Control.Monad.Reader
import Control.Monad.State

-- WRONG: StateT and ReaderT don't automatically unify
foo :: StateT Int (ReaderT Env IO) ()
foo = ask  -- ask belongs to ReaderT, not StateT

-- CORRECT: use lift
foo :: StateT Int (ReaderT Env IO) ()
foo = lift ask
```

## Related Errors

- [Haskell Type Mismatch](../haskell-type-error)
- [Haskell Ambiguous Type Variable](../haskell-ambiguous-type-var)
- [Haskell No Instance For](../haskell-no-instance-for)
