---
title: "[Solution] Pascal On Exception Error — How to Fix"
description: "Fix on exception do handler errors in Pascal when catch blocks are incorrectly structured or too broad."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1079
---

# On Exception Do Error

The `on E: ExceptionType do` pattern catches specific exception types. Errors occur when the handler order is wrong, when the exception variable `E` is used after the handler completes, or when too-broad catch masks important errors.

## Common Causes

- Catching `Exception` first (masks all more specific handlers)
- Using exception variable `E` outside the handler scope
- Not re-raising exceptions that cannot be handled locally
- Catching exceptions too broadly hiding programming errors

## How to Fix

### Solution 1 — Order handlers from specific to general

```pascal
program ExceptionOrder;

uses SysUtils;

procedure HandleError;
begin
  try
    // some code
  except
    on E: EDivByZero do
      WriteLn('Division by zero: ', E.Message)
    on E: EConvertError do
      WriteLn('Conversion error: ', E.Message)
    on E: Exception do
      WriteLn('Other error: ', E.Message);
  end;
end;
```

### Solution 2 — Use exception variable only in handler

```pascal
program ScopedException;

uses SysUtils;

var
  Msg: string;
begin
  try
    WriteLn(1 div 0);
  except
    on E: Exception do
    begin
      Msg := E.Message;  // capture message here
    end;
  end;
  WriteLn(Msg);  // use captured message, not E
end.
```

### Solution 3 — Catch and re-raise with context

```pascal
program ReraiseContext;

uses SysUtils;

procedure ProcessFile(const FileName: string);
begin
  try
    // file operations
  except
    on E: Exception do
      raise Exception.CreateFmt('Error processing %s: %s',
        [FileName, E.Message]);
  end;
end;
```

### Solution 4 — Handle multiple exception types

```pascal
program MultiCatch;

uses SysUtils;

procedure SafeOperation;
begin
  try
    // risky code
  except
    on E: EOutOfMemory do
      WriteLn('Out of memory')
    on E: EAccessViolation do
      WriteLn('Access violation')
    on E: EMathError do
      WriteLn('Math error')
    on E: Exception do
      WriteLn('Unhandled: ', E.ClassName, ': ', E.Message);
  end;
end;
```

## Examples

A `try...except` block catches `Exception` as the first handler. All specific handlers below it are never reached. Reordering to put specific exceptions first ensures each error type is handled appropriately.

## Related Errors

- [Try Except Error](/languages/pascal/pascal-try-except-error) — try/except structure
- [Raise Error](/languages/pascal/pascal-raise-error) — raising exceptions
- [Exception Error](/languages/pascal/pascal-exception-error) — general handling
