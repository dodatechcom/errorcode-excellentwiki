---
title: "[Solution] Pascal GETDIR Procedure Error"
description: "Fix Pascal GETDIR procedure errors when querying the current working directory."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

GETDIR errors occur when the drive letter is invalid or when the current directory has been deleted.

## Common Causes

- Invalid drive letter passed to GETDIR
- Current directory deleted externally
- Buffer too small for directory path
- GETDIR on network drive with disconnected path

## How to Fix

### 1. Use valid drive letter

```pascal
var
  Dir: string;
begin
  GetDir(0, Dir);  // 0 = current drive
  WriteLn('Current dir: ', Dir);
end;
```

### 2. Use adequate buffer

```pascal
var
  Dir: string[255];  // max path length
begin
  GetDir(0, Dir);
end;
```

## Examples

```pascal
program GetDirDemo;

var
  CurrentDir: string;

begin
  GetDir(0, CurrentDir);
  WriteLn('Current directory: ', CurrentDir);
end.
```

## Related Errors

- [File not found](/languages/pascal/pascal-file-not-found)
- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Directory error](/languages/pascal/pascal-directory-error)
