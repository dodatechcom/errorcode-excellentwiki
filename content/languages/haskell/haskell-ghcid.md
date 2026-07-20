---
title: "[Solution] Haskell GHCid — Fast Feedback Development"
description: "Fix ghcid errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["build-time"]
severities: ["error"]
weight: 1039
---

GHCid is a GHCi-based tool that reloads your project on every file change and displays errors. Errors involve the project not loading correctly in GHCi, cabal/stack configuration issues, or the reload loop not detecting changes.

## Common Causes

- The target specified does not match a valid module
- Cabal file has errors that prevent GHCi from loading
- File watching does not work on certain filesystems
- GHCid cannot find the right GHC or cabal-install

## How to Fix

### 1. Specify the correct target

```bash
# For a library
ghcid --command="cabal repl lib:my-lib"

# For an executable
ghcid --command="cabal repl exe:my-app"

# For a specific file
ghcid --command="cabal repl" --target="Lib"
```

### 2. Fix cabal file errors first

```bash
cabal check
cabal build
# Fix any errors before running ghcid
```

### 3. Use ghcid with Stack

```bash
ghcid --command="stack ghci"
```

### 4. Set up automatic testing

```bash
ghcid --command="cabal repl" --test=":main"
```

### 5. Use ghcid with a custom script

```bash
ghcid --command="cabal repl" --reload="src/"
```

## Examples

Basic ghcid usage:

```bash
# Watch and reload on changes
ghcid --command="cabal repl lib:my-lib"

# With test running
ghcid --command="cabal repl" --test=":main --match \".\""

# Output shows errors inline in your editor
# Fix errors in real-time as you edit
```

A ghcid setup script:

```bash
#!/bin/bash
ghcid --command="cabal repl lib:my-lib" \
      --test=":main" \
      --height=50 \
      --reload="src/"
```

## Related Errors

- [Haskell Cabal Build Error](../haskell-cabal-build)
- [Haskell Stack Build Error](../haskell-stack-build)
- [Haskell GHCi Error](../haskell-ghci)
