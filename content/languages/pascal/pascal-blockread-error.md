---
title: "[Solution] Pascal BlockRead Error — How to Fix"
description: "Fix BlockRead errors in Pascal when performing binary block I/O operations on files."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1051
---

# BlockRead Error

`BlockRead` reads a block of bytes from a typed file into a buffer. Errors occur when reading past EOF, buffer size mismatch, or file not opened in read mode.

## Common Causes

- `BlockRead` count exceeds remaining bytes in file
- Buffer not large enough for the requested block count
- File not opened with `Reset` before `BlockRead`
- Reading from a text file (only works on typed files)

## How to Fix

### Solution 1 — Check file size before reading

```pascal
program SafeBlockRead;

type
  THeader = record
    Magic: Integer;
    Version: Word;
  end;

var
  F: file;
  H: THeader;
  BytesRead: Integer;
begin
  AssignFile(F, 'data.bin');
  Reset(F, 1);           // byte-sized records
  if FileSize(F) >= SizeOf(H) then
  begin
    BlockRead(F, H, SizeOf(H), BytesRead);
    WriteLn('Read ', BytesRead, ' bytes');
  end;
  CloseFile(F);
end.
```

### Solution 2 — Read variable-count blocks

```pascal
program VariableBlockRead;

var
  F: file;
  Buf: array[0..4095] of Byte;
  Count: Integer;
  Total: Integer;
begin
  AssignFile(F, 'large.bin');
  Reset(F, 1);
  Total := 0;
  repeat
    BlockRead(F, Buf, SizeOf(Buf), Count);
    Total := Total + Count;
  until Count = 0;
  WriteLn('Total bytes: ', Total);
  CloseFile(F);
end.
```

### Solution 3 — Handle partial reads

```pascal
program PartialRead;

var
  F: file;
  Buf: array[0..255] of Byte;
  ActualCount: Integer;
begin
  AssignFile(F, 'small.bin');
  Reset(F, 1);
  BlockRead(F, Buf, SizeOf(Buf), ActualCount);
  if ActualCount < SizeOf(Buf) then
    WriteLn('Partial read: ', ActualCount, ' of ', SizeOf(Buf));
  CloseFile(F);
end.
```

### Solution 4 — Write with BlockWrite for symmetric I/O

```pascal
program BlockReadWrite;

var
  Fin, Fout: file;
  Buf: array[0..4095] of Byte;
  Count: Integer;
begin
  AssignFile(Fin, 'input.bin');
  Reset(Fin, 1);
  AssignFile(Fout, 'output.bin');
  Rewrite(Fout, 1);
  repeat
    BlockRead(Fin, Buf, SizeOf(Buf), Count);
    if Count > 0 then
      BlockWrite(Fout, Buf, Count);
  until Count = 0;
  CloseFile(Fin);
  CloseFile(Fout);
end.
```

## Examples

A file copy utility uses `BlockRead` with a 64KB buffer. If the file is smaller than 64KB, the count parameter returns the actual bytes read. Not checking the count causes processing of uninitialized buffer data.

## Related Errors

- [BlockWrite Error](/languages/pascal/pascal-blockwrite-error) — block output
- [Typed File Error](/languages/pascal/pascal-typed-file-error) — binary file mode
- [IO Error](/languages/pascal/io-error) — I/O failures
