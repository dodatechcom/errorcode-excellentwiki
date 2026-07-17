---
title: "Overflow error"
description: "An overflow error occurs when an arithmetic result exceeds the capacity of the integer type."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `Overflow error` occurs when an arithmetic operation produces a result that is too large to be represented in the integer type. This is a runtime error when overflow checking is enabled.

## Common Causes

- Multiplying large integers
- Accumulating values without sufficient range
- Recursive calls with large numbers
- Integer type too small for calculation

## How to Fix

```pascal
program OverflowDemo;

var
  a, b, result: Integer;

begin
  {$Q+}  // Overflow checking enabled
  a := 100000;
  b := 100000;
  result := a * b;  // Overflow error

  // CORRECT: Use larger type
  var
    bigResult: Int64;
  bigResult := Int64(a) * Int64(b);
end.
```

```pascal
program OverflowFix;

var
  sum: Integer;

begin
  sum := 0;
  for var i := 1 to 100000 do
  begin
    if sum + i > MaxInt then
    begin
      WriteLn('Would overflow at i = ', i);
      Break;
    end;
    sum := sum + i;
  end;
end.
```

## Examples

```pascal
program OverflowExample;

var
  x: Integer;

begin
  {$Q+}
  x := MaxInt;
  x := x + 1;  // Overflow error

  x := MaxInt * 2;  // Overflow error
end.
```

## Related Errors

- [Range check error](/languages/pascal/range-check)
- [Division by zero](/languages/pascal/division-zero4)
