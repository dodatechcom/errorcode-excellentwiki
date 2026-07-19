---
title: "[Solution] ERR_STREAM_PUSH_AFTER_END — Stream Push After End Fix"
description: "Fix ERR_STREAM_PUSH_AFTER_END when pushing data to a readable stream after it has ended."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_STREAM_PUSH After End

```javascript
const { Readable } = require('stream');

class MyStream extends Readable {
  _read(size) {
    // Don't push after calling this.push(null)
    this.push(null); // signals end
    this.push('data'); // ERR_STREAM_PUSH_AFTER_END
  }
}
```

## Fix

Track end state:

```javascript
class MyStream extends Readable {
  constructor() {
    super();
    this._ended = false;
  }
  _read(size) {
    if (this._ended) return;
    this._ended = true;
    this.push('data');
    this.push(null);
  }
}
```
