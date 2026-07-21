---
title: "[Solution] Pascal TRUNC and ROUND Error"
description: "Fix Pascal TRUNC and ROUND errors when converting real numbers to integers with precision loss."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

TRUNC and ROUND errors occur when converting real numbers to integers that exceed integer range or when rounding mode is incorrect.

## Common Causes

- TRUNC result exceeds integer range
- ROUND with banker's rounding giving unexpected results
- TRUNC of NaN or Infinity
- Precision loss in real to integer conversion

## How to Fix

### 1. Check range before conversion

```pascal
var
  R: Real;
  I: Integer;
begin
  R := 123456789.0;
  if (R >= -MaxInt) and (R <= MaxInt) then
    I := Trunc(R)
  else
    WriteLn('Overflow');
end;
```

### 2. Use appropriate rounding

```pascal
I := Round(R);  // rounds to nearest
I := Trunc(R);  // truncates toward zero
I := Floor(R);  // rounds toward negative infinity (if available)
```

## Examples

```pascal
program TruncRoundDemo;

var
  R1: Real;
  R2: Real;
  I1: Integer;
  I2: Integer;

begin
  R1 := 3.7;
  R2 := -3.7;
  I1 := Round(R1);
  I2 := Round(R2);
  WriteLn('Round(3.7) = ', I1);
  WriteLn('Round(-3.7) = ', I2);
end.
```

## Related Errors

- [Overflow error](/languages/pascal/pascal-overflow-error)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
- [Runtime error](/languages/pascal/pascal-runtime-error)
