---
title: "[Solution] Haskell Record WildCards Error"
description: "Fix Haskell RecordWildCards errors when using wildcard syntax for record construction and pattern matching."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

RecordWildCards errors occur when the extension is not enabled or when wildcard patterns do not match record field names.

## Common Causes

- RecordWildCards extension not enabled
- Field name in wildcard does not match record definition
- Shadowing issues with wildcard imported fields
- Missing fields in record construction with wildcards

## How to Fix

### 1. Enable RecordWildCards

```haskell
{-# LANGUAGE RecordWildCards #-}

data Person = Person { name :: String, age :: Int }

showPerson :: Person -> String
showPerson Person{..} = name ++ " is " ++ show age
```

### 2. Ensure field names match

```haskell
-- WRONG: Field name mismatch
data Foo = Foo { bar :: Int }
f Foo{..} = baz  -- 'baz' not in Foo

-- CORRECT
f Foo{..} = show bar
```

## Examples

```haskell
{-# LANGUAGE RecordWildCards #-}

data Config = Config { host :: String, port :: Int }

makeConfig :: Config
makeConfig = Config{ host = "localhost", port = 8080 }

describe :: Config -> String
describe Config{..} = host ++ ":" ++ show port

main :: IO ()
main = putStrLn (describe makeConfig)
```

## Related Errors

- [Record error](/languages/haskell/haskell-type-error)
- [Compile error](/languages/haskell/haskell-ghc-error)
- [Pattern match error](/languages/haskell/haskell-pattern-match)
