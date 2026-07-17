---
title: "[Solution] Haskell Could Not Find Module"
description: "Fix Haskell module not found errors. Check package dependencies, import paths, and build configuration."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The error `Could not find module X` occurs when GHC cannot locate a required module during compilation. This can mean the module is not installed, not in the search path, or not listed as a dependency.

## Common Causes

- Package not installed
- Missing dependency in .cabal or package.yaml
- Module not in exposed-modules
- Wrong import path
- Package version mismatch

## How to Fix

```haskell
-- WRONG: Module not in dependencies
import Data.Aeson (decode)  -- Fails if aeson not in .cabal

-- CORRECT: Add to .cabal file
-- build-depends: base >= 4.7 && < 5, aeson

-- Or for stack, add to package.yaml:
-- dependencies:
--   - aeson
```

```haskell
-- WRONG: Importing private module
import Data.Aeson.Internal  -- May not be exposed

-- CORRECT: Use public API
import Data.Aeson (decode, encode)
```

```haskell
-- WRONG: Wrong module path
import qualified Data.Map.Strict as M  -- Works
import qualified Data.Map as Map       -- Also works but different

-- CORRECT: Check package documentation for correct import
-- Data.Map vs Data.Map.Strict - choose one consistently
```

## Examples

```haskell
-- Example 1: Check installed packages
-- ghc-pkg list
-- stack ls dependencies

-- Example 2: Install missing package
-- cabal install aeson
-- stack build --install-deps

-- Example 3: .cabal file structure
-- myproject.cabal:
--   exposed-modules:
--     MyModule
--   build-depends:
--     base >= 4.7 && < 5,
--     containers,
--     aeson

-- Example 4: Module search paths
-- ghc -v2  -- Shows search paths
-- -i path1:path2  -- Add to search path
```

## Related Errors

- [haskell-not-in-scope]({{< relref "/languages/haskell/haskell-not-in-scope" >}}) — variable not in scope
- [haskell-type-error]({{< relref "/languages/haskell/haskell-type-error" >}}) — type error
- [haskell-io-error]({{< relref "/languages/haskell/haskell-io-error" >}}) — IO error
