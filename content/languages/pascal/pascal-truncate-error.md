---
title: "[Solution] Pascal TRUNCATE Error"
description: "Fix Pascal TRUNCATE procedure errors when truncating files to the current position."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

TRUNCATE errors occur when attempting to truncate a file that is not opened for writing or when the file handle is invalid.

## Common Causes

- TRUNCATE on read-only file
- File not positioned before truncate
- TRUNCATE on closed file
- File system does not support truncate

## How to Fix

### 1. Ensure file is writable

```pascal
var
  f: File;
begin
  Assign(f, 'data.txt');
  Reset(f);  // open for reading
  // WRONG: Truncate on read-only
  // Truncate(f);

  // CORRECT: Open for writing
  Rewrite(f);
  Truncate(f);
end;
```

### 2. Position before truncate

```pascal
Seek(f, 0);  // position to beginning
Truncate(f); // truncate to current position
```

## Examples

```pascal
program TruncateDemo;

var
  f: TextFile;

begin
  AssignFile(f, 'temp.txt');
  Rewrite(f);
  WriteLn(f, 'Line 1');
  WriteLn(f, 'Line 2');
  Truncate(f);
  CloseFile(f);
end.
```

## Related Errors

- [File not found](/languages/pascal/pascal-file-not-found)
- [File mode error](/languages/pascal/pascal-file-mode-error)
- [Runtime error](/languages/pascal/pascal-runtime-error)
