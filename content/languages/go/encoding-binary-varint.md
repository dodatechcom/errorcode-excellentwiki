---
title: "[Solution] Go encoding/binary: varint overflows — Encoding Error Fix"
description: "Fix Go binary varint overflow error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# encoding/binary: varint overflow

The error `binary: varint overflows` occurs when decoding a malformed varint.

## How to Fix

### Fix 1: Use io.ReadFull before decoding

```go
buf := make([]byte, binary.MaxVarintLen64)
_, err := io.ReadFull(r, buf)
if err != nil { return err }
n, _ := binary.Uvarint(buf)
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of file.
- [unexpected-eof]({{< relref "/languages/go/unexpected-eof" >}}) — unexpected EOF.
