---
title: "[Solution] Node.js EPIPE: broken pipe Error Fix"
description: "Fix Node.js EPIPE: broken pipe error. Handle broken pipe errors in streams, HTTP responses, and child processes."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js EPIPE — broken pipe

This error occurs when trying to write to a pipe (stream) whose read end has been closed. It commonly happens when piping data to a process that has already exited.

## What This Error Means

Common error messages:

- `Error: write EPIPE`
- `Error: EBROKENPIPE: broken pipe`
- `EPIPE: broken pipe, write`

When a process reads from a pipe and exits, the write end receives a SIGPIPE signal and EPIPE error.

## Common Causes

```javascript
// Cause 1: Piping to a process that already exited
const { spawn } = require('child_process');
const proc = spawn('grep', ['pattern']);
proc.stdin.write('line1\n');
proc.kill(); // kill process
proc.stdin.write('line2\n'); // EPIPE

// Cause 2: HTTP client disconnects before response is complete
const server = http.createServer(async (req, res) => {
  const stream = fs.createReadStream('/large-file.txt');
  stream.pipe(res); // client disconnects = EPIPE
});

// Cause 3: Writing to closed writable stream
const { Writable } = require('stream');
const writable = new Writable({ write: (chunk, enc, cb) => cb() });
writable.end();
writable.write('data'); // EPIPE

// Cause 4: Child process closes stdin before all data is written
```

## How to Fix

### Fix 1: Handle SIGPIPE and EPIPE errors

```javascript
const { spawn } = require('child_process');

const proc = spawn('grep', ['pattern']);
proc.stdin.on('error', (err) => {
  if (err.code === 'EPIPE') {
    console.error('Child process closed stdin');
  }
});
```

### Fix 2: Listen for close event before writing more

```javascript
const { spawn } = require('child_process');
const proc = spawn('head', ['-n', '5']);

const lines = Array.from({ length: 20 }, (_, i) => `Line ${i}\n`);
let index = 0;

function writeNext() {
  if (index >= lines.length) return proc.stdin.end();
  if (proc.stdin.write(lines[index])) {
    index++;
    writeNext();
  } else {
    proc.stdin.once('drain', writeNext);
  }
}

proc.on('close', () => {
  index = lines.length; // stop writing
});

writeNext();
```

### Fix 3: Handle EPIPE in HTTP streaming

```javascript
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  const stream = fs.createReadStream('/large-file.txt');

  stream.on('error', (err) => {
    if (err.code === 'EPIPE') {
      console.log('Client disconnected');
      stream.destroy();
    }
  });

  res.on('error', (err) => {
    if (err.code === 'EPIPE') {
      console.log('Response pipe broken');
    }
  });

  stream.pipe(res);
});
```

### Fix 4: Use pipeline with error handling

```javascript
const { pipeline } = require('stream/promises');
const { createReadStream, createWriteStream } = require('fs');

async function safePipeline(src, dest) {
  try {
    await pipeline(src, dest);
  } catch (err) {
    if (err.code === 'EPIPE') {
      console.log('Pipeline broken, cleaning up');
    } else {
      throw err;
    }
  }
}
```

## Examples

```javascript
const { spawn } = require('child_process');

// This triggers EPIPE
const proc = spawn('sort');
proc.stdin.write('banana\napple\n');
proc.stdin.end();
proc.stdin.write('cherry\n'); // EPIPE - stdin already closed
```

## Related Errors

- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream already destroyed
- [ECONNRESET]({{< relref "/languages/javascript/err-connection-reset" >}}) — connection reset
- [EBADF]({{< relref "/languages/javascript/ebadfd" >}}) — bad file descriptor
