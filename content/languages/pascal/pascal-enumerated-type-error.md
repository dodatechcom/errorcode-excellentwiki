---
title: "[Solution] Pascal Enumerated Type Error — How to Fix"
description: "Fix enumerated type errors in Pascal when using enum values incorrectly or mixing different enum types."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1043
---

# Enumerated Type Error

Enumerated types define a set of named constants. Errors occur when mixing different enums, assigning out-of-range ordinals, or using string literals where enum values are expected.

## Common Causes

- Assigning one enumerated type to another without conversion
- Using `Ord()` on an enum and assigning back without range check
- Comparing enums from different types
- Assigning an integer outside the enum's ordinal range

## How to Fix

### Solution 1 — Use explicit ordinal conversion

```pascal
program EnumFix;

type
  TSeason = (Spring, Summer, Autumn, Winter);
  TQuarter = (Q1, Q2, Q3, Q4);

var
  s: TSeason;
  q: TQuarter;
begin
  s := Summer;
  q := TQuarter(Ord(s));  // explicit conversion
end.
```

### Solution 2 — Create conversion functions

```pascal
program EnumConversion;

type
  TColor = (clRed, clGreen, clBlue);
  TColorIndex = 0..2;

function ColorToIndex(C: TColor): TColorIndex;
begin
  Result := Ord(C);
end;

function IndexToColor(I: TColorIndex): TColor;
begin
  Result := TColor(I);
end;
```

### Solution 3 — Use case statements for safe mapping

```pascal
program SafeMapping;

type
  TDay = (Mon, Tue, Wed, Thu, Fri, Sat, Sun);

function DayName(D: TDay): string;
begin
  case D of
    Mon: Result := 'Monday';
    Tue: Result := 'Tuesday';
    Wed: Result := 'Wednesday';
    Thu: Result := 'Thursday';
    Fri: Result := 'Friday';
    Sat: Result := 'Saturday';
    Sun: Result := 'Sunday';
  end;
end;
```

### Solution 4 — Validate enum ordinals

```pascal
function IsValidSeason(V: Integer): Boolean;
begin
  Result := (V >= Ord(Low(TSeason))) and (V <= Ord(High(TSeason)));
end;
```

## Examples

Two unrelated enums `TFruit` and `TVegetable` are confused. Assigning a fruit to a vegetable variable causes an incompatible types error. Converting through `Ord()` is the only way to transfer between them.

## Related Errors

- [Ordinal Type](/languages/pascal/pascal-ordinal-type-error) — ordinal operations
- [Type Mismatch](/languages/pascal/pascal-type-mismatch) — type compatibility
- [Subrange Type](/languages/pascal/pascal-subrange-type-error) — range restrictions
