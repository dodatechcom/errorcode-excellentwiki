---
title: "File not found"
description: "A file not found error occurs when attempting to open a file that doesn't exist."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `File not found` error occurs when the program tries to open a file for reading that doesn't exist at the specified path. This is a runtime error in Pascal file I/O operations.

## Common Causes

- File doesn't exist at path
- Wrong file path or name
- Incorrect working directory
- Typo in filename

## How to Fix

```pascal
program FileNotFoundDemo;

var
  f: Text;
  filename: String;

begin
  filename := 'data.txt';

  {$I-}  // Disable I/O checking
  Assign(f, filename);
  Reset(f);
  {$I+}  // Enable I/O checking

  if IOResult <> 0 then
    WriteLn('File not found: ', filename)
  else
  begin
    // process file
    Close(f);
  end;
end.
```

```pascal
program CheckFileExists;

uses SysUtils;

var
  filename: String;

begin
  filename := 'data.txt';

  if not FileExists(filename) then
    WriteLn('File not found: ', filename)
  else
    WriteLn('File found');
end.
```

## Examples

```pascal
program FileNotFoundExample;

var
  f: Text;

begin
  Assign(f, 'nonexistent.txt');
  Reset(f);  // File not found error
end.
```

## Related Errors

- [I/O error](/languages/pascal/io-error)
- [Invalid pointer operation](/languages/pascal/invalid-pointer)
