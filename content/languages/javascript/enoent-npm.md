---
title: "[Solution] npm ERR! enoent - package.json Missing"
description: "Fix npm ERR! enoent - no such file or directory when running npm install. Resolve missing package.json issues in Node.js projects."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["npm", "enoent", "package-json", "node-modules", "install"]
weight: 5
---

# npm ERR! enoent — package.json Missing

This error occurs when npm cannot find a `package.json` file in the current directory or parent directories. npm requires a `package.json` to understand the project structure and dependencies.

## What This Error Means

Common error messages:

- `npm ERR! enoent ENOENT: no such file or directory, open '/path/to/package.json'`
- `npm ERR! enoent ENOENT: no such file or directory, stat '/path/to/package.json'`
- `npm ERR! code ENOENT npm ERR! enoent`

npm traverses up the directory tree looking for a `package.json`. If none is found, this error is thrown.

## Common Causes

```bash
# Cause 1: Running npm install in wrong directory
cd /home/user
npm install  # no package.json here

# Cause 2: package.json was deleted or never created
rm package.json
npm install  # ENOENT

# Cause 3: Running npm commands before initializing the project
mkdir new-project && cd new-project
npm install express  # no package.json yet

# Cause 4: Typo in directory path
cd /home/user/projets/my-app  # wrong directory name
npm install
```

## How to Fix

### Fix 1: Initialize package.json

```bash
# Create a new package.json
npm init -y

# Then install dependencies
npm install express
```

### Fix 2: Navigate to the correct directory

```bash
# Check current directory
pwd

# Find the project root containing package.json
find . -name "package.json" -maxdepth 3

# Navigate to it
cd /path/to/your/project
npm install
```

### Fix 3: Create package.json manually

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "dependencies": {},
  "devDependencies": {}
}
```

### Fix 4: Check for .npmrc issues

```bash
# Ensure .npmrc doesn't override package location
cat .npmrc

# Reset npm config if needed
npm config set prefix /usr/local
```

## Examples

```bash
# This triggers the error
mkdir temp && cd temp
npm install express

# Output:
# npm ERR! code ENOENT
# npm ERR! enoent ENOENT: no such file or directory, open '/home/user/temp/package.json'

# Fix: initialize first
npm init -y
npm install express
# Works correctly
```

## Related Errors

- [ENOENT Node.js]({{< relref "/languages/javascript/enoent-node" >}}) — fs module file not found
- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err-module-not-found" >}}) — ES module not found
- [ERR_REQUIRE_ESM]({{< relref "/languages/javascript/err-import-assertion" >}}) — require() of ES module
