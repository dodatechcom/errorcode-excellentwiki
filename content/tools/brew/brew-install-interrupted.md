---
title: "[Solution] Brew Install Interrupted -- Fix Interrupted Installation"
description: "Fix brew install interrupted errors when an installation was stopped midway. Clean up and reinstall."
tools: ["brew"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means a previous `brew install` was interrupted (Ctrl+C, power loss, etc.) leaving partial files.

## Common Causes

- User pressed Ctrl+C during install
- System shutdown during installation
- SSH session disconnected
- OOM killer terminated the process

## How to Fix

### 1. Clean Up

```bash
brew cleanup
```

### 2. Force Reinstall

```bash
brew reinstall <formula>
```

### 3. Remove and Install Again

```bash
brew uninstall <formula>
brew install <formula>
```

### 4. Check for Partial Files

```bash
ls /usr/local/Cellar/<formula>/
```

## Examples

```bash
$ brew install wget
^CError: Interrupted

$ brew cleanup
$ brew install wget
```
