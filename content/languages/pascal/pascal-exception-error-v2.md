---
title: "[Solution] Pascal: exception handling error"
description: "Fix Pascal errors related to exception handling, including unhandled exceptions and try-except block issues."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Pascal exception errors occur when exceptions are raised but not properly caught, or when exception handling blocks are incorrectly structured.

## Common Causes

- Unhandled exceptions
- Exception raised in try block without matching except
- Exception not properly re-raised
- Nested exception handling issues
- Finally block missing

## How to Fix

```pascal
program UnhandledException;
var
  a, b, result: Integer;
begin
  a := 10;
  b := 0;
  result := a div b;  // Exception not caught
end.
```

```pascal
program HandleException;
var
  a, b, result: Integer;
begin
  a := 10;
  b := 0;
  
  try
    result := a div b;
  except
    on E: Exception do
      WriteLn('Error: ', E.Message);
  end;
end.
```

```pascal
program ExceptionHierarchy;
var
  f: TextFile;
begin
  try
    AssignFile(f, 'data.txt');
    Reset(f);
  except
    on E: EInOutError do
      WriteLn('I/O Error: ', E.Message)
    on E: Exception do
      WriteLn('General Error: ', E.Message);
  end;
end.
```

```pascal
program TryFinallyDemo;
var
  f: TextFile;
begin
  AssignFile(f, 'data.txt');
  
  try
    Reset(f);
    // Process file
  finally
    CloseFile(f);  // Always executed
  end;
end.
```

```pascal
program ReRaiseException;
begin
  try
    try
      // Code that may fail
    except
      on E: Exception do
      begin
        WriteLn('Caught: ', E.Message);
        raise;  // Re-raise the exception
      end;
    end;
  except
    on E: Exception do
      WriteLn('Outer handler: ', E.Message);
  end;
end.
```

```pascal
program CustomException;
type
  EInvalidInput = class(Exception);

procedure Validate(value: Integer);
begin
  if value < 0 then
    raise EInvalidInput.Create('Value must be non-negative');
end;

begin
  try
    Validate(-1);
  except
    on E: EInvalidInput do
      WriteLn('Custom error: ', E.Message);
  end;
end.
```

## Related Errors

- [Runtime Error](pascal-runtime-error-v2) - general runtime
- [Invalid Pointer](pascal-invalid-pointer-v2) - pointer errors
- [Stack Overflow](pascal-stack-overflow-v2) - stack errors
