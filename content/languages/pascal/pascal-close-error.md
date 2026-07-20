---
title: "[Solution] Pascal Close Error — How to Fix"
description: "Fix Close and CloseFile errors in Pascal when file handles are not properly released."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1050
---

# Close/CloseFile Error

`CloseFile` (or `Close` in Turbo Pascal) releases a file handle. Errors occur when closing an already-closed file, not closing files causing handle leaks, or close failing due to disk errors during final flush.

## Common Causes

- Calling `CloseFile` on an already-closed or never-opened file
- Forgetting to close files before program exit (handle leak)
- Disk full during close causing write failure
- Closing a file that was never assigned with `AssignFile`

## How to Fix

### Solution 1 — Use try/finally for guaranteed close

```pascal
program SafeClose;

var
  F: Text;
begin
  AssignFile(F, 'output.txt');
  Rewrite(F);
  try
    WriteLn(F, 'Hello');
    WriteLn(F, 'World');
  finally
    CloseFile(F);
  end;
end.
```

### Solution 2 — Check if file is open before closing

```pascal
var
  F: Text;
  IsOpen: Boolean;
begin
  IsOpen := False;
  try
    AssignFile(F, 'data.txt');
    Rewrite(F);
    IsOpen := True;
    WriteLn(F, 'data');
  finally
    if IsOpen then
      CloseFile(F);
  end;
end.
```

### Solution 3 — Close files on exception

```pascal
program ExceptionSafe;

uses SysUtils;

var
  F: file of Integer;
  N: Integer;
begin
  AssignFile(F, 'numbers.bin');
  Rewrite(F);
  try
    for N := 1 to 1000 do
      Write(F, N * N);
  finally
    CloseFile(F);
  end;
end.
```

### Solution 4 — Use RAII pattern with records

```pascal
program RAIIFile;

type
  TAutoFile = class
    F: Text;
    constructor Create(const FileName: string);
    destructor Destroy; override;
  end;

constructor TAutoFile.Create(const FileName: string);
begin
  AssignFile(F, FileName);
  Rewrite(F);
end;

destructor TAutoFile.Destroy;
begin
  CloseFile(F);
  inherited;
end;

var
  AF: TAutoFile;
begin
  AF := TAutoFile.Create('output.txt');
  try
    WriteLn(AF.F, 'auto-closed');
  finally
    AF.Free;
  end;
end.
```

## Examples

A program opens multiple files in a loop but only closes the last one. File handles accumulate until the OS limit is hit. Using `try/finally` around each file open/close pair ensures proper cleanup.

## Related Errors

- [Assign Error](/languages/pascal/pascal-assign-error) — file binding
- [IO Error](/languages/pascal/io-error) — I/O failures
- [File Not Found](/languages/pascal/pascal-file-not-found) — missing files
