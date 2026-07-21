---
title: "[Solution] Pascal LINK and UNLINK Error"
description: "Fix Pascal LINK and UNLINK errors when working with MS-DOS file handle linking."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

LINK and UNLINK errors occur when file handle linking fails or when attempting to unlink non-linked file handles.

## Common Causes

- LINK on non-existent file handle
- UNLINK on handle not created by LINK
- LINK when system file table is full
- Using LINK/UNLINK with non-DOS compilers

## How to Fix

### 1. Check handle before linking

```pascal
var
  f1, f2: File;
begin
  Assign(f1, 'data.txt');
  Reset(f1);
  Assign(f2, 'log.txt');
  Rewrite(f2);
  if IOResult = 0 then
    Link(f1, f2);
end;
```

### 2. Use modern I/O instead

```pascal
// Prefer modern file handling
AssignFile(f, 'data.txt');
Reset(f);
// process
CloseFile(f);
```

## Examples

```pascal
program LinkUnlinkDemo;

var
  f: File;

begin
  Assign(f, 'test.dat');
  Rewrite(f);
  WriteLn('File handle: ', FileRec(f).Handle);
  CloseFile(f);
end.
```

## Related Errors

- [File not found](/languages/pascal/pascal-file-not-found)
- [File locking error](/languages/pascal/pascal-file-locking-error)
- [Runtime error](/languages/pascal/pascal-runtime-error)
