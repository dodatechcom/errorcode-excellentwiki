---
title: "[Solution] Brew List Formula Not Found Error Fix"
description: "Fix 'brew list formula not found' errors. List installed packages, check formula existence, and troubleshoot Homebrew."
tools: ["brew"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Brew List Formula Not Found Error Fix

The `brew list formula not found` error occurs when trying to list files for a package that is not installed, or when the formula name is misspelled.

## What This Error Means

The `brew list` command shows installed files for a package. When the specified formula is not installed or does not exist in any tapped repository, Homebrew reports this error.

A typical error:

```
Error: No such keg: /usr/local/Cellar/gcc
```

## Why It Happens

Common causes include:

- **Formula not installed** — Package was never installed or was uninstalled.
- **Typo in formula name** — Misspelled package name.
- **Wrong tap** — Formula exists in different tap.
- **Package installed differently** — Installed via cask, not formula.
- **Cellar directory missing** — Homebrew installation corrupted.

## How to Fix It

### Fix 1: List all installed packages

```bash
# RIGHT: See what is actually installed
brew list

# List formulae only (not casks)
brew list --formula

# List casks only
brew list --cask
```

### Fix 2: Search for the formula

```bash
# RIGHT: Search available formulae
brew search gcc

# Check if formula exists
brew info gcc
```

### Fix 3: Install before listing

```bash
# RIGHT: Install first
brew install gcc
brew list gcc
```

### Fix 4: Check installed location

```bash
# RIGHT: Verify installation
ls /usr/local/Cellar/
ls /opt/homebrew/Cellar/

# Check if symlinked
ls -la /usr/local/bin/ | grep gcc
```

### Fix 5: Use brew leaves for top-level packages

```bash
# RIGHT: List installed packages not dependencies
brew leaves
```

## Common Mistakes

- **Confusing cask and formula** — `brew list` shows formulae; use `brew list --cask` for casks.
- **Not tapping third-party repos** — Some formulae need `brew tap` first.
- **Forgetting that brew list shows files, not status** — Use `brew info` for status.

## Related Pages

- [Brew Install Error](/tools/brew/brew-install-error) — Installation issues
- [Brew Search Error](brew-search-error) — Search problems
- [Brew Info Error](brew-info-error) — Package info issues
