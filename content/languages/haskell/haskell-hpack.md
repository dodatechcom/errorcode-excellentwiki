---
title: "[Solution] Haskell Hpack — Package.yaml Generation Errors"
description: "Fix hpack errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["build-time"]
severities: ["error"]
weight: 1035
---

Hpack generates `.cabal` files from `package.yaml`. Errors involve incorrect YAML syntax, missing required fields, or hpack version incompatibilities with the generated cabal file format.

## Common Causes

- YAML syntax errors (indentation, missing colons, wrong types)
- Required fields like `name`, `version`, or `dependencies` are missing
- The generated `.cabal` file has syntax that the installed cabal-install cannot parse
- Hpack-specific features used without hpack installed

## How to Fix

### 1. Validate YAML syntax

```bash
# Check for YAML errors
hpack --check
```

### 2. Ensure required fields are present

```yaml
name: my-package
version: 0.1.0.0
dependencies:
  - base >= 4.14 && < 5
```

### 3. Run hpack explicitly to regenerate

```bash
hpack
# or
stack build  # Stack runs hpack automatically
```

### 4. Use conditionals for platform-specific deps

```yaml
dependencies:
  - base >= 4.14 && < 5

when:
  - condition: os(windows)
    dependencies:
      - Win32
  - condition: os(linux)
    dependencies:
      - unix
```

### 5. Pin hpack version in your project

```yaml
# In stack.yaml
hpack:
  version: 0.36.0
```

## Examples

A complete package.yaml:

```yaml
name: my-lib
version: 0.1.0.0
synopsis: A short description
description: |
  A longer description of the library.
license: MIT
author: Author Name
maintainer: author@example.com
dependencies:
  - base >= 4.14 && < 5
  - text >= 1.2 && < 2.2
library:
  source-dirs: src
  exposed-modules:
    - MyLib
  ghc-options: -Wall
```

## Related Errors

- [Haskell Cabal Build Error](../haskell-cabal-build)
- [Haskell Stack Build Error](../haskell-stack-build)
- [Haskell Package Error](../haskell-package)
