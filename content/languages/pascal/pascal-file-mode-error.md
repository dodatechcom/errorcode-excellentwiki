---
title: "[Solution] Pascal FILE Mode Error"
description: "Fix Pascal file mode errors when opening files in incorrect modes or switching modes without resetting."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

File mode errors occur when attempting to read from a write-only file or write to a read-only file, or when RESET/REWRITE are misused.

## Common Causes

- Reading from file opened with REWRITE
- Writing to file opened with RESET
- Not calling RESET after REWRITE for appending
- Using APPEND without proper mode switching

## How to Fix

### 1. Open files in correct mode

```pascal
// WRONG: Reading from write-only file
AssignFile(f, 'data.txt');
Rewrite(f);  // opens for writing only
Read(f, ch);  // error!

// CORRECT
AssignFile(f, 'data.txt');
Reset(f);  // opens for reading
Read(f, ch);
```

### 2. Use APPEND for adding to existing files

```pascal
AssignFile(f, 'log.txt');
Append(f);  // opens for writing at end
WriteLn(f, 'New log entry');
CloseFile(f);
```

## Examples

```pascal
program FileModeDemo;

var
  f: TextFile;
  Line: string;

begin
  AssignFile(f, 'output.txt');
  Rewrite(f);
  WriteLn(f, 'Hello, World!');
  CloseFile(f);

  AssignFile(f, 'output.txt');
  Reset(f);
  while not Eof(f) do
  begin
    ReadLn(f, Line);
    WriteLn(Line);
  end;
  CloseFile(f);
end.
```

## Related Errors

- [File not found](/languages/pascal/pascal-file-not-found)
- [File locking error](/languages/pascal/pascal-file-locking-error)
- [Reset rewrite error](/languages/pascal/pascal-reset-rewrite-error)
