---
title: "APT Download Failed - Unmet Dependencies"
description: "Package download fails due to unsatisfiable dependency chain"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# APT Download Failed - Unmet Dependencies

Package download fails due to unsatisfiable dependency chain

## Common Causes

- Dependency requires older version already removed from repository
- Circular dependency between packages
- Package depends on software from third-party repository not enabled
- Broken package relationships after partial upgrade

## How to Fix

1. Check dependency tree: `apt-cache depends <package>`
2. Enable required repositories
3. Try `apt-get download <pkg>` to isolate download issues
4. Use `apt-cache rdepends <package>` to check reverse dependencies
5. Consider using `aptitude` for complex dependency resolution

## Examples

```bash
# Check what a package depends on
apt-cache depends nginx

# Check reverse dependencies
apt-cache rdepends nginx
```
