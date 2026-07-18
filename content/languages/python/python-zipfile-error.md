---
title: "[Solution] Python zipfile Error — How to Fix"
description: "Fix Python zipfile errors. Resolve corruption, path traversal, and extraction issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python zipfile Error

A `zipfile.BadZipFile` occurs when Reading or writing ZIP files fails due to corruption, unsupported compression, or path traversal..

## Why It Happens

This happens when ZIP file is corrupted, uses unsupported compression, or contains path traversal. Python enforces strict type and state checking.

## Common Error Messages

- `File is not a zip file`
- `Bad magic number for zip header`
- `Truncated file header`

## How to Fix It

### Fix 1: Validate zip files

```python
import zipfile
try:
    with zipfile.ZipFile('archive.zip', 'r') as zf:
        zf.testzip()
except zipfile.BadZipFile:
    print('Invalid zip file')
```

### Fix 2: Fix path traversal

```python
import zipfile
with zipfile.ZipFile('archive.zip', 'r') as zf:
    for name in zf.namelist():
        if '..' in name:
            raise ValueError(f'Path traversal: {name}')
```

### Fix 3: Compression types

```python
import zipfile
with zipfile.ZipFile('archive.zip', 'w') as zf:
    zf.write('file.txt', compress_type=zipfile.ZIP_DEFLATED)
```

### Fix 4: Extract safely

```python
import zipfile
with zipfile.ZipFile('archive.zip', 'r') as zf:
    zf.extractall('safe_directory/')
```

## Common Scenarios

- **Corrupted downloads** — ZIP files truncated during download.
- **Unsupported compression** — ZIP files using unsupported methods.
- **Large ZIPs** — ZIP files exceeding memory limits.

## Prevent It

- Always validate ZIP files before extraction
- Check for path traversal in ZIP entries
- Use try/except for BadZipFile

## Related Errors

- - [OSError](/languages/python/oserror/) — system call error
- - [FileNotFoundError](/languages/python/filenotfounderror/) — file not found
