---
title: "[Solution] Pascal ORD Function Error"
description: "Fix Pascal ORD function errors when converting ordinal types to integers with out-of-range values."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

ORD function errors occur when ORD is called on non-ordinal types or when CHR/ORD conversions produce out-of-range values.

## Common Causes

- ORD called on real or string type
- CHR with value outside 0..255
- ORD result used incorrectly as array index
- Type casting with ORD/CHR mismatch

## How to Fix

### 1. Use ORD only on ordinal types

```pascal
// WRONG: ORD on real
var R: Real;
N: Integer;
begin
  N := Ord(R);  // error: real not ordinal
end;

// CORRECT: Use ROUND or TRUNC
N := Round(R);
```

### 2. Validate CHR argument

```pascal
var Ch: Char;
Val: Integer;
begin
  Val := 65;
  if (Val >= 0) and (Val <= 255) then
    Ch := Chr(Val);
end.
```

## Examples

```pascal
program OrdDemo;

var
  Ch: Char;
  Code: Integer;

begin
  Ch := 'A';
  Code := Ord(Ch);
  WriteLn('ASCII of ', Ch, ' is ', Code);
  WriteLn('Character for 97 is ', Chr(97));
end.
```

## Related Errors

- [Type mismatch](/languages/pascal/pascal-type-mismatch)
- [Range check error](/languages/pascal/range-check)
- [Runtime error](/languages/pascal/pascal-runtime-error)
