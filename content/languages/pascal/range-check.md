---
title: "Range check error"
description: "A range check error occurs when a value is assigned outside the allowed range of a subrange type."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["range-check", "subrange", "bounds", "pascal"]
weight: 5
---

## What This Error Means

A `Range check error` occurs when a value is assigned to a variable whose type has a restricted range (subrange) and the value falls outside that range. This is a runtime error when range checking is enabled.

## Common Causes

- Integer overflow into subrange
- Array index out of range
- Character out of subrange
- Computed value exceeds type bounds

## How to Fix

```pascal
program RangeCheckDemo;

type
  DayRange = 1..31;

var
  day: DayRange;

begin
  {$R+}
  day := 35;  // Range check error

  // CORRECT: Validate first
  if (35 >= 1) and (35 <= 31) then
    day := 35
  else
    WriteLn('Invalid day');
end.
```

```pascal
program RangeCheckFix;

var
  arr: array[1..10] of Integer;
  idx: Integer;

begin
  {$R+}
  idx := 15;
  arr[idx] := 42;  // Range check error

  // CORRECT: Check bounds
  if (idx >= Low(arr)) and (idx <= High(arr)) then
    arr[idx] := 42
  else
    WriteLn('Index out of bounds');
end.
```

## Examples

```pascal
program RangeCheckExample;

type
  SmallInt = 0..100;
  LetterRange = 'A'..'Z';

var
  num: SmallInt;
  letter: LetterRange;

begin
  {$R+}
  num := 150;     // Range check error
  letter := 'a';  // Range check error
end.
```

## Related Errors

- [Overflow error](/languages/pascal/overflow-error3)
- [Division by zero](/languages/pascal/division-zero4)
