---
title: "[Solution] Pascal Reset/Rewrite Error — How to Fix"
description: "Fix Reset and Rewrite errors in Pascal when opening files in incorrect modes."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1048
---

# Reset/Rewrite Error

`Reset` opens an existing file for reading. `Rewrite` creates or truncates a file for writing. Errors occur when `Reset` is called on a non-existent file, or `Rewrite` is called on a read-only file.

## Common Causes

- `Reset` on a file that does not exist (runtime error 2)
- `Rewrite` on a file that is read-only or locked
- Calling `Reset` on a typed file without specifying the record size
- Using `Reset` instead of `Append` when appending is intended

## How to Fix

### Solution 1 — Check file existence before Reset

```pascal
program SafeReset;

var
  F: Text;
begin
  if FileExists('data.txt') then
  begin
    AssignFile(F, 'data.txt');
    Reset(F);
    // read file...
    CloseFile(F);
  end
  else
    WriteLn('File not found');
end.
```

### Solution 2 — Use Append instead of Reset for appending

```pascal
program AppendMode;

var
  F: Text;
begin
  AssignFile(F, 'log.txt');
  if FileExists('log.txt') then
    Append(F)            // open for appending
  else
    Rewrite(F);          // create new file
  WriteLn(F, DateTimeToStr(Now));
  CloseFile(F);
end.
```

### Solution 3 — Set FileMode for read/write access

```pascal
program ReadWriteMode;

var
  F: file of Integer;
begin
  AssignFile(F, 'numbers.bin');
  Reset(F);
  FileMode := 2;        // read/write access
  // now both Read and Write work
  CloseFile(F);
end.
```

### Solution 4 — Handle typed file reset

```pascal
program TypedReset;

type
  TRecord = record
    ID: Integer;
    Value: Double;
  end;

var
  F: file of TRecord;
begin
  AssignFile(F, 'records.bin');
  Reset(F);              // opens with record size = SizeOf(TRecord)
  // or explicitly:
  // Reset(F, SizeOf(TRecord));
end.
```

## Examples

A configuration loader calls `Reset` before checking if the config file exists. On first run, the file does not exist and the program crashes with runtime error 2. Wrapping the call in `FileExists` check prevents the crash.

## Related Errors

- [Assign Error](/languages/pascal/pascal-assign-error) — file binding
- [File Not Found](/languages/pascal/pascal-file-not-found) — missing files
- [Close Error](/languages/pascal/pascal-close-error) — file closure
