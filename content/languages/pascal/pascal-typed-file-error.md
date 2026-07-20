---
title: "[Solution] Pascal Typed File Error — How to Fix"
description: "Fix typed file errors in Pascal when performing binary I/O on files with incorrect mode or record handling."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1046
---

# Typed File Error

A typed file (`file of Type`) performs binary I/O. Errors occur when using text-mode procedures on typed files, reading past the end, or using procedures that only work on text files.

## Common Causes

- Using `ReadLn`/`WriteLn` on a typed file (only for text files)
- `Seek` beyond `FileSize` without extending the file first
- `Write` on a file opened with `Reset` (read-only mode)
- Wrong record size causing misaligned reads

## How to Fix

### Solution 1 — Open typed file in correct mode

```pascal
program TypedFileFix;

type
  TData = record
    X, Y: Integer;
    Value: Double;
  end;

var
  F: file of TData;
  D: TData;
begin
  AssignFile(F, 'data.bin');
  Rewrite(F);       // write mode
  D.X := 1;
  D.Y := 2;
  D.Value := 3.14;
  Write(F, D);
  CloseFile(F);

  Reset(F);         // read mode
  Read(F, D);
  WriteLn(D.X, ' ', D.Y, ' ', D.Value:0:2);
  CloseFile(F);
end.
```

### Solution 2 — Use Seek correctly

```pascal
program SeekDemo;

type
  TRecord = record
    ID: Integer;
    Name: string[30];
  end;

var
  F: file of TRecord;
  R: TRecord;
begin
  AssignFile(F, 'records.bin');
  Reset(F);
  if FileSize(F) > 5 then
  begin
    Seek(F, 5);      // jump to 6th record (0-indexed)
    Read(F, R);
  end;
  CloseFile(F);
end.
```

### Solution 3 — Open for read/write

```pascal
program ReadWrite;

type
  TEntry = record
    Key: Integer;
    Value: string[100];
  end;

var
  F: file of TEntry;
  E: TEntry;
begin
  AssignFile(F, 'entries.bin');
  Reset(F);          // open existing
  Seek(F, 0);
  Read(F, E);
  E.Value := 'Updated';
  Seek(F, 0);        // go back to beginning
  Write(F, E);       // overwrite first record
  CloseFile(F);
end.
```

### Solution 4 — Check file mode before writing

```pascal
function IsWritable(const F: file): Boolean;
begin
  // FPC: check file mode
  Result := FileMode = 2;  // 0=read, 1=write, 2=read/write
end;
```

## Examples

A program opens a typed file with `Reset` (read-only) and then tries to `Write` to it. Runtime error 5 (file access denied) occurs. Opening with `Reset` and setting `FileMode := 2` (read/write) fixes the issue.

## Related Errors

- [File of Record](/languages/pascal/pascal-file-of-record-error) — record I/O
- [Text File Error](/languages/pascal/pascal-text-file-error) — text-mode I/O
- [Seek Error](/languages/pascal/pascal-seek-error) — position errors
