---
title: "Node.js Error: read EPIPE / write EPIPE"
description: "Error: read EPIPE / write EPIPE — Fix broken pipe errors in Node.js streams and child processes."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The `EPIPE` error occurs when a Node.js process attempts to write to a pipe (stdin, stdout, or a child process stream) that has already been closed on the reading end. This is common in CLI tools and piped commands.

## Description

Common EPIPE messages include:

- `Error: write EPIPE` — writing to a closed pipe
- `Error: read EPIPE` — reading from a closed pipe
- `write EPIPE` — appears when piping output to `head`, `grep`, or similar commands
- `Error: This socket has been ended by the other party` — related pipe closure

## Common Causes

```javascript
// Cause 1: Piping output to a command that exits early
// $ node app.js | head -5
// head reads 5 lines then exits; node continues writing

// Cause 2: stdin closed before write completes
process.stdin.resume();
process.stdin.on("data", (chunk) => {
  process.stdout.write(chunk); // EPIPE if stdout closed
});

// Cause 3: Child process exits before parent finishes writing
const { spawn } = require("node:child_process");
const child = spawn("head", ["-5"]);
child.stdin.write("line1\nline2\nline3\nline4\nline5\n");
child.stdin.write("line6\n"); // EPIPE — head already exited

// Cause 4: HTTP response already closed
// Writing to a response after client disconnects
```

## Solutions

### Fix 1: Handle EPIPE errors gracefully

```javascript
process.on("SIGPIPE", () => {
  process.exit(0);
});

process.stdout.on("error", (err) => {
  if (err.code === "EPIPE") {
    process.exit(0);
  }
  throw err;
});

process.stderr.on("error", (err) => {
  if (err.code === "EPIPE") {
    process.exit(0);
  }
  throw err;
});
```

### Fix 2: Check child process exit code

```javascript
const { spawn } = require("node:child_process");

function safePipeInput(command, args, input) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args);
    let stderr = "";

    child.stdin.on("error", (err) => {
      if (err.code === "EPIPE") return; // ignore
      reject(err);
    });

    child.stderr.on("data", (data) => { stderr += data; });
    child.on("close", (code) => {
      if (code !== 0) {
        reject(new Error(`${command} exited with code ${code}: ${stderr}`));
      }
      resolve();
    });

    child.stdin.end(input);
  });
}
```

### Fix 3: Handle HTTP response disconnections

```javascript
const http = require("node:http");

const server = http.createServer((req, res) => {
  res.on("error", (err) => {
    if (err.code === "EPIPE") {
      console.warn("Client disconnected during response");
      return;
    }
    throw err;
  });

  res.write("data\n");
  res.end();
});
```

## Examples

```javascript
// EPIPE when piping to head
// $ node -e "for(;;) console.log('line')" | head -1
// After head exits, node keeps writing to stdout → EPIPE

// Fix: detect broken pipe
process.stdout.on("error", (err) => {
  if (err.code === "EPIPE") process.exit(0);
  throw err;
});
```

## Related Errors

- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — writing to a destroyed stream.
- [ERR_SOCKET_DESTROYED]({{< relref "/languages/javascript/err_socket_destroyed" >}}) — socket already destroyed.
- [ERR_HTTP_HEADERS_SENT]({{< relref "/languages/javascript/err_http_headers_sent" >}}) — headers already sent.
