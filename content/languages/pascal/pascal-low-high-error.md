---
title: "[Solution] Pascal LOW and HIGH Function Error"
description: "Fix Pascal LOW and HIGH function errors when querying minimum and maximum values of ordinal types."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

LOW and HIGH function errors occur when querying bounds of types that do not have defined minimum or maximum values.

## Common Causes

- LOW/HIGH on real types (not ordinal)
- LOW/HIGH on dynamic arrays returning incorrect bounds
- Using LOW/HIGH for string bounds incorrectly
- LOW/HIGH on unbounded types

## How to Fix

### 1. Use LOW/HIGH on ordinal types

```pascal
var
  Lo, Hi: Integer;
begin
  Lo := Low(Integer);  // -2147483648
  Hi := High(Integer); // 2147483647
end;
```

### 2. Use for enumeration bounds

```pascal
type
  TColor = (Red, Green, Blue);
begin
  WriteLn('First: ', Ord(Low(TColor)));   // 0
  WriteLn('Last: ', Ord(High(TColor)));   // 2
end;
```

## Examples

```pascal
program LowHighDemo;

type
  TDay = (Mon, Tue, Wed, Thu, Fri, Sat, Sun);

var
  Day: TDay;

begin
  for Day := Low(TDay) to High(TDay) do
    WriteLn(Ord(Day), ': ', Day);
end.
```

## Related Errors

- [Type mismatch](/languages/pascal/pascal-type-mismatch)
- [Range check error](/languages/pascal/range-check)
- [Runtime error](/languages/pascal/pascal-runtime-error)
