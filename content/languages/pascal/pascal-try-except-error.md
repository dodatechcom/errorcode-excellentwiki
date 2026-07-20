---
title: "[Solution] Pascal Try Except Error — How to Fix"
description: "Fix try except errors in Pascal when exception handling blocks are incorrectly structured."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1076
---

# Try Except Error

The `try...except` block catches exceptions. Errors occur when the except handler re-raises without cleanup, when exceptions are silently swallowed, or when the except block itself raises an exception.

## Common Causes

- Empty except block silently swallowing all exceptions
- Not re-raising exceptions that cannot be handled locally
- Using except where finally is needed (resource cleanup)
- Catching too broadly with `on E: Exception` hiding specific errors

## How to Fix

### Solution 1 — Always log or re-raise in except

```pascal
program ExceptFix;

uses SysUtils;

var
  F: Text;
begin
  try
    AssignFile(F, 'data.txt');
    Reset(F);
  except
    on E: Exception do
    begin
      WriteLn('Error: ', E.ClassName, ': ', E.Message);
      raise;  // re-raise if cannot handle
    end;
  end;
end.
```

### Solution 2 — Catch specific exceptions

```pascal
program SpecificCatch;

uses SysUtils;

var
  N: Integer;
  S: string;
begin
  S := 'not a number';
  try
    N := StrToInt(S);
  except
    on E: EConvertError do
      WriteLn('Conversion error: ', E.Message);
    on E: Exception do
      WriteLn('Other error: ', E.Message);
  end;
end.
```

### Solution 3 — Use except for recovery

```pascal
program Recovery;

uses SysUtils;

var
  RetryCount: Integer;
begin
  RetryCount := 0;
  repeat
    try
      // attempt operation
      Break;
    except
      on E: Exception do
      begin
        Inc(RetryCount);
        WriteLn('Retry ', RetryCount, ': ', E.Message);
        if RetryCount >= 3 then
          raise;
      end;
    end;
  until False;
end.
```

### Solution 4 — Do not nest try/except carelessly

```pascal
program NestedExcept;

uses SysUtils;

var
  F: Text;
begin
  try
    try
      AssignFile(F, 'data.txt');
      Reset(F);
      WriteLn(1 div 0);
    except
      on E: EDivByZero do
        WriteLn('Division by zero');
    end;
  except
    on E: Exception do
      WriteLn('File error: ', E.Message);
  end;
  CloseFile(F);
end.
```

## Examples

A database transaction catches all exceptions with an empty `except` block. Database corruption goes unnoticed. The fix is to log the exception, roll back the transaction, and optionally re-raise.

## Related Errors

- [Try Finally Error](/languages/pascal/pascal-try-finally-error) — cleanup blocks
- [Raise Error](/languages/pascal/pascal-raise-error) — exception raising
- [Exception Error](/languages/pascal/pascal-exception-error) — exception handling
