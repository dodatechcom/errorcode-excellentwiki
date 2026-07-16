---
title: "[Solution] Node.js ERR_HTTP2_PRIORITY — HTTP/2 Priority Error Fix"
description: "Fix Node.js ERR_HTTP2_PRIORITY when an HTTP/2 stream priority operation fails. Handle stream priority and dependency errors properly."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http2-priority", "http2", "priority", "stream", "dependency", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP2_PRIORITY — HTTP/2 Priority Error Fix

The `ERR_HTTP2_PRIORITY` error occurs when an HTTP/2 stream priority operation fails. HTTP/2 allows streams to declare dependencies on other streams to control resource allocation, and errors can occur when these priority relationships are invalid.

## Description

Common ERR_HTTP2_PRIORITY messages include:

- `ERR_HTTP2_PRIORITY: Priority error` — priority operation failed.
- `Invalid stream dependency` — stream depends on itself.
- `Priority cycle detected` — circular dependency in stream tree.
- `Stream not found` — priority references non-existent stream.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Stream depends on itself
const client = http2.connect("https://localhost:3000");
const req = client.request({
  ":path": "/api",
  "priority": {
    streamDependency: 1, // depends on itself if stream ID is 1
    weight: 16,
    exclusive: false,
  },
});

// Cause 2: Circular dependency
// Stream A depends on B, B depends on A

// Cause 3: Invalid priority weight
// Weight must be between 1 and 256

// Cause 4: Priority on closed stream
// Setting priority for a stream that's already closed
```

## Solutions

### Fix 1: Set valid priority values

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

const req = client.request({
  ":path": "/api",
  "priority": {
    streamDependency: 0, // root dependency
    weight: 16, // valid range: 1-256
    exclusive: true,
  },
});

req.on("response", (headers) => {
  console.log("Status:", headers[":status"]);
});
req.end();
```

### Fix 2: Avoid circular dependencies

```javascript
const http2 = require("node:http2");

class StreamPriorityManager {
  constructor() {
    this.dependencies = new Map();
  }

  addDependency(streamId, dependsOn) {
    // Check for circular dependency
    if (this.wouldCreateCycle(streamId, dependsOn)) {
      throw new Error(`Circular dependency: ${streamId} -> ${dependsOn}`);
    }
    this.dependencies.set(streamId, dependsOn);
  }

  wouldCreateCycle(streamId, dependsOn) {
    let current = dependsOn;
    while (current !== undefined) {
      if (current === streamId) return true;
      current = this.dependencies.get(current);
    }
    return false;
  }
}

const manager = new StreamPriorityManager();
manager.addDependency(2, 0);
manager.addDependency(4, 2);
```

### Fix 3: Validate stream exists before priority

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

function setPrioritySafe(client, streamId, parentId, weight) {
  // Verify parent stream exists or is root (0)
  if (parentId !== 0) {
    // Stream existence would need to be tracked
    console.warn(`Cannot verify stream ${parentId} exists`);
  }

  const req = client.request({
    ":path": "/api",
    "priority": {
      streamDependency: parentId,
      weight: Math.max(1, Math.min(256, weight)),
      exclusive: false,
    },
  });

  return req;
}
```

### Fix 4: Handle priority errors gracefully

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.on("error", (err) => {
    if (err.code === "ERR_HTTP2_PRIORITY") {
      console.error("Priority error on stream", stream.id);
      // Stream can still function, priority is advisory
    }
  });

  stream.respond({ ":status": 200 });
  stream.end("OK");
});

server.on("priority", (stream, priority) => {
  console.log("Stream priority:", stream.id, priority);
});
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_PRIORITY with invalid weight
const client = http2.connect("https://localhost:3000");

try {
  const req = client.request({
    ":path": "/api",
    "priority": {
      streamDependency: 0,
      weight: 0, // invalid: must be >= 1
      exclusive: false,
    },
  });
} catch (err) {
  if (err.code === "ERR_HTTP2_PRIORITY") {
    console.error("Invalid priority weight");
  }
}
```

## Related Errors

- [ERR_HTTP2_STREAM_ERROR]({{< relref "/languages/javascript/err-http2-stream-error" >}}) — HTTP/2 stream error.
- [ERR_HTTP2_SESSION]({{< relref "/languages/javascript/err-http2-session" >}}) — HTTP/2 session error.
- [ERR_HTTP2_RST_STREAM]({{< relref "/languages/javascript/err-http2-rst-stream" >}}) — stream reset by peer.
- [ERR_HTTP2_STREAM]({{< relref "/languages/javascript/err-http2-stream" >}}) — HTTP/2 stream operation error.
