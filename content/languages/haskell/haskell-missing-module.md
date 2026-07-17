---
title: "Could Not Find Module in Haskell"
description: "GHC raises module not found errors when a required module cannot be located during compilation"
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A "Could not find module" error occurs when GHC cannot locate a required module during compilation. This happens when the module is not installed, not in the search path, or the package is not listed as a dependency.

## Common Causes

- Package not installed
- Missing dependency in cabal/stack file
- Module name misspelled
- Package not in Haskell Platform
- Wrong GHC version for package

## How to Fix

Install the package:

```bash
cabal install package-name
# or
stack install package-name
```

Add to cabal file:

```cabal
build-depends:
    base >= 4.7 && < 5,
    containers,
    text
```

Add to stack.yaml extra-deps if needed:

```yaml
extra-deps:
  - package-name-1.0.0
```

Verify package is available:

```bash
ghc-pkg list | grep package-name
```

## Examples

```haskell
import Data.Text  -- Error if text package not installed
```

```text
Could not find module 'Data.Text'
Use -v to see a list of the files searched for.
```

## Related Errors

- [Not in scope]({{< relref "/languages/haskell/not-in-scope" >}})
- [Type error]({{< relref "/languages/haskell/type-error" >}})
