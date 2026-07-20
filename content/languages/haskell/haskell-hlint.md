---
title: "[Solution] Haskell HLint — Linting and Code Suggestions"
description: "Fix hlint warnings and errors. Actionable solutions with code examples."
languages: ["haskell"]
error-types: ["style"]
severities: ["warning"]
weight: 1037
---

HLint analyzes Haskell code and suggests simplifications, style improvements, and detects common mistakes. While not compilation errors, hlint suggestions can indicate real bugs or non-idiomatic code.

## Common Causes

- Using `mapM_` when `forM_` is clearer (or vice versa)
- Using `do { x }` when `x` alone suffices
- Redundant `do`, `return`, `fmap`, or parentheses
- Using `if x then True else False` instead of just `x`

## How to Fix

### 1. Run hlint on your project

```bash
hlint src/
hlint app/
```

### 2. Apply suggested fixes automatically

```bash
hlint src/ --refactor
# or with apply-refact
hlint src/ --refactor --refactor-options="-i"
```

### 3. Suppress specific hints

```haskell
{-# HLINT ignore "Use const" #-}
{-# HLINT ignore "Redundant do" #-}
```

### 4. Configure hlint in a config file

```yaml
# .hlint.yaml
- arguments: [--color]
- group:
    name: general
    enabled: true
- warn:
    - Use fmap
    - Redundant do
- ignore:
    - Use camelCase
```

### 5. Run hlint in CI

```yaml
# In GitHub Actions
- name: HLint
  run: |
    hlint src/ --report=report.html --exit
```

## Examples

Common hlint suggestions:

```haskell
-- hlint: Use mapM_
mapM_ putStrLn xs  -- OK
forM_ xs putStrLn  -- also OK, style preference

-- hlint: Redundant do
do
  putStrLn "hello"
  return ()

-- Simplify to:
putStrLn "hello"

-- hlint: Use fromMaybe
if isJust x then fromJust x else defaultVal
-- Simplify to:
fromMaybe defaultVal x
```

## Related Errors

- [Haskell GHCid Error](../haskell-ghcid)
- [Haskell Weeder Error](../haskell-weeder)
- [Haskell Compiler Warning](../haskell-compiler-warning)
