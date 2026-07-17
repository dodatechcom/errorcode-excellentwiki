---
title: "[Solution] npm Lifecycle Script Error"
description: "Fix npm lifecycle script error. Resolve issues with preinstall, postinstall, and other lifecycle scripts."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm Lifecycle Script Error — lifecycle script failed

Lifecycle script errors occur when scripts defined in `package.json` (like `preinstall`, `postinstall`, `prepare`) fail during `npm install` or `npm publish`.

## Common Causes

- Script references a command not installed globally
- Missing build tools (node-gyp, python, make)
- Script has syntax errors
- Permission issues running scripts

## How to Fix

### Check Which Script Failed

```bash
npm install --verbose
```

### Skip Lifecycle Scripts Temporarily

```bash
npm install --ignore-scripts
```

### Rebuild Native Modules

```bash
npm rebuild
```

### Install Missing Build Tools

```bash
# Ubuntu/Debian
sudo apt-get install build-essential python3

# macOS
xcode-select --install
```

### Check Script in package.json

```json
{
  "scripts": {
    "postinstall": "node scripts/setup.js"
  }
}
```

### Use --ignore-scripts Flag

```bash
npm install --ignore-scripts
node scripts/setup.js  # Run manually
```

## Examples

```bash
# Example 1: Missing build tools
npm install
# gyp ERR! build error
# Fix: sudo apt-get install build-essential python3

# Example 2: Script not found
npm install
# sh: 1: scripts/postinstall.sh: not found
# Fix: verify script path in package.json

# Example 3: Skip scripts temporarily
npm install --ignore-scripts
npm rebuild
```

## Related Errors

- [Lifecycle Error]({{< relref "/tools/npm/lifecycle-error" >}}) — script execution failure
- [Cache Error]({{< relref "/tools/npm/cache-error" >}}) — npm cache corruption
