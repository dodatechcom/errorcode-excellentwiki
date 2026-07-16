---
title: "[Solution] JavaScript InvalidStateError — Invalid Object State Fix"
description: "Fix JavaScript InvalidStateError when an object is not in the correct state for the requested operation. Check readiness, lifecycle, and initialization order."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["invalidstateerror", "state", "lifecycle", "ready", "dom"]
weight: 5
---

# InvalidStateError — Invalid Object State Fix

An `InvalidStateError` is thrown when an operation is attempted on an object that is not in the required state. This commonly occurs with DOM APIs (WebSocket, MediaSource, XMLHttpRequest) when operations are called before the object is ready or after it has been closed.

## Description

Common InvalidStateError messages include:

- `InvalidStateError: The object is in an invalid state` — generic state mismatch.
- `InvalidStateError: Failed to execute 'send' on 'WebSocket': readyState is not OPEN` — WebSocket not connected.
- `InvalidStateError: Cannot set the playbackRate when the media is not ready` — media element not loaded.
- `InvalidStateError: An attempt was made to use an object that is not, or is no longer, usable` — closed stream or connection.

## Common Causes

```javascript
// Cause 1: Sending on a WebSocket before it's open
const ws = new WebSocket("wss://example.com");
ws.send("hello");  // InvalidStateError: readyState is CONNECTING (0)

// Cause 2: Calling methods on a closed connection
const ws2 = new WebSocket("wss://example.com");
ws2.close();
ws2.send("hello");  // InvalidStateError: readyState is CLOSED (3)

// Cause 3: Playing media before it has loaded enough data
const video = document.getElementById("video");
video.play();  // InvalidStateError if no source is set or data hasn't loaded

// Cause 4: Modifying a closed ReadableStream
const stream = new ReadableStream({ start(c) { c.close(); } });
const reader = stream.getReader();
reader.read();  // InvalidStateError: stream is closed
```

## Solutions

### Fix 1: Wait for the WebSocket to open before sending

```javascript
function createWebSocket(url, onMessage) {
  const ws = new WebSocket(url);
  const messageQueue = [];

  ws.addEventListener("open", () => {
    console.log("WebSocket connected");
    // Send any queued messages
    while (messageQueue.length > 0) {
      const msg = messageQueue.shift();
      ws.send(msg);
    }
  });

  ws.addEventListener("message", (event) => {
    onMessage(event.data);
  });

  ws.addEventListener("error", (err) => {
    console.error("WebSocket error:", err);
  });

  // Safe send: queues if not yet open
  return {
    send(data) {
      if (ws.readyState === WebSocket.OPEN) {
        ws.send(data);
      } else {
        messageQueue.push(data);
      }
    },
    close() {
      ws.close();
    },
  };
}

const socket = createWebSocket("wss://example.com", (msg) => {
  console.log("Received:", msg);
});

socket.send("hello");  // safe: queued if not connected
```

### Fix 2: Check readyState before WebSocket operations

```javascript
function safeWsSend(ws, data) {
  if (ws.readyState !== WebSocket.OPEN) {
    console.error("WebSocket is not open. Current state:", ws.readyState);
    return false;
  }
  ws.send(data);
  return true;
}
```

### Fix 3: Wait for media readiness before playback

```javascript
const video = document.getElementById("my-video");

video.addEventListener("canplay", () => {
  // Now safe to call play()
  video.play().catch((err) => {
    console.error("Playback failed:", err.message);
  });
});

// Also check if source is set
if (!video.src) {
  console.error("No media source set — add a <source> or set video.src");
}
```

### Fix 4: Handle ReadableStream lifecycle correctly

```javascript
async function processStream(readableStream) {
  const reader = readableStream.getReader();

  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) {
        console.log("Stream finished");
        break;
      }
      processChunk(value);
    }
  } catch (err) {
    if (err.name === "InvalidStateError") {
      console.error("Stream was closed or locked during read");
    } else {
      throw err;
    }
  } finally {
    reader.releaseLock();
  }
}
```

## Examples

```javascript
// InvalidStateError when sending XHR after abort
const xhr = new XMLHttpRequest();
xhr.open("GET", "/api/data");
xhr.abort();  // abort the request
xhr.send();   // InvalidStateError: request already aborted

// Fix: check readyState before sending
if (xhr.readyState === XMLHttpRequest.OPENED) {
  xhr.send();
}
```

## Related Errors

- [AbortError]({{< relref "/languages/javascript/aborterror" >}}) — operation was intentionally cancelled.
- [NotAllowedError]({{< relref "/languages/javascript/notallowederror" >}}) — operation was not permitted.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream has already been destroyed.
