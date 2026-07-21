---
title: "Repository Component Missing Error"
description: "APT repository does not contain required component (main, universe, etc.)"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Repository Component Missing Error

APT repository does not contain required component (main, universe, etc.)

## Common Causes

- Repository line missing component
- Component name misspelled (e.g., 'unvierse' instead of 'universe')
- Distribution release does not support requested component
- Repository only provides specific components

## How to Fix

1. Check repository format: `cat /etc/apt/sources.list`
2. Verify component name: components are main, universe, multiverse, restricted
3. Use `apt-cache showpkg <package>` to find correct repo
4. Update sources list with correct component

## Examples

```bash
# Check current sources
cat /etc/apt/sources.list

# Add universe component
sudo add-apt-repository 'deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe'

# Update and search
sudo apt-get update
apt-cache showpkg nginx
```
