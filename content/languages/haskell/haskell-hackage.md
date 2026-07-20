---
title: "[Solution] Haskell Hackage Upload — Package Publishing Errors"
description: "Fix hackage upload errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["build-time"]
severities: ["error"]
weight: 1036
---

Uploading packages to Hackage requires correct metadata, a proper cabal file, and successful source distribution. Errors involve missing fields, incorrect version numbers, or sdist failures.

## Common Causes

- Missing required cabal fields (description, license, maintainer, synposis)
- Version number format is invalid (must be `X.Y.Z` or similar PVP format)
- `cabal sdist` fails because of missing source files
- Authentication errors when running `cabal upload`

## How to Fix

### 1. Check all required cabal fields

```cabal
name: my-package
version: 0.1.0.0
synopsis: Short one-line description
description: Longer description
license: MIT
author: Your Name
maintainer: you@example.com
category: Web
build-type: Simple
cabal-version: >=1.10
```

### 2. Run cabal check before uploading

```bash
cabal check
# Reports any warnings or errors
```

### 3. Create the source distribution

```bash
cabal sdist
# Creates dist-newstyle/my-package-0.1.0.0.tar.gz
```

### 4. Upload with correct credentials

```bash
# Set up your Hackage account first
cabal upload dist-newstyle/my-package-0.1.0.0.tar.gz

# For testing first
cabal upload --publish dist-newstyle/my-package-0.1.0.0.tar.gz
```

### 5. Follow PVP versioning

```cabal
-- PVP: A.B.C.D
-- A.B = major version
-- C   = minor / breaking changes
-- D   = patch
version: 0.1.0.0
```

## Examples

Complete upload workflow:

```bash
# 1. Check package
cabal check

# 2. Build test suite
cabal test

# 3. Create sdist
cabal sdist

# 4. Upload
cabal upload dist-newstyle/mypackage-0.1.0.0.tar.gz

# 5. Verify on Hackage
# https://hackage.haskell.org/package/mypackage
```

## Related Errors

- [Haskell Cabal Build Error](../haskell-cabal-build)
- [Haskell Stack Build Error](../haskell-stack-build)
- [Haskell Dependency Error](../haskell-dependency)
