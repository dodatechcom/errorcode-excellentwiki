---
title: "APT Auto-Remove Error"
description: "Errors occurring during automatic removal of unused packages"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# APT Auto-Remove Error

Errors occurring during automatic removal of unused packages

## Common Causes

- Package marked as manually installed but no longer needed
- Dependency package removed but dependents remain
- auto-remove wants to remove critical system packages
- Conflicting versions prevent safe removal

## How to Fix

1. Review what will be removed: `apt-get --dry-run autoremove`
2. Mark important packages as manually installed: `apt-mark manual <pkg>`
3. Use `apt-mark showmanual` to see manually installed packages
4. Check package dependencies before confirming removal

## Examples

```bash
# Preview auto-remove actions
apt-get --dry-run autoremove

# Mark a package as manually installed to prevent removal
sudo apt-mark manual linux-generic
```
