---
title: "[Solution] Express Path Traversal Error"
description: "Fix Express path traversal errors when file access is vulnerable to directory navigation attacks."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A path traversal error in Express occurs when user-controlled input is used to construct file paths without sanitization, allowing attackers to access files outside the intended directory using sequences like `../`.

## Common Causes

- User input directly used in `path.join()` or `fs.readFile()` without validation
- Static file serving configured with overly broad root directories
- Download handler constructs file path from request parameter
- Template includes or partials resolved from user input
- No sanitization of `..` sequences in file path parameters

## How to Fix

1. Sanitize file paths and verify they stay within the allowed directory:

```javascript
const path = require('path');

app.get('/download/:filename', (req, res) => {
  const uploadDir = path.join(__dirname, 'uploads');
  const filePath = path.join(uploadDir, req.params.filename);

  // Verify resolved path is within uploadDir
  if (!filePath.startsWith(uploadDir)) {
    return res.status(403).json({ error: 'Access denied' });
  }

  res.download(filePath);
});
```

2. Use `path.resolve` and compare against the allowed root:

```javascript
const fs = require('fs');

function safePath(baseDir, userPath) {
  const resolved = path.resolve(baseDir, userPath);
  if (!resolved.startsWith(baseDir)) {
    throw new Error('Path traversal detected');
  }
  return resolved;
}

app.get('/files/*', (req, res) => {
  try {
    const filePath = safePath('/var/www/files', req.params[0]);
    const content = fs.readFileSync(filePath);
    res.send(content);
  } catch (err) {
    res.status(403).json({ error: 'Access denied' });
  }
});
```

3. Use a whitelist of allowed filenames instead of user-provided names:

```javascript
const allowedFiles = ['report.pdf', 'invoice.pdf', 'summary.csv'];

app.get('/download/:file', (req, res) => {
  if (!allowedFiles.includes(req.params.file)) {
    return res.status(404).json({ error: 'File not found' });
  }
  res.download(path.join(__dirname, 'files', req.params.file));
});
```

## Examples

```javascript
// Vulnerable: direct use of user input
app.get('/view/:page', (req, res) => {
  res.sendFile(path.join(__dirname, 'pages', req.params.page));
  // GET /view/../../../etc/passwd accesses system files
});

// Safe: path traversal prevention
app.get('/view/:page', (req, res) => {
  const pagesDir = path.join(__dirname, 'pages');
  const filePath = path.join(pagesDir, req.params.page);
  if (!filePath.startsWith(pagesDir)) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  res.sendFile(filePath);
});
```

```text
Error: ENOENT: no such file or directory, access '../../etc/passwd'
```
