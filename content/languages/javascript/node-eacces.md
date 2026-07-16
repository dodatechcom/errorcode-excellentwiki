---
title: "Node.js Error EACCES: Permission Denied"
description: "Error: EACCES: permission denied — Fix Node.js file system permission errors."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nodejs", "eacces", "permission-denied", "fs", "chmod"]
weight: 5
---

The `EACCES` error occurs when Node.js attempts to access a file or directory without the necessary OS-level permissions. This is an operating system permission error, not a Node.js issue.

## Description

Common EACCES messages include:

- `EACCES: permission denied, open '/path/to/file'` — cannot read/write file
- `EACCES: permission denied, mkdir '/path/to/dir'` — cannot create directory
- `EACCES: permission denied, access '/path/to/file'` — cannot stat file
- `EACCES: permission denied, unlink '/path/to/file'` — cannot delete file

## Common Causes

```javascript
// Cause 1: Running as a user without file permissions
// $ node app.js (as regular user, file owned by root)

// Cause 2: File permissions are too restrictive
// $ ls -la /etc/passwd
// -rw------- 1 root root ... /etc/passwd

// Cause 3: Directory does not allow execution (traverse)
// Without +x on a directory, you cannot access files inside it

// Cause 4: Trying to write to a read-only filesystem
fs.writeFile("/usr/local/protected.txt", "data", (err) => {
  // EACCES
});
```

## Solutions

### Fix 1: Check and fix file permissions

```bash
# Check current permissions
ls -la /path/to/file

# Grant read/write to the user
chmod 644 /path/to/file

# Grant full access (use cautiously)
chmod 666 /path/to/file
```

### Fix 2: Use a writable directory

```javascript
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");

// Use the user's home directory instead of system paths
const outputPath = path.join(os.homedir(), ".myapp", "data.json");
const dir = path.dirname(outputPath);

if (!fs.existsSync(dir)) {
  fs.mkdirSync(dir, { recursive: true });
}

fs.writeFileSync(outputPath, "{}");
```

### Fix 3: Handle permission errors gracefully

```javascript
const fs = require("node:fs");

function safeWrite(filePath, data) {
  try {
    fs.writeFileSync(filePath, data, { mode: 0o644 });
    return true;
  } catch (err) {
    if (err.code === "EACCES") {
      console.error(`Permission denied: ${filePath}`);
      console.error(`Try: chmod 644 ${filePath}`);
    }
    throw err;
  }
}
```

## Examples

```javascript
// EACCES when running Node.js app as wrong user
// $ node server.js  (needs port 80, requires root)
// Error: EACCES: permission denied, listen

// Fix: use a port > 1024 or use setcap
// $ sudo setcap 'cap_net_bind_service=+ep' $(which node)
```

## Related Errors

- [ERR_FILE_TOO_LARGE]({{< relref "/languages/javascript/err_file_too_large" >}}) — file exceeds size limits.
- [ENOENT]({{< relref "/languages/javascript/node-enent" >}}) — file not found.
- [ERR_DOPEN_DISABLED]({{< relref "/languages/javascript/err_dlopen_disabled" >}}) — dynamic linking disabled.
