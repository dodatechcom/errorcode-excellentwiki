---
title: "Node.js Error ENOENT: No Such File or Directory"
description: "Error: ENOENT: no such file or directory — Fix Node.js file system errors when files or directories cannot be found."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nodejs", "enoent", "file-system", "fs", "no-such-file"]
weight: 5
---

The `ENOENT` error occurs when Node.js cannot find a file or directory at the specified path. This is one of the most common Node.js errors and is thrown by the `fs` module when operating on a non-existent path.

## Description

Common ENOENT messages include:

- `ENOENT: no such file or directory, open '/path/to/file.txt'` — file does not exist
- `ENOENT: no such file or directory, scandir '/path/to/dir'` — directory does not exist
- `ENOENT: no such file or directory, stat '/path/to/file'` — path does not exist

## Common Causes

```javascript
// Cause 1: File does not exist at the given path
fs.readFile("/tmp/missing.txt", (err) => {});

// Cause 2: Wrong relative path (cwd is not what you expect)
const data = fs.readFileSync("./config.json"); // cwd may differ

// Cause 3: Race condition — file deleted between check and use
if (fs.existsSync(path)) {
  // Another process may delete the file here
  fs.readFileSync(path); // ENOENT
}

// Cause 4: Path construction error
const filePath = path.join(dir, filename); // dir or filename undefined
```

## Solutions

### Fix 1: Verify path exists before operating

```javascript
const fs = require("node:fs");
const path = require("node:path");

function readFileSafe(filePath) {
  try {
    return fs.readFileSync(filePath, "utf-8");
  } catch (err) {
    if (err.code === "ENOENT") {
      console.error(`File not found: ${filePath}`);
      return null;
    }
    throw err;
  }
}
```

### Fix 2: Use __dirname for relative paths

```javascript
const path = require("node:path");
const fs = require("node:fs");

// Use __dirname instead of relative paths
const configPath = path.join(__dirname, "..", "config", "app.json");
const config = JSON.parse(fs.readFileSync(configPath, "utf-8"));
```

### Fix 3: Ensure directories exist before writing

```javascript
const fs = require("node:fs");
const path = require("node:path");

function ensureDirSync(dirPath) {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }
}

const outputDir = path.join(__dirname, "output");
ensureDirSync(outputDir);
fs.writeFileSync(path.join(outputDir, "data.json"), "{}");
```

## Examples

```javascript
// ENOENT when reading a file that does not exist
const fs = require("node:fs");
fs.readFile("/tmp/nonexistent.txt", (err) => {
  if (err.code === "ENOENT") {
    console.error("File does not exist");
  }
});

// ENOENT when requiring a module with wrong path
// Error: Cannot find module './lib/helper'
// Fix: check the actual file name and path
```

## Related Errors

- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err-cannot-find-module" >}}) — module resolution failure.
- [ERR_NO_CWD]({{< relref "/languages/javascript/err_no_cwd" >}}) — cannot access current working directory.
- [ERR_FILE_TOO_LARGE]({{< relref "/languages/javascript/err_file_too_large" >}}) — file too large for read operation.
