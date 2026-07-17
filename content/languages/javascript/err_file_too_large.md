---
title: "[Solution] Node.js ERR_FILE_TOO_LARGE — File Too Large Fix"
description: "Fix Node.js ERR_FILE_TOO_LARGE when reading or writing files that exceed size limits. Use streams for large files and check available disk space."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_FILE_TOO_LARGE — File Too Large Fix

The `ERR_FILE_TOO_LARGE` error occurs when attempting to read or write a file that exceeds the system's or Node.js's maximum file size limit. This commonly happens when loading entire large files into memory using `readFile` or `writeFile`.

## Description

Common ERR_FILE_TOO_LARGE messages include:

- `Error [ERR_FILE_TOO_LARGE]: File size (...) is greater than 2 GiB` — 32-bit file size limit.
- `RangeError: Invalid string length` — string buffer overflow from large file content.
- `ERR_FS_FILE_TOO_LARGE` — file exceeds V8 string or buffer limits.

## Common Causes

```javascript
const fs = require("fs");

// Cause 1: Reading a multi-gigabyte file into memory
const hugeData = fs.readFileSync("/data/big-database.dump");
// ERR_FILE_TOO_LARGE or out of memory

// Cause 2: Writing a buffer larger than the string length limit
const largeString = "x".repeat(2**32);  // ~4GB string
fs.writeFileSync("/tmp/large.txt", largeString);  // ERR_FILE_TOO_LARGE

// Cause 3: 32-bit Node.js build attempting > 2GB file operations
// 32-bit systems cannot handle files larger than 2 GiB

// Cause 4: Concatenating many buffers beyond V8 limits
const chunks = [];
for (let i = 0; i < 10_000_000; i++) {
  chunks.push(Buffer.alloc(1000));
}
Buffer.concat(chunks);  // may exceed memory limits
```

## Solutions

### Fix 1: Use streams for large file operations

```javascript
const fs = require("fs");
const { pipeline } = require("stream/promises");

// Wrong — loads entire file into memory
// const data = fs.readFileSync("/data/huge-file.bin");

// Correct — stream the file
async function copyLargeFile(src, dest) {
  const readable = fs.createReadStream(src);
  const writable = fs.createWriteStream(dest);

  await pipeline(readable, writable);
  console.log("File copied successfully");
}

copyLargeFile("/data/huge-file.bin", "/tmp/copy.bin");
```

### Fix 2: Process large files in chunks

```javascript
const fs = require("fs");

async function processLargeFile(filePath, processChunk) {
  const stream = fs.createReadStream(filePath, {
    highWaterMark: 64 * 1024,  // 64KB chunks
  });

  for await (const chunk of stream) {
    await processChunk(chunk);
  }
}

// Usage: count lines in a large file
let lineCount = 0;
await processLargeFile("/data/big-log.txt", (chunk) => {
  lineCount += chunk.toString().split("\n").length;
});
console.log("Lines:", lineCount);
```

### Fix 3: Check file size before reading

```javascript
const fs = require("fs").promises;
const MAX_FILE_SIZE = 100 * 1024 * 1024; // 100 MB limit

async function safeReadFile(filePath) {
  const stat = await fs.stat(filePath);

  if (stat.size > MAX_FILE_SIZE) {
    console.error(`File too large: ${(stat.size / 1024 / 1024).toFixed(1)} MB`);
    console.error(`Maximum allowed: ${MAX_FILE_SIZE / 1024 / 1024} MB`);
    return null;
  }

  return await fs.readFile(filePath, "utf-8");
}
```

### Fix 4: Use streaming for file uploads

```javascript
const fs = require("fs");
const FormData = require("form-data");
const http = require("http");

function uploadLargeFile(filePath, uploadUrl) {
  const form = new FormData();
  form.append("file", fs.createReadStream(filePath));

  return new Promise((resolve, reject) => {
    const req = http.request(uploadUrl, {
      method: "POST",
      headers: form.getHeaders(),
    });

    form.pipe(req);

    req.on("response", (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => resolve(data));
    });

    req.on("error", reject);
  });
}
```

### Fix 5: Use 64-bit Node.js for large file support

```bash
# Check if Node.js is 32-bit or 64-bit
node -e "console.log(process.arch)"
# Should output: x64, arm64, etc. (not ia32 or arm)

# Install 64-bit Node.js if running on 32-bit
# Download from https://nodejs.org (choose 64-bit installer)
```

## Examples

```javascript
// Stream-based line reader for large log files
const fs = require("fs");
const readline = require("readline");

async function* readLargeFileLines(filePath) {
  const stream = fs.createReadStream(filePath);
  const rl = readline.createInterface({ input: stream, crlfDelay: Infinity });

  for await (const line of rl) {
    yield line;
  }
}

// Process a 10GB log file line by line without loading into memory
for await (const line of readLargeFileLines("/var/log/huge.log")) {
  if (line.includes("ERROR")) {
    console.log(line);
  }
}
```

## Related Errors

- [SystemError]({{< relref "/languages/javascript/ensystemerror" >}}) — operating system-level error.
- [ERR_NO_CWD]({{< relref "/languages/javascript/err_no_cwd" >}}) — current working directory inaccessible.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream already destroyed.
- [ERR_SOCKET_DESTROYED]({{< relref "/languages/javascript/err_socket_destroyed" >}}) — socket already destroyed.
