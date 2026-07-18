---
title: "[Solution] Pascal: runtime error number"
description: "Identify Pascal runtime errors by interpreting error numbers and enabling error trapping routines."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Pascal runtime errors are identified by numeric codes that indicate the specific failure that occurred. Common codes include 1 (division by zero), 2 (file not found), 6 (invalid file mode), 201 (range check), 202 (stack overflow), 203 (out of heap), and 204 (invalid pointer). When a runtime error occurs, the program prints the error number and terminates. In Object Pascal, these can be caught using try-except blocks. The `ExitCode` variable contains the runtime error number after termination.

## Why It Happens

Runtime errors occur when the program encounters a condition that prevents continued execution. Each error number corresponds to a specific failure type. Errors can result from invalid arithmetic operations (division by zero, overflow), memory problems (stack overflow, heap exhaustion, invalid pointers), file I/O issues (file not found, invalid mode, read past end), array access violations (range check), and type errors. Many runtime errors are preventable through input validation, boundary checking, and proper resource management. Some errors only manifest under specific conditions, such as processing particular input data or running on systems with limited resources.

## How to Fix It

**Map error numbers to their causes:**

```pascal
program RuntimeErrorGuide;
var
  errorCode: Integer;
begin
  { Common Pascal runtime error codes: }
  { 1: Division by zero }
  { 2: File not found }
  { 3: File access denied }
  { 4: Invalid file mode }
  { 5: File already open }
  { 6: Invalid file mode }
  { 8: Out of memory }
  { 9: Invalid pointer }
  { 10: Division overflow }
  { 15: Invalid string operation }
  { 101: Disk write error }
  { 102: File not assigned }
  { 103: File not open }
  { 104: File write error }
  { 105: File not open for input }
  { 106: Invalid numeric format }
  { 201: Range check error }
  { 202: Stack overflow }
  { 203: Out of heap space }
  { 204: Invalid pointer operation }

  errorCode := 1;
  WriteLn('Error code ', errorCode, ': Division by zero');
end.
```

**Enable runtime error handling:**

```pascal
program ErrorTrapping;
{$mode objfpc}
uses SysUtils;

var
  result: Integer;
begin
  try
    result := 100 div 0;
  except
    on E: EDivByZero do
      WriteLn('Caught division by zero: ', E.Message)
    on E: ERangeError do
      WriteLn('Caught range error: ', E.Message)
    on E: EIntOverflow do
      WriteLn('Caught overflow: ', E.Message)
    on E: Exception do
      WriteLn('Caught exception: ', E.ClassName, ': ', E.Message)
  end;
end.
```
**Create a runtime error handler:**

```pascal
program ErrorHandler;
{$mode objfpc}
uses SysUtils;

procedure HandleError(code: Integer);
begin
  case code of
    1: WriteLn('Runtime Error: Division by zero');
    2: WriteLn('Runtime Error: File not found');
    201: WriteLn('Runtime Error: Range check');
    202: WriteLn('Runtime Error: Stack overflow');
    203: WriteLn('Runtime Error: Out of heap');
    204: WriteLn('Runtime Error: Invalid pointer');
  else
    WriteLn('Runtime Error: Unknown error code ', code);
  end;
end;

begin
  try
    { Main program logic }
  except
    on E: Exception do
      HandleError(ExitCode);
  end;
end.


## Common Mistakes

- Not knowing what common runtime error numbers mean
- Compiling without runtime checks enabled during development
- Using `Halt` without setting `ExitCode` for proper error reporting
- Not using try-except blocks in Object Pascal to catch and handle errors
- Assuming runtime errors only happen with invalid input and not with edge cases

## Related Pages

- [Range check error in Pascal](/languages/pascal/pascal-index-error-new)
- [Stack overflow in Pascal](/languages/pascal/pascal-stack-overflow-v2)
