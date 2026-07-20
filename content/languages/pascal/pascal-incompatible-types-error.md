---
title: "[Solution] Pascal Incompatible Types Error — How to Fix"
description: "Fix incompatible types errors in Pascal when assigning or comparing values of structurally different types."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1040
---

# Incompatible Types Error

Pascal requires explicit type compatibility between operands. Incompatible types errors arise when the compiler detects two types that cannot be implicitly converted, even if they have the same underlying representation.

## Common Causes

- Assigning one enumerated type to another without conversion
- Passing a `String` variable where a `PChar` is expected
- Comparing typed constants of different types
- Using a typed file variable where a text file is expected

## How to Fix

### Solution 1 — Use explicit type conversion

```pascal
program IncompatibleDemo;

type
  TColor = (clRed, clGreen, clBlue);
  TSize = (szSmall, szMedium, szLarge);

var
  c: TColor;
  s: TSize;
begin
  c := clRed;
  s := TSize(Ord(c));    // explicit Ord conversion
end.
```

### Solution 2 — Use intermediary types

```pascal
program IntermediaryDemo;

var
  a: AnsiString;
  w: WideString;
  p: PChar;
begin
  a := 'Hello';
  w := WideString(a);    // explicit conversion through WideString
  p := PChar(w);         // then to PChar
end.
```

### Solution 3 — Declare compatible types

```pascal
program CompatibleTypesDemo;

type
  TIntArray = array of Integer;
  TMyArray = array of Integer;  // different type name, same structure

var
  a: TIntArray;
  b: TMyArray;  // NOT compatible — must use same type
begin
  SetLength(a, 5);
  // b := a;  // ERROR: incompatible types
  b := TIntArray(a);  // explicit cast works
end.
```

### Solution 4 — Use Variant for dynamic typing

```pascal
program VariantDemo;

var
  v: Variant;
  i: Integer;
  s: string;
begin
  v := 42;         // Integer
  v := 'Hello';    // now String
  i := Integer(v); // explicit conversion
end.
```

## Examples

Two enumerated types `TDay` and `TMonth` are used interchangeably. Assigning a `TDay` value to a `TMonth` variable causes an incompatible types error. The fix is to use `Ord()` and `Succ()`/`Pred()` for conversion, or redesign to use a common base type.

## Related Errors

- [Type Mismatch](/languages/pascal/pascal-type-mismatch) — assignment type issues
- [Ordinal Type](/languages/pascal/pascal-ordinal-type-error) — ordinal restrictions
- [Variant Error](/languages/pascal/pascal-variant-error) — variant conversion
