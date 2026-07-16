---
title: "[Solution] Node.js Error ENOENT — No Such File or Directory Fix"
description: "Fix Node.js ENOENT error when files cannot be found at runtime. Check file paths, use path.join(), handle __dirname, and use async file operations."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
tags: ["enoent", "nodejs", "file", "path", "fs"]
weight: 90
---

# Node.js Error ENOENT — No Such File or Directory Fix

An `ENOENT` (Error NO ENTry) is thrown by Node.js when the `fs` module tries to access a file or directory that does not exist. This is one of the most frequent errors in Node.js applications and is almost always caused by incorrect file paths, relative path confusion, or missing files.

## Description

Common ENOENT messages include:

- `Error: ENOENT: no such file or directory, open '/path/to/file.txt'`
- `Error: ENOENT: no such file or directory, scandir '/path/to/dir'`
- `Error: ENOENT: no such file or directory, stat '/path/to/file'`

The path in the error message is the exact path Node tried to access. Compare it carefully with where the file actually lives.

## Common Causes

```javascript
// Cause 1: Relative path resolves differently than expected
const fs = require("fs");
fs.readFileSync("data/config.json");  // relative to process.cwd(), not __dirname

// Cause 2: Using __dirname incorrectly with ES modules
import fs from "fs";
const data = fs.readFileSync("./templates/email.html");  // wrong in ES modules

// Cause 3: Missing forward slash in path concatenation
const dir = "/home/user";
const file = dir + "config.json";  // "/home/userconfig.json" instead of "/home/user/config.json"

// Cause 4: File not yet created (race condition)
const content = fs.readFileSync("/tmp/upload.txt");  // file doesn't exist yet

// Cause 5: Windows vs Unix path differences
const filePath = "C:\\Users\\admin\\file.txt";  // fails on Linux/Mac
```

## Solutions

### Fix 1: Use path.join() for cross-platform paths

```javascript
// Wrong - manual string concatenation breaks on different OS
const filePath = __dirname + "/templates/email.html";
// On Windows: __dirname is "C:\app\src", so this becomes "C:\app\src/templates/email.html"

// Correct - path.join handles separators automatically
const path = require("path");
const filePath = path.join(__dirname, "templates", "email.html");
// On Windows: "C:\app\src\templates\email.html"
// On Linux: "/home/user/app/src/templates/email.html"
```

### Fix 2: Use __dirname correctly in ES modules (Node 14+)

```javascript
// Wrong - __dirname is not available in ES modules
import fs from "fs";
const data = fs.readFileSync("data/config.json");

// Correct - import.meta.url with fileURLToPath
import fs from "fs";
import { fileURLToPath } from "url";
import path from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const data = fs.readFileSync(path.join(__dirname, "data", "config.json"));
```

### Fix 3: Verify file exists before reading

```javascript
// Wrong - crashes if file does not exist
const config = JSON.parse(fs.readFileSync("config.json", "utf8"));

// Correct - check first
const fs = require("fs");
const path = require("path");

const configPath = path.join(__dirname, "config.json");

if (!fs.existsSync(configPath)) {
    console.error("Config file not found at:", configPath);
    process.exit(1);
}

const config = JSON.parse(fs.readFileSync(configPath, "utf8"));
```

### Fix 4: Use async file operations with proper error handling

```javascript
// Wrong - synchronous read in async context blocks the event loop
const data = fs.readFileSync(hugeFile);

// Correct - async read with error handling
const fs = require("fs").promises;
const path = require("path");

async function readFileSafe(filePath) {
    try {
        const data = await fs.readFile(filePath, "utf8");
        return data;
    } catch (err) {
        if (err.code === "ENOENT") {
            console.error("File not found:", filePath);
            return null;
        }
        throw err;  // re-throw unexpected errors
    }
}

const config = await readFileSafe(path.join(__dirname, "config.json"));
```

### Fix 5: Use path.resolve for absolute path resolution

```javascript
// Wrong - relative path depends on current working directory
const data = fs.readFileSync("data/input.csv");

// Correct - resolve to absolute path first
const path = require("path");
const filePath = path.resolve(__dirname, "data", "input.csv");
// Always resolves to the same absolute path regardless of cwd
```

### Fix 6: Handle file upload race conditions

```javascript
// Wrong - file might not exist yet after async write
await writeToFile("/tmp/upload.dat", buffer);
const content = fs.readFileSync("/tmp/upload.dat");

// Correct - write and read the same buffer
const content = await writeToFile("/tmp/upload.dat", buffer);
// Or use a temporary path and rename atomically
const tmpPath = "/tmp/upload.dat." + process.pid;
await fs.writeFile(tmpPath, buffer);
await fs.rename(tmpPath, "/tmp/upload.dat");
```

## Debugging Tips

```bash
# Show the actual resolved path Node is trying to access
node -e "console.log(require('path').resolve('data/config.json'))"

# Check if file exists from the command line
ls -la /path/to/missing/file

# Trace file system calls on Linux
strace -e trace=openat node app.js 2>&1 | grep ENOENT

# Use Node's --trace-warnings flag to see the full call stack
node --trace-warnings app.js
```

## Related Errors

- [EACCES](#) — file exists but you lack read/write permission.
- [EISDIR](#) — expected a file but the path is a directory.
- [ENOTDIR](#) — expected a directory but the path is a file.
