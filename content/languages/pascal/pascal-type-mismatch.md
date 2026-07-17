---
title: "Type mismatch in Pascal"
description: "Type mismatch errors in Pascal occur when assigning or comparing values of incompatible types."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Pascal is strongly typed and prevents implicit conversion between incompatible types. A type mismatch error occurs when you try to assign or compare values of different types without explicit conversion.

## Common Causes

- Assigning string to integer
- Comparing real to integer directly
- Passing wrong type to function parameter
- Variant type mismatch

## How to Fix

```pascal
program TypeMismatchDemo;

var
  s: String;
  n: Integer;

begin
  // WRONG: Type mismatch
  s := 'hello';
  n := s;   // Error: string to integer

  // CORRECT: Convert explicitly
  s := '42';
  n := StrToInt(s);
  WriteLn(n);
end.
```

```pascal
// CORRECT: Use type-compatible operations
program SafeTypeDemo;

var
  a: Integer;
  b: Real;

begin
  a := 10;
  b := 2.5;
  // Use explicit conversion
  if a = Round(b) then
    WriteLn('Equal');
  // Or convert integer to real
  if Real(a) = b then
    WriteLn('Equal as reals');
end.
```

## Examples

```pascal
program Example;
var
  x: Integer;
  y: String;
begin
  y := '10';
  x := y;   // Type mismatch: string to integer
end.
```

## Related Errors

- [Runtime Error](/languages/pascal/pascal-runtime-error) - general errors
- [Overflow Error](/languages/pascal/overflow-error3) - numeric errors
