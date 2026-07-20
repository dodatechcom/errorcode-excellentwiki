---
title: "[Solution] Pascal FileSize Error — How to Fix"
description: "Fix FileSize errors in Pascal when querying the size of an unopened or invalid file."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1055
---

# FileSize Error

`FileSize` returns the number of records (or bytes for byte-sized files) in an opened file. Errors occur when the file is not open, or for text files where `FileSize` is not directly usable.

## Common Causes

- Calling `FileSize` on a file that is not open
- Using `FileSize` on a text file (undefined behavior)
- File was deleted while the file variable was still assigned
- Integer overflow for files larger than MaxInt records

## How to Fix

### Solution 1 — Open file before querying size

```pascal
program SafeFileSize;

var
  F: file of Integer;
  Count: Integer;
begin
  AssignFile(F, 'data.bin');
  Reset(F);
  Count := FileSize(F);   // number of Integer records
  WriteLn('Records: ', Count);
  CloseFile(F);
end.
```

### Solution 2 — Get byte size of typed file

```pascal
program ByteSize;

var
  F: file of Integer;
begin
  AssignFile(F, 'data.bin');
  Reset(F);
  WriteLn('Records: ', FileSize(F));
  WriteLn('Bytes: ', FileSize(F) * SizeOf(Integer));
  CloseFile(F);
end.
```

### Solution 3 — Use for typed file bounds

```pascal
program BoundsCheck;

var
  F: file of Integer;
  N: Integer;
begin
  AssignFile(F, 'data.bin');
  Reset(F);
  for N := 0 to FileSize(F) - 1 do
  begin
    Seek(F, N);
    Read(F, N);
  end;
  CloseFile(F);
end.
```

### Solution 4 — Get byte size for raw file

```pascal
program RawFileSize;

var
  F: file;
begin
  AssignFile(F, 'big.bin');
  Reset(F, 1);            // byte-sized records
  WriteLn('File size: ', FileSize(F), ' bytes');
  CloseFile(F);
end.
```

## Examples

A backup utility reads a file in chunks. It uses `FileSize(F) * SizeOf(TRecord)` to calculate total size. If the file has more records than `MaxInt div SizeOf(TRecord)`, the multiplication overflows. Using `FileSize(F)` directly with record-sized reads avoids the overflow.

## Related Errors

- [FilePos Error](/languages/pascal/pascal-filepos-error) — current position
- [Seek Error](/languages/pascal/pascal-seek-error) — positioning
- [IO Error](/languages/pascal/io-error) — I/O failures
