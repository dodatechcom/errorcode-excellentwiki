---
title: "[Solution] Pascal DIRECTORY Error"
description: "Fix Pascal directory operation errors when creating, deleting, or changing directories."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

Directory errors occur when MKDIR, RMDIR, or CHDIR operations fail due to permissions, non-existent paths, or non-empty directories.

## Common Causes

- Directory already exists (MKDIR)
- Directory not empty (RMDIR)
- Path does not exist (CHDIR)
- Permission denied on directory

## How to Fix

### 1. Check existence before operations

```pascal
if not DirectoryExists('newdir') then
  MkDir('newdir');
```

### 2. Use IOResult to check

```pascal
MkDir('testdir');
if IOResult <> 0 then
  WriteLn('Cannot create directory');
```

## Examples

```pascal
program DirectoryDemo;

begin
  if not DirectoryExists('temp') then
  begin
    MkDir('temp');
    WriteLn('Created temp directory');
  end;
  ChDir('temp');
  WriteLn('Changed to temp');
  ChDir('..');
  RmDir('temp');
  WriteLn('Removed temp directory');
end.
```

## Related Errors

- [File not found](/languages/pascal/pascal-file-not-found)
- [Permission denied](/languages/pascal/pascal-file-locking-error)
- [Runtime error](/languages/pascal/pascal-runtime-error)
