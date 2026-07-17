---
title: "Runtime error in Pascal"
description: "General runtime errors in Pascal occur during program execution due to invalid operations, unhandled exceptions, or resource limitations."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Pascal runtime errors occur when the program encounters an invalid operation during execution. Free Pascal and Delphi provide detailed error messages and error codes.

## Common Causes

- Division by zero
- Integer overflow
- Array index out of range
- File I/O failures
- Invalid memory access

## How to Fix

```pascal
program RuntimeErrorDemo;

var
  a, b, result: Integer;

begin
  // Enable runtime error checking
  {$R+}  // Range checking
  {$Q+}  // Overflow checking

  a := 10;
  b := 0;
  if b <> 0 then
    result := a div b
  else
    WriteLn('Cannot divide by zero');
end.
```

```pascal
// Use exception handling
program SafeErrorDemo;

var
  result: Integer;

begin
  try
    result := 10 div 0;
  except
    on E: Exception do
      WriteLn('Error: ', E.Message);
  end;
end.
```

## Examples

```pascal
program Example;
var
  arr: array[1..5] of Integer;
begin
  arr[10] := 42;   // Runtime error: index out of range
end.
```

## Related Errors

- [Division by Zero](/languages/pascal/division-by-zero) - arithmetic errors
- [Index Out of Range](/languages/pascal/range-check) - array bounds
- [Stack Overflow](/languages/pascal/stack-overflow5) - stack errors
