---
title: "[Solution] Pascal File of Record Error — How to Fix"
description: "Fix typed file of record errors in Pascal when reading or writing record structures to disk."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1044
---

# File of Record Error

Pascal supports `file of RecordType` for binary record I/O. Errors occur when the record structure changes between writes and reads, when file mode is incorrect, or when seeking past the end of the file.

## Common Causes

- Reading a file of record after the record structure changed
- Using `Read` on a file opened with `Reset` in wrong mode
- Seeking beyond `FileSize` without extending the file
- Mixing `Read`/`Write` with `BlockRead`/`BlockWrite`

## How to Fix

### Solution 1 — Open file correctly for record I/O

```pascal
program FileOfRecordFix;

type
  TPerson = record
    Name: string[50];
    Age: Integer;
  end;

var
  F: file of TPerson;
  P: TPerson;
begin
  AssignFile(F, 'people.dat');
  Rewrite(F);           // create/truncate
  P.Name := 'Alice';
  P.Age := 30;
  Write(F, P);
  CloseFile(F);
end.
```

### Solution 2 — Append records without truncating

```pascal
program AppendRecord;

type
  TScore = record
    ID: Integer;
    Value: Double;
  end;

var
  F: file of TScore;
  S: TScore;
begin
  AssignFile(F, 'scores.dat');
  Reset(F);
  Seek(F, FileSize(F));  // move to end
  S.ID := 42;
  S.Value := 95.5;
  Write(F, S);
  CloseFile(F);
end.
```

### Solution 3 — Handle versioned record structures

```pascal
program VersionedRecord;

type
  TPersonV1 = record
    Name: string[50];
    Age: Integer;
  end;

  TPersonV2 = record
    Name: string[50];
    Age: Integer;
    Email: string[100];  // new field
  end;

function ReadPersonV2(var F: file of TPersonV1): TPersonV2;
begin
  FillChar(Result, SizeOf(Result), 0);
  // read old format, populate new fields with defaults
end;
```

### Solution 4 — Use BlockRead for bulk record I/O

```pascal
program BulkRecord;

type
  TRecord = record
    X, Y: Integer;
  end;

var
  F: file of TRecord;
  Buf: array[0..99] of TRecord;
  Count: Integer;
begin
  AssignFile(F, 'data.bin');
  Reset(F);
  BlockRead(F, Buf, 100, Count);
  CloseFile(F);
  WriteLn('Read ', Count, ' records');
end.
```

## Examples

A database saves records as `file of TPerson`. A new version adds a field. Old files crash when read with the new structure. The fix is to version the record or use `BlockRead` with a version header.

## Related Errors

- [Typed File](/languages/pascal/pascal-typed-file-error) — binary file mode
- [File Not Found](/languages/pascal/pascal-file-not-found) — missing files
- [IO Error](/languages/pascal/io-error) — I/O operation failures
