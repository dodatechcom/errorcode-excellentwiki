---
title: "[Solution] Pascal ABS Function Error"
description: "Fix Pascal ABS function errors when computing absolute values that overflow the target type."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

ABS function errors occur when the absolute value of the minimum integer overflows, or when ABS is called on non-numeric types.

## Common Causes

- ABS of MinInt overflows (same absolute value)
- ABS on real type producing oversized result
- ABS result assigned to too-small integer type
- ABS on non-numeric type

## How to Fix

### 1. Check for overflow

```pascal
var
  N: Integer;
  AbsN: Integer;
begin
  N := -32768;
  AbsN := Abs(N);  // may overflow on 16-bit
end;
```

### 2. Use larger type for result

```pascal
var
  N: Integer;
  AbsN: Int64;
begin
  N := -2147483648;
  AbsN := Abs(Int64(N));  // safe
end.
```

## Examples

```pascal
program AbsDemo;

var
  Value: Integer;
  Result: Integer;

begin
  Value := -42;
  Result := Abs(Value);
  WriteLn('Absolute value of ', Value, ' is ', Result);
end.
```

## Related Errors

- [Overflow error](/languages/pascal/pascal-overflow-error)
- [Range check error](/languages/pascal/range-check)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
