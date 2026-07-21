---
title: "[Solution] Haskell ImportQualifiedPost Error"
description: "Fix Haskell ImportQualifiedPost errors when using the post-qualified import syntax."
languages: ["haskell"]
error-types: ["syntax-error"]
severities: ["error"]
---

ImportQualifiedPost errors occur when the ImportQualifiedPost extension is not enabled or when post-qualified import syntax is incorrectly used.

## Common Causes

- ImportQualifiedPost extension not enabled
- Using post-qualified syntax without extension
- Mixing pre and post qualified syntax
- Import list conflicts with qualified names

## How to Fix

### 1. Enable ImportQualifiedPost

```haskell
{-# LANGUAGE ImportQualifiedPost #-}

-- WRONG: Pre-qualified in new style
-- import qualified Data.Map as Map

-- CORRECT: Post-qualified
import Data.Map qualified as Map
```

### 2. Use consistent import style

```haskell
{-# LANGUAGE ImportQualifiedPost #-}

import Data.Text qualified as T
import Data.Map qualified as Map
```

## Examples

```haskell
{-# LANGUAGE ImportQualifiedPost #-}

import Data.Map qualified as Map
import Data.List qualified as L

main :: IO ()
main = do
  let m = Map.fromList [(1, "one"), (2, "two")]
  print (Map.lookup 1 m)
  print (L.sort [3, 1, 2])
```

## Related Errors

- [Import error](/languages/haskell/haskell-import-error-new)
- [Not in scope](/languages/haskell/haskell-not-in-scope)
- [Compile error](/languages/haskell/haskell-ghc-error)
