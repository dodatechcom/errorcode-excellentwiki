---
title: "[Solution] npm rebuild Python Not Found"
description: "Fix npm rebuild Python not found errors by installing Python, configuring node-gyp, and setting the correct Python path in npm config."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm rebuild Python Not Found

This guide helps you diagnose and resolve npm rebuild Python Not Found errors encountered when running npm commands.

## Common Causes

- Python is not installed on the system
- Python is installed but not in the system PATH
- node-gyp expects Python 2.x but only Python 3.x is available

## How to Fix

### Install Python 3

```bash
sudo apt-get install python3
```

### Set Python Path for npm

```bash
npm config set python /usr/bin/python3
```

### Verify Python Installation

```bash
python3 --version
```

## Examples

```bash
# Python not installed
npm rebuild node-sass
# Fix: Install Python
sudo apt-get install python3

# Python not in PATH
npm rebuild
# Fix: Set path in npm config
npm config set python /usr/bin/python3
npm rebuild

```

## Related Errors

- [Node-gyp Error]({{< relref "/tools/npm/node-gyp-error" >}}) -- build tool error
- [Build Failed]({{< relref "/tools/npm/build-failed" >}}) -- compilation error
