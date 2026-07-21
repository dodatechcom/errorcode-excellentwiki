---
title: "[Solution] Brew Cask Install Error -- Fix Cask Installation Failure"
description: "Fix brew cask install errors when installing a macOS application via Homebrew Cask fails. Check cask configuration."
tools: ["brew"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `brew install --cask <app>` failed to install a macOS application.

## Common Causes

- App requires newer macOS version
- Cask download URL is broken
- App requires Gatekeeper approval
- Disk space is insufficient

## How to Fix

### 1. Update Homebrew

```bash
brew update
brew install --cask <app>
```

### 2. Check macOS Compatibility

```bash
brew info --cask <app>
```

### 3. Allow Gatekeeper

```bash
xattr -r -d com.apple.quarantine /Applications/<App>.app
```

### 4. Install with Verbose

```bash
brew install --cask --verbose <app>
```

## Examples

```bash
$ brew install --cask firefox
Error: Cask 'firefox' requires macOS >= 12.0

$ brew info --cask firefox
# Check requirements
```
