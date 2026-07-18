---
title: "[Solution] Brew Unlink Failed Error Fix"
description: "Fix 'brew unlink failed' errors in Homebrew. Resolve symlink removal issues and package unlinking problems."
tools: ["brew"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Brew Unlink Failed Error Fix

The `brew unlink failed` error occurs when Homebrew cannot remove symlinks for a package, usually because the symlinks are missing or the package is not linked.

## What This Error Means

Unlinking removes symlinks that Homebrew created in `/usr/local/bin` (or `/opt/homebrew/bin`). When these symlinks do not exist, are already removed, or the package was installed as keg-only, unlinking fails.

A typical error:

```
Error: Could not symlink bin/gfortran
Target /usr/local/bin/gfortran is a symlink belonging to gcc
```

## Why It Happens

Common causes include:

- **Package not linked** — Trying to unlink something not linked.
- **Symlinks already removed** — Package was manually unlinked.
- **Keg-only package** — Keg-only packages are not linked by default.
- **Conflicting symlinks** — Another package owns the symlink.
- **Permission issues** — Cannot remove symlinks due to permissions.

## How to Fix It

### Fix 1: Check if package is linked

```bash
# RIGHT: Check link status
brew list --links gcc

# List all linked packages
brew list | head -20
```

### Fix 2: Force unlink

```bash
# RIGHT: Force unlink
brew unlink --force gcc

# Unlink multiple packages
brew unlink --force gcc gfortran
```

### Fix 3: Remove symlinks manually

```bash
# RIGHT: Manually remove symlinks
ls -la /usr/local/bin/ | grep gcc
sudo rm /usr/local/bin/gfortran
sudo rm /usr/local/bin/gcc
```

### Fix 4: Check keg-only status

```bash
# RIGHT: See if package is keg-only
brew info gcc | grep "keg-only"

# Keg-only packages don't need unlinking
```

### Fix 5: Reinstall after unlinking

```bash
# RIGHT: Full cycle
brew unlink gcc
brew uninstall gcc
brew install gcc
```

## Common Mistakes

- **Trying to unlink keg-only packages** — They are not linked in the first place.
- **Not checking symlink ownership** — Use `ls -la` to see who owns the link.
- **Assuming unlink removes the package** — It only removes symlinks.

## Related Pages

- [Brew Link Error](brew-link-error) — Link creation issues
- [Brew Install Error](/tools/brew/brew-install-error) — Installation problems
- [Brew Untap Error](brew-untap-error) — Tap management issues
