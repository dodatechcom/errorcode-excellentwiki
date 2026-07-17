---
title: "Index out of range in Pascal"
description: "Index out of range errors in Pascal occur when accessing array elements beyond the declared bounds."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["index", "range", "array", "bounds", "pascal"]
weight: 5
---

## What This Error Means

Pascal arrays have fixed bounds declared in the type definition. Accessing an element outside these bounds causes a range check error when range checking is enabled.

## Common Causes

- Array index exceeds declared upper bound
- Array index below declared lower bound
- Off-by-one errors in loops
- Loop counter exceeding array size

## How to Fix

```pascal
program RangeCheckDemo;

var
  arr: array[1..5] of Integer;
  i: Integer;

begin
  // Enable range checking
  {$R+}

  for i := 1 to 5 do
    arr[i] := i * 10;   // Correct

  // arr[0] and arr[6] would cause range error
end.
```

```pascal
// CORRECT: Use Length() for bounds
program SafeAccess;

var
  arr: array[1..5] of Integer;
  i: Integer;

begin
  for i := 1 to Length(arr) do
    arr[i] := i * 10;
end.
```

## Examples

```pascal
program Example;
var
  a: array[1..3] of Integer;
begin
  a[1] := 10;
  a[2] := 20;
  a[3] := 30;
  WriteLn(a[4]);   // Range check error
end.
```

## Related Errors

- [Runtime Error](/languages/pascal/pascal-runtime-error) - general errors
- [Division by Zero](/languages/pascal/division-by-zero) - arithmetic errors
