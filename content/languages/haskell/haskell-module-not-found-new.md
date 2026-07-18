---
title: "[Solution] Haskell: could not find module error"
description: "Fix Haskell could not find module errors by installing packages and verifying cabal configuration."
languages: ["haskell"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `Could not find module` error in Haskell indicates that the GHC compiler or Cabal build system cannot locate a required module during compilation. The error message includes the module name and lists the paths it searched. This means the module is either not installed as a package, not listed as a dependency, or the module path is incorrect. This is a build-time error that prevents compilation entirely.

## Why It Happens

The most common cause is a missing package dependency. If your code imports `Data.Map` but the `containers` package is not listed in your `.cabal` file or `package.yaml`, GHC cannot find the module. Another frequent cause is misspelling the module name. Module names in Haskell are case-sensitive and must match exactly. You might also see this error when using a package that requires a specific GHC version or when the package database is in a corrupt state. Local modules that you have written yourself can also trigger this error if the module path does not match the module declaration. For example, declaring `module MyLib.Helper` but placing the file in `src/MyLib.hs` instead of `src/MyLib/Helper.hs` will cause a mismatch. Stack projects may fail if the resolver does not include the required package.

## How to Fix It

**Install the missing package:**

```bash
# Using cabal
cabal install containers

# Using stack
stack install containers

# Check available packages
cabal list map
```

**Add the dependency to your cabal file:**

```cabal
library
  build-depends:
    base >= 4.7 && < 5,
    containers >= 0.6,
    text >= 1.2
```

**Or in package.yaml (hpack format):**

```yaml
dependencies:
  - base >= 4.7 && < 5
  - containers >= 0.6
  - text >= 1.2
```

**Verify the module name matches the file path:**

```haskell
-- File: src/MyLib/Util.hs
-- CORRECT declaration:
module MyLib.Util where

-- WRONG if file is at src/MyLib.hs:
-- module MyLib.Util where
```

**Check your package database:**

```bash
ghc-pkg list
ghc-pkg check
# Rebuild if corrupted
cabal update
stack clean
```

**For Stack projects, verify the resolver includes the package:**

```yaml
# stack.yaml
resolver: lts-21.0  # ensure package exists in this snapshot
extra-deps:
  - some-package-1.0  # add if not in snapshot
```

## Common Mistakes

- Forgetting to run `cabal update` after adding new dependencies
- Using a package name instead of a module name in import statements
- Assuming all modules from a package are automatically available without importing
- Confusing the package name with the module namespace (e.g., `containers` package contains `Data.Map`)
- Not rebuilding after changing the cabal file

## Related Pages

- [Import error in Haskell](/languages/haskell/haskell-import-error-new)
- [Variable not in scope in Haskell](/languages/haskell/haskell-not-in-scope-new)
- [GHC runtime error in Haskell](/languages/haskell/haskell-ghc-error-new)
- [Parse error in Haskell](/languages/haskell/haskell-parse-error-new)
