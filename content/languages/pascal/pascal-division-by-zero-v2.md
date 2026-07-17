---
title: "[Solution] Pascal: division by zero error"
description: "Fix Pascal runtime errors when dividing by zero in integer or real arithmetic."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Pascal division by zero occurs when dividing an integer or real value by zero, which is mathematically undefined.

## Common Causes

- Divisor variable is zero
- Uninitialized divisor
- Missing zero-check
- Array element is zero
- Function returns zero

## How to Fix

```pascal
program DivByZero;
var
  a, b, result: Integer;
begin
  a := 10;
  b := 0;
  result := a div b;  // Runtime error
end.
```

```pascal
program SafeDivide;
var
  a, b, result: Integer;
begin
  a := 10;
  b := 0;
  
  if b <> 0 then
  begin
    result := a div b;
    WriteLn('Result: ', result);
  end
  else
    WriteLn('Cannot divide by zero');
end.
```

```pascal
program TryExceptDiv;
var
  a, b, result: Integer;
begin
  a := 10;
  b := 0;
  
  try
    result := a div b;
    WriteLn('Result: ', result);
  except
    on E: Exception do
      WriteLn('Error: ', E.Message);
  end;
end.
```

```pascal
program RealDivision;
var
  x, y, result: Real;
begin
  x := 10.0;
  y := 0.0;
  
  if Abs(y) > 1E-10 then
  begin
    result := x / y;
    WriteLn('Result: ', result);
  end
  else
    WriteLn('Divisor too small');
end.
```

```pascal
program SafeFunction;
function SafeDiv(a, b: Integer): Integer;
begin
  if b <> 0 then
    SafeDiv := a div b
  else
    SafeDiv := 0;  // Or raise exception
end;

begin
  WriteLn(SafeDiv(10, 0));
end.
```

## Related Errors

- [Overflow](pascal-overflow-error-v2) - arithmetic overflow
- [Index Out of Range](pascal-index-out-of-range-v2) - array bounds
- [Runtime Error](pascal-runtime-error-v2) - general runtime
