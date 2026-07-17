---
title: "[Solution] Node.js EBADF: bad file descriptor Error Fix"
description: "Fix Node.js EBADF: bad file descriptor error. Handle closed file descriptors, prevent double-close, and manage file operations."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js EBADF — bad file descriptor

This error occurs when attempting to read from, write to, or close a file descriptor that is invalid, already closed, or never existed.

## What This Error Means

Common error messages:

- `Error: EBADF: bad file descriptor, read`
- `Error: EBADF: bad file descriptor, write`
- `Error: EBADF: bad file descriptor, close`

A file descriptor (fd) is a reference to an open file. After closing a file, its fd becomes invalid and cannot be used again.

## Common Causes

```javascript
// Cause 1: Reading from closed file descriptor
const fs = require('fs');
const fd = fs.openSync('/tmp/test.txt', 'r');
fs.closeSync(fd);
fs.readSync(fd, Buffer.alloc(100), 0, 100, 0); // EBADF

// Cause 2: Double-closing a file descriptor
const fd2 = fs.openSync('/tmp/test.txt', 'w');
fs.closeSync(fd2);
fs.closeSync(fd2); // EBADF

// Cause 3: Using stream after it's destroyed
const stream = fs.createReadStream('/tmp/test.txt');
stream.destroy();
stream.on('data', () => {}); // EBADF

// Cause 4: Race condition in async operations
fs.open('/tmp/test.txt', 'r', (err, fd) => {
  fs.close(fd); // closes the fd
  fs.read(fd, buf, 0, 100, null, callback); // EBADF
});
```

## How to Fix

### Fix 1: Track file descriptor state

```javascript
const fs = require('fs/promises');

class SafeFileReader {
  constructor(path) {
    this.path = path;
    this.fd = null;
  }

  async open() {
    this.fd = await fs.open(this.path, 'r');
  }

  async read(buffer, length) {
    if (!this.fd) throw new Error('File not opened');
    return this.fd.read(buffer, 0, length, 0);
  }

  async close() {
    if (this.fd) {
      await this.fd.close();
      this.fd = null;
    }
  }
}
```

### Fix 2: Use try-finally to ensure cleanup

```javascript
const fs = require('fs/promises');

async function processFile(path) {
  let fd;
  try {
    fd = await fs.open(path, 'r');
    const buffer = Buffer.alloc(1024);
    await fd.read(buffer, 0, 1024, 0);
    return buffer.toString();
  } finally {
    if (fd) await fd.close();
  }
}
```

### Fix 3: Don't reuse streams after destroy

```javascript
const fs = require('fs');

const stream = fs.createReadStream('/tmp/test.txt');
stream.on('error', (err) => {
  if (err.code === 'EBADF') {
    console.error('Stream was closed');
  }
});

// Don't do this after stream.destroy():
// stream.pipe(anotherStream);
```

### Fix 4: Check if file is still open

```javascript
const fs = require('fs');

function safeRead(fd, buffer) {
  try {
    fs.fstatSync(fd); // check if fd is valid
    return fs.readSync(fd, buffer, 0, buffer.length, 0);
  } catch (err) {
    if (err.code === 'EBADF') {
      console.error('File descriptor is no longer valid');
      return null;
    }
    throw err;
  }
}
```

## Examples

```javascript
const fs = require('fs');

// This triggers EBADF
const fd = fs.openSync('/tmp/test.txt', 'w');
fs.writeSync(fd, 'hello');
fs.closeSync(fd);
fs.writeSync(fd, 'world'); // EBADF: bad file descriptor
```

## Related Errors

- [ENOENT]({{< relref "/languages/javascript/enoent-node" >}}) — file not found
- [EACCES]({{< relref "/languages/javascript/eacces-npm" >}}) — permission denied
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream destroyed
