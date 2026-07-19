---
title: "[Solution] ERR_BUFFER_OUT_OF_BOUNDS — Buffer Index Out of Range Fix"
description: "Fix ERR_BUFFER_OUT_OF_BOUNDS when reading/writing beyond buffer length in Node.js."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_BUFFER_OUT_OF_BOUNDS

Buffer read/write operation exceeds buffer boundaries.

## Fix

```javascript
const buf = Buffer.alloc(4);

// Wrong — index 10 doesn't exist
buf.readInt32BE(10); // ERR_BUFFER_OUT_OF_BOUNDS

// Check length first
if (offset + size <= buf.length) {
  buf.readInt32BE(offset);
}
```
