---
title: "[Solution] Haskell Cabal Build — Build System Errors"
description: "Fix cabal build errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["build-time"]
severities: ["error"]
weight: 1033
---

Cabal is Haskell's package build system. Errors involve missing dependencies, version bounds, incorrect `.cabal` file syntax, or sandbox/environment configuration problems.

## Common Causes

- Dependency version bounds exclude the installed version
- Missing `build-depends` entries for modules you imported
- Incorrect `other-extensions` or `default-extensions` declarations
- Cabal version mismatch between the file format and installed cabal-install

## How to Fix

### 1. Update dependency bounds

```cabal
library
  build-depends: base >=4.14 && <5
                 , aeson >=1.5 && <2.3
                 , text >=1.2 && <2.2
```

### 2. Run cabal update first

```bash
cabal update
cabal build
```

### 3. Check for missing modules

```bash
# The error will tell you which module is missing
# Add the corresponding package to build-depends
```

### 4. Use cabal init to generate a proper cabal file

```bash
cabal init --non-interactive
```

### 5. Use freeze files for reproducible builds

```bash
cabal freeze
# Creates cabal.project.freeze with exact versions
```

## Examples

A complete cabal file:

```cabal
cabal-version: 2.4
name: my-app
version: 0.1.0.0
build-type: Simple

library
  exposed-modules: Lib
  build-depends: base >=4.14 && <5
  default-language: Haskell2010
  ghc-options: -Wall

executable my-app
  main-is: Main.hs
  build-depends: base >=4.14 && <5, my-app
  default-language: Haskell2010
```

## Related Errors

- [Haskell Stack Build Error](../haskell-stack-build)
- [Haskell Hackage Upload Error](../haskell-hackage)
- [Haskell Dependency Error](../haskell-dependency)
