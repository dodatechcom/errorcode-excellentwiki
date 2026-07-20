---
title: "[Solution] Pascal Try Finally Error — How to Fix"
description: "Fix try finally errors in Pascal when resource cleanup blocks are incorrectly used or missing."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1077
---

# Try Finally Error

The `try...finally` block guarantees cleanup code runs even when exceptions occur. Errors occur when finally blocks contain exception-raising code, when finally is used instead of except for error handling, or when resources are not properly released.

## Common Causes

- Finally block raising an exception (masks the original exception)
- Using finally for error handling instead of except
- Not putting resource cleanup in finally
- Mixing try/finally with try/except incorrectly

## How to Fix

### Solution 1 — Use finally for guaranteed cleanup

```pascal
program FinallyFix;

var
  F: Text;
begin
  AssignFile(F, 'output.txt');
  Rewrite(F);
  try
    WriteLn(F, 'Hello');
    WriteLn(1 div 0);   // exception!
  finally
    CloseFile(F);         // always runs
  end;
end.
```

### Solution 2 — Nest try/except inside try/finally

```pascal
program NestedTry;

uses SysUtils;

var
  F: Text;
begin
  AssignFile(F, 'data.txt');
  Rewrite(F);
  try
    try
      WriteLn(F, 'data');
      // risky operation
    except
      on E: Exception do
        WriteLn('Error: ', E.Message);
    end;
  finally
    CloseFile(F);
  end;
end.
```

### Solution 3 — Free objects in finally

```pascal
program FreeInFinally;

uses SysUtils;

var
  List: TStringList;
begin
  List := TStringList.Create;
  try
    List.Add('Hello');
    List.Add('World');
    WriteLn(List.Count);
  finally
    List.Free;
  end;
end.
```

### Solution 4 — Multiple resources in finally

```pascal
program MultiResource;

var
  F1, F2: Text;
begin
  AssignFile(F1, 'in.txt');
  AssignFile(F2, 'out.txt');
  Reset(F1);
  Rewrite(F2);
  try
    while not Eof(F1) do
    begin
      var Line: string;
      ReadLn(F1, Line);
      WriteLn(F2, Line);
    end;
  finally
    CloseFile(F1);
    CloseFile(F2);
  end;
end.
```

## Examples

A database connection is opened and used. If an exception occurs during use, the connection is never closed. Wrapping the entire block in `try...finally` with `Connection.Close` in the finally section ensures cleanup.

## Related Errors

- [Try Except Error](/languages/pascal/pascal-try-except-error) — exception catching
- [Raise Error](/languages/pascal/pascal-raise-error) — raising exceptions
- [Memory Leak](/languages/pascal/pascal-memory-leak-error) — resource leaks
