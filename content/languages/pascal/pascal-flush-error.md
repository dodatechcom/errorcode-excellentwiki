---
title: "[Solution] Pascal FLUSH Function Error"
description: "Fix Pascal FLUSH function errors when flushing file buffers to disk."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

FLUSH function errors occur when flushing buffers on files not opened for writing or when the file system does not support flushing.

## Common Causes

- FLUSH on read-only file
- FLUSH on binary file opened incorrectly
- Buffer not dirty (nothing to flush)
- FLUSH on closed file

## How to Fix

### 1. Check file is writable

```pascal
var
  f: TextFile;
begin
  AssignFile(f, 'output.txt');
  Rewrite(f);
  WriteLn(f, 'Data');
  if not Flush(f) then
    WriteLn('Flush failed');
  CloseFile(f);
end;
```

### 2. Use Flush after critical writes

```pascal
WriteLn(f, 'Important data');
Flush(f);  // ensure written to disk
```

## Examples

```pascal
program FlushDemo;

var
  f: TextFile;

begin
  AssignFile(f, 'flush.txt');
  Rewrite(f);
  WriteLn(f, 'Before flush');
  Flush(f);
  WriteLn(f, 'After flush');
  Flush(f);
  CloseFile(f);
end.
```

## Related Errors

- [File not found](/languages/pascal/pascal-file-not-found)
- [File mode error](/languages/pascal/pascal-file-mode-error)
- [Runtime error](/languages/pascal/pascal-runtime-error)
