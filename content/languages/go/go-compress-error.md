---
title: "[Solution] compress/gzip Read Error Fix"
description: "Fix Go gzip compression errors. Handle invalid gzip data, buffer issues, and decompression failures."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# compress/gzip Read Error

The `compress/gzip` package fails when reading gzip-compressed data due to wrong magic bytes, the reader is not closed to flush the footer, the data is not actually gzip-compressed, or the decompressed data exceeds memory limits. Gzip readers must be fully consumed and closed to verify data integrity.

## Common Causes

```go
// Cause 1: Data is not gzip-compressed
reader, err := gzip.NewReader(bytes.NewReader(data))
// gzip: invalid header

// Cause 2: Reader not closed — footer not verified
reader, _ := gzip.NewReader(file)
io.Copy(buf, reader)
// forgot: reader.Close() — may miss corruption errors

// Cause 3: Wrong compression level used for writing
writer, _ := gzip.NewWriterLevel(buf, gzip.BestCompression)
// Much slower, but not wrong — just performance issue

// Cause 4: Concurrent reads on same gzip.Reader
// gzip.Reader is not safe for concurrent use

// Cause 5: Truncated gzip stream
// Network transfer interrupted mid-stream
reader, _ := gzip.NewReader(truncatedData)
io.Copy(buf, reader) // may succeed with partial data
reader.Close() // error: unexpected EOF
```

## How to Fix

### Fix 1: Always close the gzip reader to verify integrity

```go
import (
    "compress/gzip"
    "fmt"
    "io"
    "os"
)

func decompressFile(path string) ([]byte, error) {
    f, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer f.Close()

    reader, err := gzip.NewReader(f)
    if err != nil {
        return nil, fmt.Errorf("gzip reader: %w", err)
    }
    defer reader.Close()

    data, err := io.ReadAll(reader)
    if err != nil {
        return nil, fmt.Errorf("read: %w", err)
    }
    return data, nil
}
```

### Fix 2: Use gzip.NewReader with proper error handling

```go
func decompressWithHeader(r io.Reader) ([]byte, error) {
    reader, err := gzip.NewReader(r)
    if err != nil {
        return nil, err
    }
    defer reader.Close()

    // Read gzip metadata
    fmt.Println("Comment:", reader.Comment)
    fmt.Println("Extra:", reader.Extra)

    return io.ReadAll(reader)
}
```

### Fix 3: Compress with appropriate level

```go
func compressData(data []byte) ([]byte, error) {
    var buf bytes.Buffer
    writer, err := gzip.NewWriterLevel(&buf, gzip.DefaultCompression)
    if err != nil {
        return nil, err
    }

    if _, err := writer.Write(data); err != nil {
        return nil, err
    }
    if err := writer.Close(); // important: flushes footer
    err != nil {
        return nil, err
    }
    return buf.Bytes(), nil
}
```

## Examples

```go
package main

import (
    "bytes"
    "compress/gzip"
    "fmt"
    "io"
    "log"
)

func main() {
    original := []byte("Hello, gzip compression!")

    // Compress
    var compressed bytes.Buffer
    writer, _ := gzip.NewWriterLevel(&compressed, gzip.BestCompression)
    writer.Write(original)
    writer.Close()

    fmt.Printf("Original: %d bytes, Compressed: %d bytes\n",
        len(original), compressed.Len())

    // Decompress
    reader, err := gzip.NewReader(&compressed)
    if err != nil {
        log.Fatal(err)
    }
    defer reader.Close()

    decompressed, _ := io.ReadAll(reader)
    fmt.Printf("Decompressed: %s\n", string(decompressed))
}
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — unexpected end of compressed stream
- [go-archive-error]({{< relref "/languages/go/go-archive-error" >}}) — archive/tar header errors
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — decompression bomb exhausting memory
