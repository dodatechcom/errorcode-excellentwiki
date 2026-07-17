---
title: "[Solution] Homebrew Formula Not Found Error on Mac"
description: "Fix Homebrew errors when a formula or cask cannot be found, including 'No available formula' and 'Unknown command' errors."
platforms: ["macos"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Homebrew Formula Not Found Error on Mac

Homebrew reports "No available formula with the name", "Unknown command", or "No formula or cask found" when trying to install packages.

## What This Error Means

Homebrew formula not found errors occur when the local formula index is outdated, the package name is misspelled, the formula was removed or renamed, or the tap containing the formula is not installed.

## Common Causes

- Outdated Homebrew formula index
- Misspelled package name
- Formula removed or renamed upstream
- Required tap not installed
- Homebrew installation corrupted
- Using deprecated package names

## How to Fix

### Update Homebrew

```bash
# Update formula index
brew update

# Check for outdated packages
brew outdated
```

### Search for the Formula

```bash
# Search by name
brew search <package-name>

# Search with description
brew search --desc "<description>"

# Check if formula exists
brew info <package-name>
```

### Add Required Taps

```bash
# Add a tap
brew tap <user/repo>

# List installed taps
brew tap

# Example: add homebrew-cask
brew tap homebrew/cask
```

### Fix Renamed/Removed Formulas

```bash
# Homebrew often suggests the new name
brew install <old-name>
# Output: "No available formula... Installing as formula: <new-name>"

# Use the suggested new name
brew install <new-name>
```

### Reinstall Homebrew

```bash
# Check installation health
brew doctor

# Fix permissions
sudo chown -R $(whoami) /usr/local/bin /usr/local/lib
```

## Related Errors

- [Homebrew Dependency Error]({{< relref "/os/macos/macos-homebrew-dependency-error" >}}) — Dependency conflicts
- [Swift Package Error]({{< relref "/os/macos/macos-swift-package-error-v2" >}}) — SPM issues
- [Xcode Build Error]({{< relref "/os/macos/macos-xcode-error-v2" >}}) — Build failures
