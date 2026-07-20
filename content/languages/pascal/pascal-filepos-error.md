---
title: "[Solution] Pascal FilePos Error — How to Fix"
description: "Fix FilePos errors in Pascal when querying the current file position of an unpositioned or closed file."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1054
---

# FilePos Error

`FilePos` returns the current position (record number or byte offset) of a file pointer. Errors occur when calling `FilePos` on an unassigned, unopened, or closed file.

## Common Causes

- Calling `FilePos` on a file that was never opened
- File closed before `FilePos` is called
- Using `FilePos` on a text file after `ReadLn` (position is unreliable)
- Calling `FilePos` immediately after `Rewrite` (position is 0, which is valid)

## How to Fix

### Solution 1 — Ensure file is open

```pascal
program SafeFilePos;

var
  F: file of Integer;
begin
  AssignFile(F, 'data.bin');
  Reset(F);
  WriteLn('Position: ', FilePos(F));  // 0 after Reset
  Seek(F, 5);
  WriteLn('Position: ', FilePos(F));  // 5
  CloseFile(F);
end.
```

### Solution 2 — Use FilePos before and after operations

```pascal
program TrackPosition;

var
  F: file of Integer;
  StartPos, EndPos: Int64;
begin
  AssignFile(F, 'data.bin');
  Reset(F);
  StartPos := FilePos(F);
  Seek(F, FileSize(F));
  EndPos := FilePos(F);
  WriteLn('File spans positions ', StartPos, ' to ', EndPos);
  CloseFile(F);
end.
```

### Solution 3 — FilePos with BlockRead tracking

```pascal
program BlockReadPos;

var
  F: file;
  Buf: array[0..1023] of Byte;
  Count: Integer;
begin
  AssignFile(F, 'data.bin');
  Reset(F, 1);
  WriteLn('Start: ', FilePos(F));
  repeat
    BlockRead(F, Buf, SizeOf(Buf), Count);
    WriteLn('Read to position: ', FilePos(F));
  until Count = 0;
  CloseFile(F);
end.
```

### Solution 4 — Safe wrapper function

```pascal
function SafeFilePos(var F: file): Int64;
begin
  try
    Result := FilePos(F);
  except
    Result := -1;
  end;
end;
```

## Examples

A progress indicator uses `FilePos(F) / FileSize(F) * 100` to show percentage complete. After the file is closed, the next call to `FilePos` triggers runtime error 5. Moving the calculation inside the read loop before closing fixes the issue.

## Related Errors

- [Seek Error](/languages/pascal/pascal-seek-error) — positioning errors
- [FileSize Error](/languages/pascal/pascal-filesize-error) — size query
- [IO Error](/languages/pascal/io-error) — I/O failures
