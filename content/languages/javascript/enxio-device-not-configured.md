---
title: "[Solution] ENXIO — No Such Device or Address Error"
description: "Fix ENXIO errors in Node.js when accessing a device or address that doesn't exist."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ENXIO — No Such Device or Address

The system cannot locate the specified device or address.

## Causes

- Serial port doesn't exist
- FIFO pipe not connected
- NFS mount disconnected

```javascript
// Check device exists before opening
const fs = require('fs');
if (fs.existsSync('/dev/ttyUSB0')) {
  // open device
}
```
