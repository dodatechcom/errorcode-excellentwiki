---
title: "[Solution] Brew Untap Failed Not Tapped Error Fix"
description: "Fix 'brew untap failed' and 'not tapped' errors. Remove Homebrew taps and resolve tap management issues."
tools: ["brew"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Brew Untap Failed Not Tapped Error Fix

The `brew untap failed` or `not tapped` error occurs when trying to remove a tap that does not exist, has already been removed, or has dependencies.

## What This Error Means

Taps are third-party package repositories. When you try to untap (remove) a tap that is not present, or when removing a tap would break installed packages, Homebrew reports this error.

A typical error:

```
Error: No such tap: custom/tap-name
```

Or:

```
Error: refusing to untap custom/tap-name because it is still being used by:
  formula_name
```

## Why It Happens

Common causes include:

- **Tap not added** — Trying to untap something never tapped.
- **Already untapped** — Tap was already removed.
- **Installed packages depend on tap** — Packages from tap are still installed.
- **Typo in tap name** — Wrong name or namespace.
- **Built-in tap** — Cannot remove default Homebrew taps.

## How to Fix It

### Fix 1: Check if tap exists

```bash
# RIGHT: List all taps
brew tap

# Check specific tap
brew tap-info custom/tap-name
```

### Fix 2: Remove dependent packages first

```bash
# RIGHT: Uninstall packages from tap
brew untap custom/tap-name

# If packages depend on it
brew list custom/tap-name
brew uninstall $(brew list custom/tap-name)
brew untap custom/tap-name
```

### Fix 3: Force untap

```bash
# RIGHT: Force removal
brew untap --force custom/tap-name
```

### Fix 4: Remove tap directory manually

```bash
# RIGHT: Manual removal (last resort)
rm -rf /usr/local/Homebrew/Library/Taps/custom/homebrew-tap-name
rm -rf /opt/homebrew/Library/Taps/custom/homebrew-tap-name

# Or for user taps
rm -rf ~/Library/Homebrew/Taps/custom/homebrew-tap-name
```

### Fix 5: Manage taps properly

```bash
# RIGHT: See tap details
brew tap-info --installed

# See what a tap provides
brew search custom/tap-name/
```

## Common Mistakes

- **Forgetting that built-in taps cannot be removed** — homebrew/core and homebrew/cask are required.
- **Not checking what packages come from a tap** — Use `brew tap-info` first.
- **Assuming untap is the same as uninstall** — Untap removes the repository; uninstall removes packages.

## Related Pages

- [Brew Link Error](brew-link-error) — Link issues
- [Brew Install Error](/tools/brew/brew-install-error) — Installation problems
- [Brew Search Error](brew-search-error) — Search issues
