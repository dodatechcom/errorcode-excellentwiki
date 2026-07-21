---
title: "[Solution] Haskell NamedFieldPuns Error"
description: "Fix Haskell NamedFieldPuns errors when using record field names as variable bindings in patterns."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

NamedFieldPuns errors occur when the extension is not enabled or when field names do not match the record definition.

## Common Causes

- NamedFieldPuns extension not enabled
- Field name used in pattern does not exist in record
- Ambiguous field names from multiple records
- Missing fields in NamedFieldPuns pattern

## How to Fix

### 1. Enable NamedFieldPuns

```haskell
{-# LANGUAGE NamedFieldPuns #-}

data Person = Person { name :: String, age :: Int }

greet :: Person -> String
greet Person{name, age} = "Hello " ++ name ++ ", age " ++ show age
```

### 2. Ensure field names match record

```haskell
-- WRONG: Field not in record
data Foo = Foo { bar :: Int }
f Foo{baz} = baz  -- 'baz' not in Foo

-- CORRECT
f Foo{bar} = bar
```

## Examples

```haskell
{-# LANGUAGE NamedFieldPuns #-}

data Config = Config { host :: String, port :: Int }

describe :: Config -> String
describe Config{host, port} = host ++ ":" ++ show port

main :: IO ()
main = print (describe (Config "localhost" 8080))
```

## Related Errors

- [RecordWildCards error](/languages/haskell/haskell-record-wildcards-error)
- [Record error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
