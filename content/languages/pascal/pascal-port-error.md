---
title: "[Solution] Pascal PORT and PORTW Error"
description: "Fix Pascal PORT and PORTW errors when accessing hardware I/O ports directly."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

PORT and PORTW errors occur when accessing hardware ports that are restricted or do not exist.

## Common Causes

- Accessing port without privilege level
- Port address does not exist
- PORTW on 32-bit systems (not supported)
- Port access conflicts with device drivers

## How to Fix

### 1. Check port availability

```pascal
var
  Value: Byte;
begin
  Value := Port[$3FD];  // read from serial port
end;
```

### 2. Use PORT for byte access

```pascal
Port[$3F8] := ByteValue;  // write to port
```

## Examples

```pascal
program PortDemo;

var
  Status: Byte;

begin
  Status := Port[$3FD];  // COM1 line status
  WriteLn('Port status: ', Status);
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Permission denied](/languages/pascal/pascal-file-locking-error)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
