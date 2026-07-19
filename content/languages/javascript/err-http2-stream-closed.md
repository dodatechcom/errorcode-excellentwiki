---
title: "[Solution] ERR_HTTP2_STREAM_CLOSED — HTTP/2 Stream Already Closed Fix"
description: "Fix ERR_HTTP2_STREAM_CLOSED when writing to a closed HTTP/2 stream."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_HTTP2_STREAM Closed

The HTTP/2 stream was closed before the write completed.

## Fix

```javascript
const http2 = require('http2');
const client = http2.connect('https://example.com');

client.on('error', (err) => {
  console.error('Client error:', err.code);
});

const req = client.request({ ':path': '/' });
req.on('error', (err) => {
  if (err.code === 'ERR_HTTP2_STREAM_CLOSED') {
    console.log('Stream closed by server');
  }
});
```
