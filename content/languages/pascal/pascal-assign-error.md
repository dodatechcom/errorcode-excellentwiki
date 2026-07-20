---
title: "[Solution] Pascal Assign Error — How to Fix"
description: "Fix Assign and AssignFile errors in Pascal when connecting file variables to disk files."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1047
---

# Assign/AssignFile Error

`AssignFile` (or `Assign` in Turbo Pascal) connects a file variable to a physical file path. Errors occur when the path is invalid, the file is already open, or the procedure is called on an already-assigned file.

## Common Causes

- File path contains invalid characters or does not exist
- Calling `AssignFile` on an already-assigned file
- Using `Assign` instead of `AssignFile` in Delphi/FPC mode
- Empty or nil file name string

## How to Fix

### Solution 1 — Verify path before assigning

```pascal
program AssignFix;

uses SysUtils;

var
  F: Text;
  Path: string;
begin
  Path := 'output.txt';
  if not FileExists(ExtractFilePath(Path)) then
    ForceDirectories(ExtractFilePath(Path));
  AssignFile(F, Path);
  Rewrite(F);
  WriteLn(F, 'Created successfully');
  CloseFile(F);
end.
```

### Solution 2 — Close before re-assigning

```pascal
program ReassignFix;

var
  F: Text;
begin
  AssignFile(F, 'file1.txt');
  Rewrite(F);
  WriteLn(F, 'File 1');
  CloseFile(F);           // must close first

  AssignFile(F, 'file2.txt');
  Rewrite(F);
  WriteLn(F, 'File 2');
  CloseFile(F);
end.
```

### Solution 3 — Use relative or absolute paths

```pascal
program PathDemo;

uses SysUtils;

var
  F: Text;
  AppDir: string;
begin
  AppDir := ExtractFilePath(ParamStr(0));
  AssignFile(F, AppDir + 'data.log');
  Append(F);
  WriteLn(F, Now);
  CloseFile(F);
end.
```

### Solution 4 — Handle special file names

```pascal
program SpecialFiles;

var
  F: Text;
begin
  AssignFile(F, 'CON');       // DOS console
  Rewrite(F);
  WriteLn(F, 'Hello console');
  CloseFile(F);
end.
```

## Examples

A service opens a log file, writes entries, but never calls `CloseFile`. After many write operations, the OS runs out of file handles. Adding `CloseFile` calls or using `try/finally` ensures proper cleanup.

## Related Errors

- [File Not Found](/languages/pascal/pascal-file-not-found) — missing files
- [Reset/Rewrite Error](/languages/pascal/pascal-reset-rewrite-error) — file mode issues
- [IO Error](/languages/pascal/io-error) — I/O failures
