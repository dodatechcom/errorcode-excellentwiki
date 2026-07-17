---
title: "I/O error"
description: "An I/O error occurs when a file input/output operation fails."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `I/O error` occurs when a file input/output operation fails. This can happen due to disk full, permission denied, hardware failure, or other system-level issues.

## Common Causes

- Disk full
- Permission denied
- Hardware failure
- Network drive disconnected

## How to Fix

```pascal
program IODemo;

var
  f: File;
  filename: String;

begin
  filename := 'data.dat';

  {$I-}
  Assign(f, filename);
  Rewrite(f);
  {$I+}

  if IOResult <> 0 then
    WriteLn('I/O error: ', IOResult)
  else
  begin
    // write data
    Close(f);
  end;
end.
```

```pascal
program SafeIO;

uses SysUtils;

procedure WriteToFile(const filename, content: String);
var
  f: Text;
begin
  try
    AssignFile(f, filename);
    Rewrite(f);
    WriteLn(f, content);
    CloseFile(f);
  except
    on E: EInOutError do
      WriteLn('I/O error: ', E.Message);
  end;
end;

begin
  WriteToFile('output.txt', 'Hello');
end.
```

## Examples

```pascal
program IOExample;

var
  f: Text;

begin
  // Example 1: Write to read-only file
  Assign(f, '/etc/passwd');
  Rewrite(f);  // I/O error (permission denied)

  // Example 2: Read non-existent file
  Assign(f, 'missing.txt');
  Reset(f);  // I/O error (file not found)
end.
```

## Related Errors

- [File not found](/languages/pascal/file-not-found4)
- [Invalid pointer operation](/languages/pascal/invalid-pointer)
