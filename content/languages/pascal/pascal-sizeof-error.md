---
title: "[Solution] Pascal SIZEOF Function Error"
description: "Fix Pascal SIZEOF function errors when querying the byte size of types or variables incorrectly."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

SIZEOF function errors occur when SIZEOF is used on incomplete types, dynamic arrays, or when the result is used incorrectly.

## Common Causes

- SIZEOF on dynamic array returns pointer size
- SIZEOF on incomplete type definition
- Using SIZEOF for type comparison incorrectly
- SIZEOF on string type returning different values across compilers

## How to Fix

### 1. Use SIZEOF on concrete types

```pascal
var
  Size: SizeInt;
begin
  Size := SizeOf(Integer);     // typically 4
  Size := SizeOf(Double);      // typically 8
  Size := SizeOf(TRecord);     // sum of fields
end;
```

### 2. Account for dynamic arrays

```pascal
var
  Arr: array of Integer;
begin
  // SizeOf(Arr) is pointer size, not array size
  WriteLn('Array length: ', Length(Arr));
end;
```

## Examples

```pascal
program SizeOfDemo;

type
  TPoint = record
    X, Y: Integer;
  end;

begin
  WriteLn('Size of Integer: ', SizeOf(Integer));
  WriteLn('Size of Char: ', SizeOf(Char));
  WriteLn('Size of TPoint: ', SizeOf(TPoint));
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
- [Compile error](/languages/pascal/pascal-compiler-error-new)
