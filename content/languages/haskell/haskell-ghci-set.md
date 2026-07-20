---
title: "[Solution] Haskell GHCi :set — REPL Configuration Errors"
description: "Fix GHCi :set command errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1040
---

The `:set` command in GHCi configures the REPL session. Errors involve invalid flag names, setting options that conflict with loaded modules, or using syntax that only works in `.ghci` configuration files.

## Common Causes

- Setting a GHC option that is not valid for the current GHC version
- Conflicting options (e.g., `-Wall` with `-Wno-orphans`)
- Using `:set` with options that require a module to be loaded first
- `.ghci` file syntax errors preventing GHCi from starting

## How to Fix

### 1. Check valid GHCi options

```haskell
:set +t          -- show type of result
:set +c          -- show type of evaluated result
:set prompt ">>>"
:set prompt-cont "  | "
:set editor vim   -- set editor for :edit
```

### 2. Set GHC options with :seti or :set

```haskell
:set -Wall
:set -Wno-orphans
:set -XFlexibleContexts
:set -XOverloadedStrings
```

### 3. Check your .ghci file

```bash
# ~/.ghci or .ghci in project root
:set prompt "λ> "
:set +t
:set -Wall
:set -XOverloadedStrings
```

### 4. Use :set with no args to see current settings

```haskell
:set
-- Shows all current options and language extensions
```

### 5. Reset options with -X or :unset

```haskell
:set -XOverloadedStrings
-- later
:set -XNoOverloadedStrings
```

## Examples

A productive GHCi session:

```haskell
:set +t +c
:set prompt "λ> "
:set -Wall
:set -XOverloadedStrings
:set -XScopedTypeVariables

-- Now you can use typed results and extensions
λ> :type length
length :: Foldable t => t a -> Int
λ> 1 + 2 :: Int
3
```

## Related Errors

- [Haskell GHCi Error](../haskell-ghci)
- [Haskell :type Error](../haskell-colon-type)
- [Haskell :info Error](../haskell-colon-info)
