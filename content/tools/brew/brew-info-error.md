---
title: "[Solution] Brew No Formula Or Cask Found Error Fix"
description: "Fix 'No formula or cask found' errors in Homebrew. Resolve missing package issues with taps, search, and alternatives."
tools: ["brew"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Brew No Formula Or Cask Found Error Fix

The `No formula or cask found` error occurs when Homebrew cannot locate a package by the specified name, either because it does not exist, requires a tap, or is named differently.

## What This Error Means

Homebrew searches both formulae (command-line tools) and casks (GUI applications). When neither is found, you may need to add a tap, use a different name, or find an alternative.

A typical error:

```
Error: No formula or cask found for "myapp".
```

## Why It Happens

Common causes include:

- **Package not in Homebrew** — Not all software is available.
- **Wrong name** — Package has different name in Homebrew.
- **Needs tap** — Package is in third-party repository.
- **Deprecated or removed** — Package was removed from Homebrew.
- **Case sensitivity** — Package names are lowercase.

## How to Fix It

### Fix 1: Search broadly

```bash
# RIGHT: Search with different terms
brew search myapp
brew search my
brew search app

# Search with description
brew search --desc "my application"
```

### Fix 2: Try common alternatives

```bash
# RIGHT: Check common package patterns
brew search python    # python, python@3.11, python@3.10
brew search node      # node, node@18, node@16
brew search vim       # vim, neovim, macvim
```

### Fix 3: Check if it is a cask

```bash
# RIGHT: Search casks specifically
brew search --cask myapp

# List all casks
brew search --cask | grep -i myapp
```

### Fix 4: Add required taps

```bash
# RIGHT: Tap additional repos
brew tap homebrew/cask-versions
brew tap homebrew/cask-drivers
brew tap custom/tap-name
```

### Fix 5: Use brew info to verify

```bash
# RIGHT: Check package details
brew info ffmpeg

# JSON output for scripting
brew info --json=v2 ffmpeg
```

### Fix 6: Consider alternatives

```bash
# RIGHT: If not in Homebrew, check alternatives
pip install mypackage      # Python package
npm install -g mypackage   # Node package
cargo install mypackage    # Rust crate
```

## Common Mistakes

- **Not checking if it is a cask vs formula** — Use `--cask` flag.
- **Forgetting that brew search is case-sensitive** — Use lowercase.
- **Assuming all software is in Homebrew** — Check upstream directly.

## Related Pages

- [Brew Search Error](brew-search-error) — Search issues
- [Brew Info Error](brew-info-error) — Package info problems
- [Brew Install Error](/tools/brew/brew-install-error) — Installation issues
