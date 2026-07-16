---
title: "[Solution] Node.js ERR_HTTP2_SETTINGS — HTTP/2 Settings Error Fix"
description: "Fix Node.js ERR_HTTP2_SETTINGS when an HTTP/2 SETTINGS frame operation fails. Handle settings negotiation errors properly."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http2-settings", "http2", "settings", "configuration", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP2_SETTINGS — HTTP/2 Settings Error Fix

The `ERR_HTTP2_SETTINGS` error occurs when an HTTP/2 SETTINGS frame operation fails. This can happen when settings are sent on a closed session, when settings values are invalid, or when SETTINGS acknowledgments fail.

## Description

Common ERR_HTTP2_SETTINGS messages include:

- `ERR_HTTP2_SETTINGS: Settings error` — SETTINGS frame failed.
- `Cannot send settings on closed session` — session is not active.
- `Invalid settings value` — settings parameter is out of range.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Sending settings on destroyed session
const client = http2.connect("https://localhost:3000");
client.destroy();
client.settings({ maxConcurrentStreams: 100 }); // ERR_HTTP2_SETTINGS

// Cause 2: Invalid settings values
client.settings({
  maxConcurrentStreams: -1, // negative value
  headerTableSize: 0, // too small
  maxFrameSize: 100, // below minimum
});

// Cause 3: Changing settings too frequently
client.settings({ maxConcurrentStreams: 100 });
client.settings({ maxConcurrentStreams: 200 });
client.settings({ maxConcurrentStreams: 300 }); // rapid changes

// Cause 4: Settings on HTTP/1.1 connection
const http = require("node:http");
const req = http.get("http://localhost:3000");
// HTTP/1.1 doesn't have SETTINGS
```

## Solutions

### Fix 1: Validate settings before sending

```javascript
const http2 = require("node:http2");

const VALID_SETTINGS = {
  headerTableSize: { min: 0, max: 4294967295 },
  enablePush: { min: 0, max: 1 },
  maxConcurrentStreams: { min: 0, max: 4294967295 },
  initialWindowSize: { min: 0, max: 2147483647 },
  maxFrameSize: { min: 16384, max: 16777215 },
  maxHeaderListSize: { min: 0, max: 4294967295 },
};

function validateSettings(settings) {
  for (const [key, value] of Object.entries(settings)) {
    const range = VALID_SETTINGS[key];
    if (!range) {
      throw new Error(`Unknown setting: ${key}`);
    }
    if (value < range.min || value > range.max) {
      throw new Error(`Setting ${key} must be between ${range.min} and ${range.max}`);
    }
  }
  return true;
}

const client = http2.connect("https://localhost:3000");
validateSettings({ maxConcurrentStreams: 100 });
client.settings({ maxConcurrentStreams: 100 });
```

### Fix 2: Check session state before settings

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

function safeSettings(client, settings) {
  if (client.destroyed || client.closed) {
    console.warn("Cannot send settings: session not available");
    return false;
  }
  client.settings(settings);
  return true;
}

safeSettings(client, { maxConcurrentStreams: 100 });
```

### Fix 3: Handle settings acknowledgments

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

client.on("remoteSettings", (settings) => {
  console.log("Remote settings:", settings);
});

client.on("localSettings", (settings) => {
  console.log("Local settings applied:", settings);
});

client.on("error", (err) => {
  if (err.code === "ERR_HTTP2_SETTINGS") {
    console.error("Settings error:", err.message);
  }
});

// Send settings with callback
client.settings({
  maxConcurrentStreams: 100,
  initialWindowSize: 1048576,
});
```

### Fix 4: Configure server settings properly

```javascript
const http2 = require("node:http2");

const server = http2.createServer({
  settings: {
    headerTableSize: 4096,
    enablePush: false,
    maxConcurrentStreams: 100,
    initialWindowSize: 65535,
    maxFrameSize: 16384,
    maxHeaderListSize: 16384,
  },
});

server.on("stream", (stream, headers) => {
  stream.respond({ ":status": 200 });
  stream.end("OK");
});
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_SETTINGS from invalid values
const client = http2.connect("https://localhost:3000");

try {
  client.settings({
    maxFrameSize: 100, // below minimum of 16384
  });
} catch (err) {
  console.error(err.code); // ERR_HTTP2_SETTINGS
}
```

## Related Errors

- [ERR_HTTP2_SESSION]({{< relref "/languages/javascript/err-http2-session" >}}) — HTTP/2 session error.
- [ERR_HTTP2_PING]({{< relref "/languages/javascript/err-http2-pong" >}}) — PING operation failed.
- [ERR_HTTP2_ENHANCE_YOUR_CALM]({{< relref "/languages/javascript/err-http2-enhance-your-calm" >}}) — rate limit exceeded.
- [ERR_HTTP2_FRAME_ERROR]({{< relref "/languages/javascript/err-http2-frame-error" >}}) — invalid frame received.
