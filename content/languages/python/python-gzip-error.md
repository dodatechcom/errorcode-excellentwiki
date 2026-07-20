---
title: "[Solution] Python gzip Error — Gzip Compression and Decompression Errors"
description: "Fix Python gzip errors including BadGzipFile, OSError, decompression errors, and read/write failures. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 235
---

# Python gzip Error — Gzip Compression and Decompression Errors

The `gzip` module provides gzip compression and decompression. Errors involve corrupt files, invalid gzip headers, premature EOF, and I/O failures.

## Common Causes

```python
import gzip

# Error: Decompressing a non-gzip file
with gzip.open("/tmp/not_gzip.txt", "rb") as f:
    f.read()
# gzip.BadGzipFile: Not a gzipped file
```

```python
import gzip

# Error: Corrupt gzip file
with gzip.open("/tmp/corrupt.gz", "rb") as f:
    f.read()
# gzip.BadGzipFile: corrupted gzip stream
```

```python
import gzip

# Error: Writing in wrong mode
with gzip.open("/tmp/data.gz", "wt") as f:
    f.write(b"binary data")
# TypeError: a bytes-like object is required, not 'str'
```

```python
import gzip

# Error: Compressing very large file without streaming
with open("/tmp/huge_file", "rb") as f:
    data = f.read()  # MemoryError for large files
compressed = gzip.compress(data)
```

```python
import gzip

# Error: Seeking in gzip file (not supported)
with gzip.open("/tmp/data.gz", "rb") as f:
    f.seek(100)
# OSError: Seeking is not supported
```

## How to Fix

### Fix 1: Verify File Is Gzip Before Opening

```python
import gzip

def open_gzip_safe(filepath):
    try:
        with gzip.open(filepath, "rb") as f:
            f.read(1)  # Test read
        return gzip.open(filepath, "rb")
    except gzip.BadGzipFile:
        print(f"Not a gzip file: {filepath}")
        return None
```

### Fix 2: Use Correct Read/Write Modes

```python
import gzip

# Binary mode for binary data
with gzip.open("/tmp/data.gz", "wb") as f:
    f.write(b"Hello, World!")

# Text mode for strings
with gzip.open("/tmp/data.gz", "wt") as f:
    f.write("Hello, World!")

# Always use rb for reading
with gzip.open("/tmp/data.gz", "rb") as f:
    data = f.read()
```

### Fix 3: Stream Large Files Instead of Loading Into Memory

```python
import gzip

# Stream compression of large files
def compress_large(input_path, output_path):
    with open(input_path, "rb") as f_in:
        with gzip.open(output_path, "wb") as f_out:
            while True:
                chunk = f_in.read(65536)  # 64KB chunks
                if not chunk:
                    break
                f_out.write(chunk)

compress_large("/tmp/huge_file", "/tmp/huge_file.gz")
```

### Fix 4: Use io.BytesIO for In-Memory Gzip

```python
import gzip
import io

# Compress in memory
buffer = io.BytesIO()
with gzip.GzipFile(fileobj=buffer, mode="wb") as gz:
    gz.write(b"Hello, World!")
compressed_data = buffer.getvalue()

# Decompress in memory
buffer = io.BytesIO(compressed_data)
with gzip.GzipFile(fileobj=buffer, mode="rb") as gz:
    decompressed = gz.read()
print(decompressed)  # b'Hello, World!'
```

## Examples

```python
import gzip
import os

# Safe gzip operations
def safe_gzip_compress(input_path, output_path):
    try:
        with open(input_path, "rb") as f_in:
            with gzip.open(output_path, "wb") as f_out:
                while True:
                    chunk = f_in.read(8192)
                    if not chunk:
                        break
                    f_out.write(chunk)
        return True
    except OSError as e:
        print(f"Gzip error: {e}")
        return False

def safe_gzip_decompress(input_path, output_path):
    try:
        with gzip.open(input_path, "rb") as f_in:
            with open(output_path, "wb") as f_out:
                while True:
                    chunk = f_in.read(8192)
                    if not chunk:
                        break
                    f_out.write(chunk)
        return True
    except gzip.BadGzipFile as e:
        print(f"Not a valid gzip file: {e}")
        return False
    except OSError as e:
        print(f"Gzip error: {e}")
        return False

# Usage
safe_gzip_compress("large_file.txt", "large_file.txt.gz")
safe_gzip_decompress("large_file.txt.gz", "restored_file.txt")
```

## Related Errors

- [Python OSError](/languages/python/python-oserror/)
- [Python EOFError](/languages/python/python-eoferror/)
- [Python ValueError](/languages/python/python-valueerror/)
