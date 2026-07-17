---
title: "[Solution] Pascal: arithmetic overflow error"
description: "Fix Pascal runtime errors when arithmetic operations exceed the data type's maximum capacity."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Pascal arithmetic overflow occurs when the result of a calculation exceeds the maximum value that the variable's data type can hold.

## Common Causes

- Result exceeds Integer range
- Multiplication producing large values
- Accumulated values in loops
- Using wrong data type for calculations

## How to Fix

```pascal
program OverflowError;
var
  x: Integer;
begin
  x := 40000;  // Runtime error: exceeds Integer range
end.
```

```pascal
program SafeOverflow;
var
  x: LongInt;  // Use larger type
begin
  x := 40000;  // OK: LongInt max is ~2.1 billion
  WriteLn(x);
end.
```

```pascal
program OverflowChecking;
var
  a, b, result: Integer;
begin
  {$Q+}  // Enable overflow checking
  a := 200;
  b := 200;
  result := a * b;  // Will trigger overflow check
  {$Q-}
end.
```

```pascal
program SafeMultiply;
var
  a, b: Integer;
  result: Int64;
begin
  a := 200;
  b := 200;
  result := Int64(a) * Int64(b);  // Use larger type
  WriteLn(result);
end.
```

```pascal
program CheckOverflow;
function SafeAdd(a, b: Integer): Integer;
begin
  if (b > 0) and (a > MaxInt - b) then
    raise Exception.Create('Integer overflow')
  else if (b < 0) and (a < MinInt - b) then
    raise Exception.Create('Integer underflow')
  else
    SafeAdd := a + b;
end;

begin
  WriteLn(SafeAdd(MaxInt, 1));
end.
```

## Related Errors

- [Division by Zero](pascal-division-by-zero-v2) - arithmetic errors
- [Stack Overflow](pascal-stack-overflow-v2) - stack errors
- [Index Out of Range](pascal-index-out-of-range-v2) - bounds errors
