---
title: "[Solution] Node.js ENOENT - no such file or directory Error Fix"
description: "Fix Node.js ENOENT: no such file or directory error from fs module. Handle file operations, check paths, and use proper error handling."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["enoent", "fs", "file-not-found", "nodejs", "filesystem"]
weight: 5
---

# Node.js ENOENT — no such file or directory

This error occurs when the Node.js `fs` module attempts to access a file or directory that does not exist. It is one of the most common filesystem errors in Node.js.

## What This Error Means

Common error messages:

- `Error: ENOENT: no such file or directory, open '/path/to/file.txt'`
- `Error: ENOENT: no such file or directory, stat '/path/to/file.txt'`
- `Error: ENOENT: no such file or directory, readdir '/path/to/dir'`

The `ENOENT` code stands for "Error NO ENTry" — the file system entry does not exist.

## Common Causes

```javascript
// Cause 1: File doesn't exist
const fs = require('fs');
fs.readFileSync('/tmp/missing-file.txt'); // ENOENT

// Cause 2: Incorrect file path (typo)
fs.readFileSync('/home/user/douments/file.txt'); // misspelled

// Cause 3: Using relative path from wrong working directory
// Running: node scripts/build.js from project root
fs.readFileSync('src/index.js'); // wrong relative path

// Cause 4: Directory doesn't exist
fs.readdirSync('/tmp/nonexistent-folder'); // ENOENT

// Cause 5: File was deleted before access
fs.unlinkSync('/tmp/file.txt');
fs.readFileSync('/tmp/file.txt'); // ENOENT
```

## How to Fix

### Fix 1: Check if file exists before accessing

```javascript
const fs = require('fs');
const path = require('path');

function readConfig(configPath) {
  if (!fs.existsSync(configPath)) {
    console.warn(`Config file not found: ${configPath}, using defaults`);
    return { port: 3000 };
  }
  return JSON.parse(fs.readFileSync(configPath, 'utf8'));
}
```

### Fix 2: Use try-catch with fs operations

```javascript
const fs = require('fs/promises');

async function readFileSafe(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    return { data, error: null };
  } catch (err) {
    if (err.code === 'ENOENT') {
      return { data: null, error: `File not found: ${filePath}` };
    }
    throw err;
  }
}
```

### Fix 3: Resolve paths with path module

```javascript
const path = require('path');

// Wrong: hardcoded absolute path
const config = require('/home/user/config.json');

// Correct: resolve relative to __dirname
const configPath = path.join(__dirname, '..', 'config', 'config.json');
const config = require(configPath);
```

### Fix 4: Ensure directories exist before writing

```javascript
const fs = require('fs/promises');
const path = require('path');

async function ensureDirAndWrite(filePath, content) {
  const dir = path.dirname(filePath);
  await fs.mkdir(dir, { recursive: true });
  await fs.writeFile(filePath, content);
}
```

## Examples

```javascript
const fs = require('fs');

// This triggers ENOENT
try {
  fs.readFileSync('/tmp/nonexistent.txt');
} catch (err) {
  console.error(err.code); // "ENOENT"
  console.error(err.message); // "ENOENT: no such file or directory..."
}
```

## Related Errors

- [npm ERR! enoent]({{< relref "/languages/javascript/enoent-npm" >}}) — package.json missing
- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err-module-not-found" >}}) — ES module resolution failed
- [ERR_FILE_TOO_LARGE]({{< relref "/languages/javascript/err_file_too_large" >}}) — file exceeds size limit
