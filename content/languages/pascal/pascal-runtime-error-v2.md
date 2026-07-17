---
title: "[Solution] Pascal: runtime error - file not found"
description: "Fix Pascal runtime errors when files cannot be found or opened during program execution."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["runtime", "file", "not-found", "open", "exception", "pascal"]
weight: 5
---

## What This Error Means

Pascal runtime error "file not found" occurs when the program attempts to open a file that doesn't exist at the specified path.

## Common Causes

- File doesn't exist at specified path
- Incorrect file path or name
- File moved or deleted
- Working directory incorrect
- Case sensitivity issues

## How to Fix

```pascal
program RuntimeErrorDemo;
var
  f: TextFile;
begin
  AssignFile(f, 'data.txt');
  Reset(f);  // Runtime error if file doesn't exist
  CloseFile(f);
end.
```

```pascal
program SafeFileOpen;
var
  f: TextFile;
begin
  if FileExists('data.txt') then
  begin
    AssignFile(f, 'data.txt');
    Reset(f);
    // Process file
    CloseFile(f);
  end
  else
    WriteLn('File not found');
end.
```

```pascal
program TryExceptDemo;
var
  f: TextFile;
  line: string;
begin
  try
    AssignFile(f, 'data.txt');
    Reset(f);
    while not Eof(f) do
    begin
      ReadLn(f, line);
      WriteLn(line);
    end;
    CloseFile(f);
  except
    on E: Exception do
      WriteLn('Error: ', E.Message);
  end;
end.
```

```pascal
program FileDialog;
var
  f: TextFile;
  filename: string;
begin
  Write('Enter filename: ');
  ReadLn(filename);
  
  if FileExists(filename) then
  begin
    AssignFile(f, filename);
    Reset(f);
    // Process file
    CloseFile(f);
  end
  else
    WriteLn('File not found: ', filename);
end.
```

## Related Errors

- [Index Out of Range](pascal-index-out-of-range-v2) - array bounds
- [Invalid Pointer](pascal-invalid-pointer-v2) - pointer errors
- [Stack Overflow](pascal-stack-overflow-v2) - stack errors
