---
title: "[Solution] ERR_STREAM_WRITE_AFTER_END — Write to Closed Stream Fix"
description: "Fix ERR_STREAM_WRITE_AFTER_END when writing to a stream that has already ended."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_STREAM_WRITE After End

```javascript
const stream = require('stream');

const writable = new stream.Writable({
  write(chunk, encoding, callback) {
    callback();
  }
});

writable.end();
writable.write('data'); // ERR_STREAM_WRITE_AFTER_END

// Fix — check if writable before writing
if (!writable.destroyed && !writable.writableEnded) {
  writable.write('data');
}
```
