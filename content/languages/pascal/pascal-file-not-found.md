---
title: "File not found in Pascal"
description: "File not found errors in Pascal occur when attempting to open a file that doesn't exist at the specified path."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["file", "not-found", "path", "open", "pascal"]
weight: 5
---

## What This Error Means

Pascal's `Assign` and `Reset`/`Rewrite` procedures fail with a file not found error when the specified file path doesn't exist or is inaccessible.

## Common Causes

- Incorrect file path
- File doesn't exist yet (for Reset)
- Working directory is wrong
- Network drive not connected

## How to Fix

```pascal
program FileNotFoundDemo;

var
  f: Text;
  path: String;

begin
  path := 'data.txt';
  Assign(f, path);
  {$I-}   // Disable I/O checking
  Reset(f);
  {$I+}   // Re-enable I/O checking
  if IOResult <> 0 then
    WriteLn('File not found: ', path)
  else
  begin
    // Process file
    Close(f);
  end;
end.
```

```pascal
// CORRECT: Check file existence first
uses SysUtils;

var
  f: Text;
begin
  if FileExists('data.txt') then
  begin
    Assign(f, 'data.txt');
    Reset(f);
    // Process file
    Close(f);
  end
  else
    WriteLn('File does not exist');
end.
```

## Examples

```pascal
program Example;
var
  f: Text;
begin
  Assign(f, 'nonexistent.txt');
  Reset(f);   // Runtime error: file not found
end.
```

## Related Errors

- [IO Error](/languages/pascal/io-error) - I/O operation errors
- [Invalid Pointer](/languages/pascal/invalid-pointer) - memory errors
