---
title: "[Solution] Pascal Seek Error — How to Fix"
description: "Fix Seek errors in Pascal when positioning a file pointer outside valid bounds."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1053
---

# Seek Error

`Seek` moves the file position to a specified record or byte offset. Errors occur when seeking to a negative position, beyond `FileSize`, or on a text file.

## Common Causes

- Seeking to a negative offset
- Seeking beyond `FileSize` without extending the file
- Using `Seek` on a text file (not supported)
- Integer overflow in the seek offset for large files

## How to Fix

### Solution 1 — Validate seek position

```pascal
program SafeSeek;

var
  F: file of Integer;
  N: Integer;
begin
  AssignFile(F, 'data.bin');
  Reset(F);
  N := 10;
  if N < FileSize(F) then
  begin
    Seek(F, N);
    Read(F, N);
    WriteLn('Value: ', N);
  end
  else
    WriteLn('Index out of range');
  CloseFile(F);
end.
```

### Solution 2 — Extend file with Seek + Write

```pascal
program ExtendFile;

var
  F: file of Integer;
begin
  AssignFile(F, 'sparse.bin');
  Rewrite(F);
  Seek(F, 999);            // jump to record 999
  Write(F, 42);            // file now has 1000 records (0..999)
  CloseFile(F);
end.
```

### Solution 3 — Use FilePos for current position

```pascal
program FilePosDemo;

var
  F: file of Integer;
begin
  AssignFile(F, 'data.bin');
  Reset(F);
  WriteLn('Current position: ', FilePos(F));
  Seek(F, 5);
  WriteLn('After seek: ', FilePos(F));
  CloseFile(F);
end.
```

### Solution 4 — Handle large file seeking with Int64

```pascal
program LargeFileSeek;

var
  F: file;
begin
  AssignFile(F, 'huge.bin');
  Reset(F, 1);
  // Use FileSize which returns Int64 in FPC
  if FileSize(F) > 2000000000 then
    WriteLn('File is larger than 2GB');
  Seek(F, FileSize(F) - 100);
  CloseFile(F);
end.
```

## Examples

A database uses `Seek` to jump to a specific record. The record index is computed from user input. A negative index (from an invalid input) triggers runtime error 5. Adding bounds checking before `Seek` prevents the crash.

## Related Errors

- [FilePos Error](/languages/pascal/pascal-filepos-error) — current position
- [FileSize Error](/languages/pascal/pascal-filesize-error) — file size query
- [IO Error](/languages/pascal/io-error) — I/O failures
