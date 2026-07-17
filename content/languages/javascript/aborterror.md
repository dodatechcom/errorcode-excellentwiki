---
title: "[Solution] JavaScript AbortError — Operation Aborted Fix"
description: "Fix JavaScript AbortError when async operations are cancelled. Handle AbortController signals, clean up listeners, and manage timeouts properly."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# AbortError — Operation Aborted Fix

An `AbortError` is thrown when an asynchronous operation is cancelled before it completes. This typically occurs when an `AbortController` signal is triggered, a user navigates away from a page while a Promise is pending, or a timeout mechanism cancels the operation.

## Description

Common AbortError messages include:

- `AbortError: The user aborted a request` — the user navigated away or closed the tab.
- `AbortError: The operation was aborted` — an `AbortController` signal was triggered.
- `AbortError: Fetch is aborted` — `fetch()` was aborted via its signal option.

AbortError is a DOMException subclass and cannot be prevented — it only indicates the operation was intentionally cancelled.

## Common Causes

```javascript
// Cause 1: AbortController triggered
const controller = new AbortController();
fetch("/api/slow-endpoint", { signal: controller.signal })
  .then(res => res.json())
  .catch(err => {
    if (err.name === "AbortError") {
      console.log("Request was cancelled");
    }
  });

controller.abort();  // triggers AbortError

// Cause 2: User navigated away during a pending request
// Browser aborts all pending fetch() calls on page unload

// Cause 3: Timeout using AbortController
const timeoutId = setTimeout(() => controller.abort(), 5000);

// Cause 4: Signal passed to a synchronous operation
// AbortController only works with async operations that support signals
```

## Solutions

### Fix 1: Handle AbortError in fetch requests

```javascript
async function fetchWithTimeout(url, options = {}, timeoutMs = 10000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
    });
    clearTimeout(timeoutId);
    return response;
  } catch (err) {
    clearTimeout(timeoutId);
    if (err.name === "AbortError") {
      console.error(`Request to ${url} timed out after ${timeoutMs}ms`);
      return null;
    }
    throw err;
  }
}

// Usage
const data = await fetchWithTimeout("/api/data", {}, 5000);
```

### Fix 2: Cancel only when needed with clean signal propagation

```javascript
async function loadData() {
  const controller = new AbortController();

  // Only abort on explicit user action, not page unload
  document.getElementById("cancel-btn").addEventListener("click", () => {
    controller.abort();
  });

  try {
    const res = await fetch("/api/heavy-data", {
      signal: controller.signal,
    });
    const data = await res.json();
    renderData(data);
  } catch (err) {
    if (err.name === "AbortError") {
      console.log("Load cancelled by user");
      showCancelledMessage();
    } else {
      throw err;
    }
  }
}
```

### Fix 3: Use Promise.race for timeout without AbortController

```javascript
function fetchWithRace(url, timeoutMs = 5000) {
  const fetchPromise = fetch(url).then(res => res.json());

  const timeoutPromise = new Promise((_, reject) => {
    setTimeout(() => reject(new Error("Request timed out")), timeoutMs);
  });

  return Promise.race([fetchPromise, timeoutPromise]);
}

// Usage
try {
  const data = await fetchWithRace("/api/data", 3000);
} catch (err) {
  if (err.message === "Request timed out") {
    console.error("Request took too long");
  }
}
```

### Fix 4: Avoid AbortError on page navigation

```javascript
// Don't pass AbortController signals that fire on page unload
// The browser handles this automatically for fetch() — let it

// Instead, use beforeunload to warn users
window.addEventListener("beforeunload", (e) => {
  if (isUploadInProgress) {
    e.preventDefault();
    e.returnValue = "Upload still in progress. Are you sure?";
  }
});
```

## Examples

```javascript
// AbortError when cancelling a ReadableStream
async function streamWithAbort(url) {
  const controller = new AbortController();

  const response = await fetch(url, { signal: controller.signal });
  const reader = response.body.getReader();

  // Cancel after processing 1MB
  let bytesReceived = 0;
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    bytesReceived += value.length;
    if (bytesReceived > 1_000_000) {
      controller.abort();  // AbortError on next fetch call using this signal
      break;
    }
  }
}
```

## Related Errors

- [NotFoundError]({{< relref "/languages/javascript/notfounderror" >}}) — resource could not be located.
- [NotAllowedError]({{< relref "/languages/javascript/notallowederror" >}}) — operation was not permitted.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream already destroyed.
