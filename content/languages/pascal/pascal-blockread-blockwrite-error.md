---
title: "[Solution] Pascal BLOCKREAD/BLOCKWRITE Error"
description: "Fix Pascal BLOCKREAD and BLOCKWRITE errors when performing unformatted binary file I/O."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

BLOCKREAD and BLOCKWRITE errors occur when reading or writing binary data blocks with incorrect sizes or to files not opened in binary mode.

## Common Causes

- File not opened for untyped I/O
- Block size exceeds buffer size
- Reading past end of file
- BLOCKWRITE to read-only file

## How to Fix

### 1. Open files for untyped I/O

```pascal
var
  f: File;
  Buf: array[1..512] of Byte;
  Count: Integer;
begin
  Assign(f, 'data.bin');
  Reset(f, 1);  // record size = 1 byte
  BlockRead(f, Buf, SizeOf(Buf), Count);
  CloseFile(f);
end;
```

### 2. Check BytesRead

```pascal
BlockRead(f, Buf, SizeOf(Buf), BytesRead);
if BytesRead < SizeOf(Buf) then
  WriteLn('Partial read: ', BytesRead, ' bytes');
```

## Examples

```pascal
program BlockIODemo;

var
  f: File;
  Buffer: array[1..100] of Byte;
  BytesRead: Integer;

begin
  Assign(f, 'binary.dat');
  Reset(f, 1);
  BlockRead(f, Buffer, SizeOf(Buffer), BytesRead);
  WriteLn('Read ', BytesRead, ' bytes');
  CloseFile(f);
end.
```

## Related Errors

- [File not found](/languages/pascal/pascal-file-not-found)
- [File mode error](/languages/pascal/pascal-file-mode-error)
- [Runtime error](/languages/pascal/pascal-runtime-error)
