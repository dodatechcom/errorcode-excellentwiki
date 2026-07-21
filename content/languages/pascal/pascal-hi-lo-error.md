---
title: "[Solution] Pascal HI and LO Function Error"
description: "Fix Pascal HI and LO function errors when extracting high and low bytes from ordinal values."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

HI and LO function errors occur when called on types larger than expected or when the result is used with incorrect type assumptions.

## Common Causes

- HI/LO on integer types larger than 16 bits
- HI/LO on real types
- Using HI/LO result as full integer
- Not accounting for endianness

## How to Fix

### 1. Use HI/LO on word-sized values

```pascal
var
  W: Word;
  HiByte, LoByte: Byte;
begin
  W := $1234;
  HiByte := Hi(W);  // $12
  LoByte := Lo(W);  // $34
end;
```

### 2. Use for correct data types

```pascal
var
  N: Integer;
begin
  N := $00FF;
  WriteLn('High byte: ', Hi(N));
  WriteLn('Low byte: ', Lo(N));
end;
```

## Examples

```pascal
program HiLoDemo;

var
  Value: Word;
  HiVal: Byte;
  LoVal: Byte;

begin
  Value := $ABCD;
  HiVal := Hi(Value);
  LoVal := Lo(Value);
  WriteLn('Hi: $', HexStr(HiVal, 2));
  WriteLn('Lo: $', HexStr(LoVal, 2));
end.
```

## Related Errors

- [Type mismatch](/languages/pascal/pascal-type-mismatch)
- [Range check error](/languages/pascal/range-check)
- [Runtime error](/languages/pascal/pascal-runtime-error)
