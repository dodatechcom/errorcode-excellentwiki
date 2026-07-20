---
title: "[Solution] Pascal BlockWrite Error — How to Fix"
description: "Fix BlockWrite errors in Pascal when performing binary block output operations on files."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1052
---

# BlockWrite Error

`BlockWrite` writes a block of bytes from a buffer to a typed file. Errors occur when the disk is full, the file is read-only, or the buffer address is invalid.

## Common Causes

- Disk full — `BlockWrite` cannot write all bytes
- File opened with `Reset` (read-only) instead of `Rewrite`
- Writing more bytes than the file can hold (disk quota)
- Invalid buffer pointer or uninitialized buffer

## How to Fix

### Solution 1 — Check disk space before writing

```pascal
program SafeBlockWrite;

var
  F: file;
  Buf: array[0..1023] of Byte;
  Count: Integer;
begin
  AssignFile(F, 'output.bin');
  Rewrite(F, 1);
  FillChar(Buf, SizeOf(Buf), $AA);
  BlockWrite(F, Buf, SizeOf(Buf), Count);
  if Count < SizeOf(Buf) then
    WriteLn('Warning: only wrote ', Count, ' of ', SizeOf(Buf), ' bytes');
  CloseFile(F);
end.
```

### Solution 2 — Handle disk-full gracefully

```pascal
program DiskFullHandling;

var
  F: file;
  Buf: array[0..4095] of Byte;
  Written, Total: Integer;
begin
  AssignFile(F, 'output.bin');
  Rewrite(F, 1);
  Total := 0;
  repeat
    FillChar(Buf, SizeOf(Buf), $00);
    BlockWrite(F, Buf, SizeOf(Buf), Written);
    Total := Total + Written;
  until Written = 0;
  WriteLn('Wrote ', Total, ' bytes');
  CloseFile(F);
end.
```

### Solution 3 — Append to existing data

```pascal
program AppendBlock;

var
  F: file;
  Data: Integer;
  Count: Integer;
begin
  AssignFile(F, 'numbers.bin');
  Reset(F, 1);
  Seek(F, FileSize(F));    // move to end
  Data := 42;
  BlockWrite(F, Data, SizeOf(Data), Count);
  CloseFile(F);
end.
```

### Solution 4 — Write header then data

```pascal
program WriteWithHeader;

type
  TFileHeader = record
    Magic: Cardinal;
    RecordCount: Integer;
  end;

var
  F: file;
  H: TFileHeader;
  Records: array[0..99] of Integer;
  Count: Integer;
begin
  AssignFile(F, 'database.bin');
  Rewrite(F, 1);

  H.Magic := $DEADBEEF;
  H.RecordCount := 100;
  BlockWrite(F, H, SizeOf(H), Count);

  FillChar(Records, SizeOf(Records), 0);
  BlockWrite(F, Records, SizeOf(Records), Count);

  CloseFile(F);
end.
```

## Examples

A data acquisition system writes sensor readings via `BlockWrite`. When the disk fills up, only a partial write occurs. The code does not check the count parameter and assumes all data was written, leading to corrupted files.

## Related Errors

- [BlockRead Error](/languages/pascal/pascal-blockread-error) — block input
- [IO Error](/languages/pascal/io-error) — I/O failures
- [Seek Error](/languages/pascal/pascal-seek-error) — position errors
