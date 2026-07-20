---
title: "[Solution] Haskell Stack Build — Stack Tool Errors"
description: "Fix stack build errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["build-time"]
severities: ["error"]
weight: 1034
---

Stack is a Haskell build tool that manages GHC versions and dependencies via Stackage snapshots. Errors involve resolver mismatches, missing snapshots, or conflicts between system GHC and Stack's managed GHC.

## Common Causes

- Stackage snapshot does not include a required package version
- Resolver is too old for a dependency's requirements
- System GHC version conflicts with Stack's configuration
- Missing `stack.yaml` or `package.yaml` / `.cabal` file

## How to Fix

### 1. Update the resolver to a newer snapshot

```yaml
# stack.yaml
resolver: lts-21.25  # or the latest
```

### 2. Use extra-deps for packages not in the snapshot

```yaml
# stack.yaml
extra-deps:
  - some-package-1.2.3
```

### 3. Let Stack install GHC automatically

```bash
stack setup
# Installs the correct GHC version for the resolver
```

### 4. Check package compatibility with Stackage

```bash
# Search for a package in the current snapshot
stack ls dependencies | grep packagename
```

### 5. Use stack clean to fix stale builds

```bash
stack clean
stack build
```

## Examples

A typical stack.yaml:

```yaml
resolver: lts-21.25
packages:
  - .
extra-deps:
  - some-unlisted-package-0.1.0
```

A package.yaml:

```yaml
name: my-app
version: 0.1.0.0
dependencies:
  - base >=4.14 && <5
  - aeson
library:
  source-dirs: src
executables:
  my-app:
    main: Main.hs
    source-dirs: app
```

## Related Errors

- [Haskell Cabal Build Error](../haskell-cabal-build)
- [Haskell Hpack Error](../haskell-hpack)
- [Haskell Dependency Error](../haskell-dependency)
