---
title: "[Solution] ERR_FILE_TOO_LARGE — File Size Limit Exceeded Fix"
description: "Fix ERR_FILE_TOO_LARGE when a file exceeds the maximum allowed size for processing."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_FILE_TOO_LARGE

```javascript
const fs = require('fs');
const stat = fs.statSync('large-file.bin');

const MAX_SIZE = 100 * 1024 * 1024; // 100MB
if (stat.size > MAX_SIZE) {
  throw new Error('File too large');
}
```

For large files, use streaming:

```javascript
const { createReadStream } = require('fs');
const stream = createReadStream('large-file.bin', {
  highWaterMark: 64 * 1024
});
```
