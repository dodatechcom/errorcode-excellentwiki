---
title: "[Solution] Pascal: file not found error"
description: "Fix Pascal errors when attempting to open files that don't exist at the specified path."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Pascal file not found errors occur when the program tries to open a file that doesn't exist. This is similar to runtime error 2 in Free Pascal.

## Common Causes

- File path incorrect
- File doesn't exist
- Wrong working directory
- File moved or deleted
- Case sensitivity

## How to Fix

```pascal
program FileNotFound;
var
  f: TextFile;
begin
  AssignFile(f, 'nonexistent.txt');
  Reset(f);  // Error: file not found
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
program FullPathDemo;
var
  f: TextFile;
  path: string;
begin
  path := 'C:\Users\Data\file.txt';
  
  if FileExists(path) then
  begin
    AssignFile(f, path);
    Reset(f);
    CloseFile(f);
  end
  else
    WriteLn('Not found: ', path);
end.
```

```pascal
program RelativePathDemo;
var
  f: TextFile;
begin
  // Use relative path from current directory
  if FileExists('..\data\file.txt') then
  begin
    AssignFile(f, '..\data\file.txt');
    Reset(f);
    CloseFile(f);
  end;
end.
```

```pascal
program CreateIfMissing;
var
  f: TextFile;
begin
  if not FileExists('data.txt') then
  begin
    AssignFile(f, 'data.txt');
    Rewrite(f);
    WriteLn(f, 'Default data');
    CloseFile(f);
  end;
  
  AssignFile(f, 'data.txt');
  Reset(f);
  // Process file
  CloseFile(f);
end.
```

## Related Errors

- [Runtime Error](pascal-runtime-error-v2) - file errors
- [Invalid Pointer](pascal-invalid-pointer-v2) - pointer errors
- [Exception Error](pascal-exception-error-v2) - exception handling
