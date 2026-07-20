---
title: "[Solution] Pascal Raise Exception Error — How to Fix"
description: "Fix raise exception errors in Pascal when exceptions are raised incorrectly or without proper constructors."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1078
---

# Raise Exception Error

The `raise` statement creates and raises an exception object. Errors occur when raising a nil exception, when the exception class lacks a constructor, or when raise is used outside a try block with no handler.

## Common Causes

- `raise nil` or `raise TObject(nil)` — nil exception object
- Exception class without proper Message property
- Raising an exception in a finally block (masks original)
- Not freeing the exception object after handling

## How to Fix

### Solution 1 — Raise with a proper exception object

```pascal
program RaiseFix;

uses SysUtils;

procedure ValidateAge(Age: Integer);
begin
  if Age < 0 then
    raise Exception.Create('Age cannot be negative');
  if Age > 150 then
    raise Exception.CreateFmt('Invalid age: %d', [Age]);
end;

begin
  try
    ValidateAge(-5);
  except
    on E: Exception do
      WriteLn('Caught: ', E.Message);
  end;
end.
```

### Solution 2 — Create custom exception classes

```pascal
program CustomException;

type
  EValidationError = class(Exception)
    FieldName: string;
    constructor Create(const AField, AMsg: string);
  end;

constructor EValidationError.Create(const AField, AMsg: string);
begin
  inherited Create(AMsg);
  FieldName := AField;
end;

procedure CheckName(const Name: string);
begin
  if Name = '' then
    raise EValidationError.Create('Name', 'Name is required');
end;
```

### Solution 3 — Re-raise with exception chain

```pascal
program Reraise;

uses SysUtils;

procedure DoWork;
begin
  try
    WriteLn(1 div 0);
  except
    on E: Exception do
      raise Exception.Create('Work failed: ' + E.Message);
  end;
end;
```

### Solution 4 — Never raise in finally

```pascal
program NoRaiseInFinally;

uses SysUtils;

var
  F: Text;
begin
  AssignFile(F, 'data.txt');
  Rewrite(F);
  try
    WriteLn(F, 'data');
  finally
    try
      CloseFile(F);
    except
      // silently handle close errors
    end;
  end;
end.
```

## Examples

A validation routine raises `Exception.Create('')` with an empty message. The catch block cannot identify what went wrong. Using a custom exception class with a `FieldName` property provides context for error reporting.

## Related Errors

- [Try Except Error](/languages/pascal/pascal-try-except-error) — catching exceptions
- [Try Finally Error](/languages/pascal/pascal-try-finally-error) — cleanup
- [Exception Error](/languages/pascal/pascal-exception-error) — general exception handling
