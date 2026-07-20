---
title: "[Solution] Pascal Dynamic Array Error — How to Fix"
description: "Fix dynamic array errors in Pascal when managing heap-allocated variable-length arrays."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1062
---

# Dynamic Array Error

Dynamic arrays (`array of Type`) are reference-counted heap objects in Pascal. Errors occur when accessing uninitialized arrays, out-of-bounds indexing, or when the reference count drops to zero unexpectedly.

## Common Causes

- Accessing elements before `SetLength` is called
- Index out of bounds (0 to Length-1)
- Copying an array shares the reference (not a deep copy)
- Circular references preventing deallocation

## How to Fix

### Solution 1 — Always SetLength before use

```pascal
program DynamicArrayFix;

var
  Arr: array of Integer;
  I: Integer;
begin
  SetLength(Arr, 10);     // allocate 10 elements
  for I := 0 to High(Arr) do
    Arr[I] := I * I;
  for I := Low(Arr) to High(Arr) do
    WriteLn(Arr[I]);
end.
```

### Solution 2 — Check bounds before access

```pascal
program SafeAccess;

var
  Arr: array of string;
  Idx: Integer;
begin
  SetLength(Arr, 5);
  Idx := 10;
  if (Idx >= Low(Arr)) and (Idx <= High(Arr)) then
    WriteLn(Arr[Idx])
  else
    WriteLn('Index out of range');
end.
```

### Solution 3 — Deep copy with Copy function

```pascal
program DeepCopy;

var
  A, B: array of Integer;
  I: Integer;
begin
  SetLength(A, 5);
  for I := 0 to 4 do A[I] := I;
  B := Copy(A);           // deep copy, not reference
  B[0] := 999;
  WriteLn(A[0], ' ', B[0]);  // 0  999
end.
```

### Solution 4 — Resize dynamically

```pascal
program DynamicResize;

var
  Arr: array of Double;
  Count: Integer;
begin
  SetLength(Arr, 0);
  Count := 0;
  // Simulate adding elements
  while Count < 100 do
  begin
    Inc(Count);
    SetLength(Arr, Count);
    Arr[Count - 1] := Count * 1.5;
  end;
  WriteLn('Final length: ', Length(Arr));
end.
```

## Examples

A sorting algorithm accesses `Arr[Length(Arr)]` — one past the end. This causes an out-of-bounds error. Changing the loop to use `High(Arr)` (which is `Length(Arr) - 1`) fixes the access.

## Related Errors

- [SetLength Error](/languages/pascal/pascal-setlength-error) — allocation issues
- [Array Bounds Error](/languages/pascal/pascal-array-bounds-error) — index out of range
- [Heap Error](/languages/pascal/pascal-heap-error) — memory allocation
