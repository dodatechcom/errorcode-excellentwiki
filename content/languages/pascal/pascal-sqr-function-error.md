---
title: "[Solution] Pascal SQR Function Error"
description: "Fix Pascal SQR function errors when squaring numbers that overflow the result type."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

SQR function errors occur when squaring a number produces a result that exceeds the target type's range.

## Common Causes

- SQR of large integer overflows
- SQR result assigned to too-small type
- SQR on non-numeric type
- Negative input to SQR producing positive overflow

## How to Fix

### 1. Use larger type for result

```pascal
var
  N: Integer;
  Sq: Int64;
begin
  N := 100000;
  Sq := Sqr(Int64(N));  // prevent overflow
end;
```

### 2. Check range before squaring

```pascal
if Abs(N) <= Sqrt(MaxInt) then
  Result := Sqr(N)
else
  WriteLn('Overflow');
```

## Examples

```pascal
program SqrDemo;

var
  Num: Integer;
  Square: Integer;

begin
  Num := 7;
  Square := Sqr(Num);
  WriteLn(Num, ' squared is ', Square);
end.
```

## Related Errors

- [Overflow error](/languages/pascal/pascal-overflow-error)
- [Range check error](/languages/pascal/range-check)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
