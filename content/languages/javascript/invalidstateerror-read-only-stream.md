---
title: "[Solution] InvalidStateError — ReadableStream Locked or Already Used Fix"
description: "Fix InvalidStateError when a ReadableStream is already consumed or locked by a reader."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ReadableStream InvalidStateError

```javascript
const response = await fetch('/api');
const reader = response.body.getReader();
const reader2 = response.body.getReader(); // InvalidStateError: locked

// Fix — consume once
async function readStream(stream) {
  const reader = stream.getReader();
  const chunks = [];
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    chunks.push(value);
  }
  return new Uint8Array(chunks.reduce((a, b) => a + b.length, 0));
}
```
