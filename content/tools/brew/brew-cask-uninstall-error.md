---
title: "[Solution] Brew Cask Uninstall Error -- Fix Cask Removal Failure"
description: "Fix brew cask uninstall errors when removing a macOS application via Homebrew Cask fails. Force removal and cleanup."
tools: ["brew"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `brew uninstall --cask <app>` failed to remove the macOS application.

## Common Causes

- App is currently running
- Files are locked by the system
- App installed in non-standard location
- App has components in multiple locations

## How to Fix

### 1. Quit the App First

```bash
osascript -e 'quit app "<App>"'
brew uninstall --cask <app>
```

### 2. Force Uninstall

```bash
brew uninstall --cask --force <app>
```

### 3. Remove Manually

```bash
rm -rf /Applications/<App>.app
brew uninstall --cask <app>
```

### 4. Clean Up Residual Files

```bash
rm -rf ~/Library/Application\ Support/<App>
```

## Examples

```bash
$ brew uninstall --cask firefox
Error: Cask 'firefox' is running

$ osascript -e 'quit app "Firefox"'
$ brew uninstall --cask firefox
```
