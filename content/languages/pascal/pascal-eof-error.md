---
title: "[Solution] Pascal EOF Error — How to Fix"
description: "Fix EOF (end-of-file) errors in Pascal when reading past the end of a file."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1056
---

# EOF Error

`EOF` returns `True` when the file pointer is at or past the end. Runtime errors occur when `Read` is called after `EOF` returns `True`, or when `EOF` is used on an unopened file.

## Common Causes

- `Read` called without checking `EOF` first
- `EOF` on a file that was never assigned or opened
- Mixed `Read` and `ReadLn` leaving the pointer at an inconsistent position
- Using `EOF` on a typed file after seeking past the end

## How to Fix

### Solution 1 — Always check EOF before reading

```pascal
program SafeEOF;

var
  F: file of Integer;
  N: Integer;
begin
  AssignFile(F, 'data.bin');
  Reset(F);
  while not EOF(F) do
  begin
    Read(F, N);
    WriteLn(N);
  end;
  CloseFile(F);
end.
```

### Solution 2 — Use try/except for robust reading

```pascal
program RobustRead;

var
  F: Text;
  Line: string;
begin
  AssignFile(F, 'text.txt');
  Reset(F);
  try
    while not EOF(F) do
    begin
      ReadLn(F, Line);
      WriteLn(Line);
    end;
  except
    on E: Exception do
      WriteLn('Read error: ', E.Message);
  end;
  CloseFile(F);
end.
```

### Solution 3 — Check EOF on typed files correctly

```pascal
program TypedEOF;

type
  TRecord = record
    ID: Integer;
    Value: Double;
  end;

var
  F: file of TRecord;
  R: TRecord;
begin
  AssignFile(F, 'records.bin');
  Reset(F);
  while not EOF(F) do
  begin
    Read(F, R);
    ProcessRecord(R);
  end;
  CloseFile(F);
end.
```

### Solution 4 — Handle binary EOF for raw files

```pascal
program BinaryEOF;

var
  F: file;
  Buf: array[0..255] of Byte;
  Count: Integer;
begin
  AssignFile(F, 'data.bin');
  Reset(F, 1);
  while not EOF(F) do
  begin
    BlockRead(F, Buf, SizeOf(Buf), Count);
    if Count > 0 then
      ProcessBuffer(Buf, Count);
  end;
  CloseFile(F);
end.
```

## Examples

A CSV parser reads lines with `ReadLn` without checking `EOF`. On the last line, the second `ReadLn` call tries to read past the file end, causing runtime error 100. Adding `not EOF(F)` to the loop condition fixes the issue.

## Related Errors

- [EOLN Error](/languages/pascal/pascal-eoln-error) — end-of-line
- [IO Error](/languages/pascal/io-error) — I/O failures
- [Text File Error](/languages/pascal/pascal-text-file-error) — text mode issues
