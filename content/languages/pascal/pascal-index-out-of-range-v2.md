---
title: "[Solution] Pascal: index out of range error"
description: "Fix Pascal runtime errors when array or string indices exceed their declared bounds."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["index", "out-of-range", "array", "bounds", "string", "pascal"]
weight: 5
---

## What This Error Means

Pascal index out of range occurs when accessing an array element or string character using an index outside the valid range.

## Common Causes

- Index exceeds upper bound
- Index below lower bound
- Off-by-one error in loops
- String index out of range
- Dynamic array bounds exceeded

## How to Fix

```pascal
program IndexError;
var
  arr: array[1..5] of Integer;
begin
  arr[10] := 42;  // Runtime error: index out of range
end.
```

```pascal
program SafeIndex;
var
  arr: array[1..5] of Integer;
  i: Integer;
begin
  for i := 1 to 5 do
    arr[i] := i * 2;
  
  // Check before access
  if (i >= Low(arr)) and (i <= High(arr)) then
    WriteLn(arr[i]);
end.
```

```pascal
program RangeChecking;
var
  arr: array[1..10] of Integer;
begin
  {$R+}  // Enable range checking
  arr[1] := 1;
  arr[11] := 2;  // Will trigger range check error
  {$R-}
end.
```

```pascal
program SafeStringAccess;
var
  s: string;
  i: Integer;
begin
  s := 'Hello';
  
  for i := 1 to Length(s) do
    WriteLn(s[i]);
  
  // Safe access
  if (i >= 1) and (i <= Length(s)) then
    WriteLn(s[i]);
end.
```

```pascal
program DynamicArray;
var
  arr: array of Integer;
  i: Integer;
begin
  SetLength(arr, 5);
  for i := 0 to High(arr) do
    arr[i] := i;
  
  // Check bounds
  if (i >= Low(arr)) and (i <= High(arr)) then
    WriteLn(arr[i]);
end.
```

## Related Errors

- [Runtime Error](pascal-runtime-error-v2) - general runtime
- [Division by Zero](pascal-division-by-zero-v2) - arithmetic errors
- [Stack Overflow](pascal-stack-overflow-v2) - stack errors
