---
title: "[Solution] ERR_STREAM_PREMATURE_CLOSE — Stream Destroyed Before Finish Fix"
description: "Fix ERR_STREAM_PREMATURE_CLOSE when a stream is destroyed before all data is consumed."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_STREAM_PREMATURE_CLOSE

The stream was destroyed before the operation completed.

## Causes

- Client disconnected
- Request aborted
- Pipe destination errored

```javascript
const { pipeline } = require('stream');
const { promisify } = require('util');
const pipelineAsync = promisify(pipeline);

// Use pipeline for automatic cleanup
await pipelineAsync(
  fs.createReadStream('input.txt'),
  zlib.createGzip(),
  fs.createWriteStream('output.txt.gz')
);
```
