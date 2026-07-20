---
title: "[Solution] encoding/binary Read Error Fix"
description: "Fix Go binary read errors. Handle buffer overflow, endianness, and data alignment issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# encoding/binary Read Error

The `encoding/binary` package returns errors when the buffer is too small for the requested type, data is malformed, or there is an endianness mismatch. This breaks network protocol parsers, file format readers, and C struct interop.

## Common Causes

```go
// Cause 1: Buffer too small for the target type
var num int64
buf := make([]byte, 4) // only 4 bytes, but int64 needs 8
err := binary.Read(bytes.NewReader(buf), binary.LittleEndian, &num)
// error: unexpected EOF

// Cause 2: Endianness mismatch between writer and reader
binary.BigEndian.PutUint32(buf, 42)
binary.Read(bytes.NewReader(buf), binary.LittleEndian, &val) // wrong value

// Cause 3: Struct field alignment issues
type Bad struct {
    A byte
    B uint32 // 3-byte padding inserted by binary.Read
}

// Cause 4: Reading from a partially consumed reader
reader := bytes.NewReader([]byte{0, 0, 0, 1, 0, 0, 0, 2})
binary.Read(reader, binary.BigEndian, &val1)
binary.Read(reader, binary.BigEndian, &val2) // offset mistakes cause EOF
```

## How to Fix

### Fix 1: Ensure buffer size matches the target type

```go
import (
    "bytes"
    "encoding/binary"
    "fmt"
)

func readUint32(data []byte) (uint32, error) {
    if len(data) < 4 {
        return 0, fmt.Errorf("buffer too small: need 4 bytes, got %d", len(data))
    }
    return binary.BigEndian.Uint32(data[:4]), nil
}
```

### Fix 2: Use the same endianness for encode and decode

```go
func encodeUint32(val uint32) []byte {
    buf := make([]byte, 4)
    binary.LittleEndian.PutUint32(buf, val)
    return buf
}

func decodeUint32(data []byte) uint32 {
    return binary.LittleEndian.Uint32(data)
}
```

### Fix 3: Control struct layout with explicit padding

```go
type RawHeader struct {
    A byte
    _ [3]byte // explicit padding
    B uint32
}
```

## Examples

```go
package main

import (
    "bytes"
    "encoding/binary"
    "fmt"
    "log"
)

type Record struct {
    ID    uint32
    Score float64
}

func main() {
    buf := new(bytes.Buffer)
    rec := Record{ID: 12345, Score: 99.5}
    if err := binary.Write(buf, binary.BigEndian, rec); err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Encoded %d bytes: %x\n", buf.Len(), buf.Bytes())

    var decoded Record
    if err := binary.Read(bytes.NewReader(buf.Bytes()), binary.BigEndian, &decoded); err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Decoded: ID=%d Score=%.1f\n", decoded.ID, decoded.Score)
}
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — unexpected end of data during binary read
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — similar struct-tag issues with JSON encoding
- [index-out-of-range]({{< relref "/languages/go/slice-bounds" >}}) — buffer access beyond allocated length
