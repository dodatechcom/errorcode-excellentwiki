---
title: "Exception error in Pascal"
description: "Exception errors in Pascal occur when an unhandled exception is raised and no try/except block catches it."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["exception", "try", "except", "handled", "pascal"]
weight: 5
---

## What This Error Means

Pascal supports exception handling with try/except/finally blocks. When an exception is raised but not caught, the program terminates with an error message.

## Common Causes

- Missing try/except block around risky code
- Exception not matching any except handler
- Re-raising exception without handling
- Resource cleanup missing (finally block)

## How to Fix

```pascal
program ExceptionDemo;

begin
  // WRONG: No exception handling
  try
    // Code that may raise exception
  except
    on E: Exception do
      WriteLn('Caught: ', E.Message);
  end;
end.
```

```pascal
// CORRECT: Comprehensive exception handling
program SafeExceptionDemo;

var
  f: Text;

begin
  try
    Assign(f, 'data.txt');
    Reset(f);
    // Process file
  except
    on E: EFileNotFoundException do
      WriteLn('File not found: ', E.Message)
    on E: Exception do
      WriteLn('Unexpected error: ', E.Message);
  finally
    // Cleanup code runs regardless
    if FileExists('data.txt') then
      Close(f);
  end;
end.
```

## Examples

```pascal
program Example;
begin
  // This will crash without try/except
  WriteLn(1 div 0);
end.
```

## Related Errors

- [Runtime Error](/languages/pascal/pascal-runtime-error) - general errors
- [File Not Found](/languages/pascal/file-not-found4) - file errors
