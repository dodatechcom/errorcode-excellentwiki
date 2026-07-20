---
title: "[Solution] Pascal Append Error — How to Fix"
description: "Fix Append errors in Pascal when opening text files for appending to existing content."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1049
---

# Append Error

`Append` opens an existing text file for writing at the end. Errors occur when the file does not exist, the file is write-only, or `Append` is used on a non-text file.

## Common Causes

- `Append` on a file that does not exist (unlike `Rewrite`, it does not create)
- Using `Append` on a typed file (only valid for `Text` variables)
- File locked by another process
- File opened in read-only mode before `Append` call

## How to Fix

### Solution 1 — Create file if it doesn't exist

```pascal
program SafeAppend;

var
  F: Text;
begin
  AssignFile(F, 'log.txt');
  if FileExists('log.txt') then
    Append(F)
  else
    Rewrite(F);          // create new file if missing
  WriteLn(F, 'New entry');
  CloseFile(F);
end.
```

### Solution 2 — Use Append with ForceDirectories

```pascal
program AppendWithDir;

uses SysUtils;

var
  F: Text;
  Dir: string;
begin
  Dir := 'logs/' + FormatDateTime('yyyymm', Now);
  ForceDirectories(Dir);
  AssignFile(F, Dir + '/app.log');
  if FileExists(Dir + '/app.log') then
    Append(F)
  else
    Rewrite(F);
  WriteLn(F, DateTimeToStr(Now), ': Application started');
  CloseFile(F);
end.
```

### Solution 3 — Append with try/except

```pascal
program SafeAppendTry;

var
  F: Text;
begin
  try
    AssignFile(F, 'data.txt');
    Append(F);
    WriteLn(F, 'New data');
    CloseFile(F);
  except
    on E: Exception do
      WriteLn('Append failed: ', E.Message);
  end;
end.
```

### Solution 4 — Handle read-only files

```pascal
program ReadOnlyAppend;

uses SysUtils;

var
  F: Text;
begin
  if FileExists('readonly.txt') then
  begin
    // Must have write permission
    AssignFile(F, 'readonly.txt');
    try
      Append(F);
      WriteLn(F, 'This may fail if file is read-only');
      CloseFile(F);
    except
      on E: Exception do
        WriteLn('Cannot append: file may be read-only');
    end;
  end;
end.
```

## Examples

A daemon appends to a log file. If the log was deleted by another process while the daemon is running, the next `Append` call fails. The fix is to check `FileExists` and fall back to `Rewrite`.

## Related Errors

- [Reset/Rewrite Error](/languages/pascal/pascal-reset-rewrite-error) — file open modes
- [File Not Found](/languages/pascal/pascal-file-not-found) — missing files
- [IO Error](/languages/pascal/io-error) — I/O failures
