---
title: "[Solution] Express Range Request Error"
description: "Fix Express range request errors when partial content responses fail or return incorrect byte ranges."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A range request error in Express occurs when the server does not properly handle `Range` headers for partial content, causing media streaming, file downloads, or resume functionality to fail.

## Common Causes

- `Range` header not parsed by the server
- Response does not include `Content-Range` header
- Multiple range requests not supported
- File read offset calculation is incorrect
- `Accept-Ranges` header missing from initial response

## How to Fix

1. Implement range request handling for file serving:

```javascript
const fs = require('fs');

app.get('/video/:id', (req, res) => {
  const filePath = `/videos/${req.id}.mp4`;
  const stat = fs.statSync(filePath);
  const fileSize = stat.size;

  res.set('Accept-Ranges', 'bytes');

  const range = req.headers.range;
  if (range) {
    const parts = range.replace(/bytes=/, '').split('-');
    const start = parseInt(parts[0], 10);
    const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;
    const chunkSize = end - start + 1;

    const file = fs.createReadStream(filePath, { start, end });
    res.writeHead(206, {
      'Content-Range': `bytes ${start}-${end}/${fileSize}`,
      'Accept-Ranges': 'bytes',
      'Content-Length': chunkSize,
      'Content-Type': 'video/mp4'
    });
    file.pipe(res);
  } else {
    res.writeHead(200, {
      'Content-Length': fileSize,
      'Content-Type': 'video/mp4'
    });
    fs.createReadStream(filePath).pipe(res);
  }
});
```

2. Use a streaming library for proper range support:

```javascript
const rangeParser = require('range-parser');

app.get('/audio/:id', (req, res) => {
  const filePath = `/audio/${id}.mp3`;
  const stat = fs.statSync(filePath);
  const range = req.headers.range;

  if (range) {
    const [start, end] = rangeParser(stat.size, range)[0];
    const stream = fs.createReadStream(filePath, { start, end });
    res.writeHead(206, {
      'Content-Range': `bytes ${start}-${end}/${stat.size}`,
      'Accept-Ranges': 'bytes',
      'Content-Length': end - start + 1,
      'Content-Type': 'audio/mpeg'
    });
    stream.pipe(res);
  } else {
    res.writeHead(200, { 'Content-Length': stat.size, 'Content-Type': 'audio/mpeg' });
    fs.createReadStream(filePath).pipe(res);
  }
});
```

## Examples

```javascript
// Bug: no range support -- video cannot be seeked
app.get('/stream/:id', (req, res) => {
  const file = fs.createReadStream(`/media/${req.params.id}.mp4`);
  file.pipe(res); // Always sends full file
});

// Fixed: supports Range header for seeking
app.get('/stream/:id', (req, res) => {
  const stat = fs.statSync(`/media/${req.params.id}.mp4`);
  const range = req.headers.range;
  if (range) {
    const [start, end] = rangeParser(stat.size, range)[0];
    fs.createReadStream(`/media/${req.params.id}.mp4`, { start, end }).pipe(res);
  } else {
    res.set('Accept-Ranges', 'bytes');
    fs.createReadStream(`/media/${req.params.id}.mp4`).pipe(res);
  }
});
```

```text
416 Range Not Satisfiable
```
