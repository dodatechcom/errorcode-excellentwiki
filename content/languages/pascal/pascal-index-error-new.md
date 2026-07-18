---
title: "[Solution] Pascal: range check error or index out of bounds"
description: "Fix Pascal range check errors by enabling range checking and validating array and string indices."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Pascal range check error occurs when a program accesses an array, string, or enumerated type using a value outside its declared valid range. This runtime error is detected when range checking is enabled (compiler directive `{$R+}` or `{$RANGECHECKS ON}`). The error is sometimes reported as `Runtime error 201` or `Range check error`. Without range checking enabled, the program silently reads or writes incorrect memory, leading to data corruption and unpredictable behavior.

## Why It Happens

Range check errors in Pascal occur when an index variable exceeds the bounds of an array or when an integer assignment overflows the target type's range. Off-by-one errors in loop boundaries are the most frequent cause, such as accessing `arr[11]` when the array is declared as `array[1..10]`. Using a loop variable after the loop has ended, when its value has incremented one past the upper bound, is another common scenario. Assigning a value outside the range of an enumerated type or subrange type triggers this error. String indices that exceed the string length when accessing individual characters also cause range violations. Negative indices used on arrays that start at 1 are another source of range check failures.

## How to Fix It

**Enable range checking during development:**

```pascal
{$R+}  { Enable range checking }
{$RANGECHECKS ON}  { Alternative syntax }

program RangeCheckDemo;
var
  arr: array[1..10] of Integer;
  i: Integer;
begin
  for i := 1 to 10 do
    arr[i] := i * 2;
  { arr[11] would trigger range check error }
end.
```

**Use Low and High to get valid bounds:**

```pascal
program SafeBounds;
var
  arr: array[1..100] of Integer;
  i: Integer;
begin
  for i := Low(arr) to High(arr) do
    arr[i] := i;

  WriteLn('Array bounds: ', Low(arr), ' to ', High(arr));
end.
```

**Check indices before access:**

```pascal
program SafeAccess;
var
  arr: array[1..5] of Integer;
  idx: Integer;
begin
  arr[1] := 10;
  arr[2] := 20;
  idx := 3;

  if (idx >= Low(arr)) and (idx <= High(arr)) then
    WriteLn('Value: ', arr[idx])
  else
    WriteLn('Index out of range');
end.
```

**Fix loop boundary errors:**

```pascal
program LoopBounds;
var
  arr: array[1..10] of Integer;
  i: Integer;
begin
  { WRONG: i goes one past the end }
  { for i := 1 to 11 do arr[i] := 0; }

  { CORRECT: use High }
  for i := 1 to High(arr) do
    arr[i] := 0;
end.
```

**Handle string character access safely:**

```pascal
program SafeString;
var
  s: string;
  i: Integer;
begin
  s := 'Hello';
  for i := 1 to Length(s) do
    WriteLn('Char ', i, ': ', s[i]);
end.
```

## Common Mistakes

- Forgetting that Pascal arrays are 1-indexed by default, not 0-indexed
- Using a loop variable after the loop ends, when it is one past the upper bound
- Not enabling range checking in development, allowing silent memory corruption
- Assuming that `High(arr)` is always the declared size minus one
- Accessing string characters with index 0, which is reserved for the length byte in short strings

## Related Pages

- [Division by zero in Pascal](/languages/pascal/pascal-division-by-zero-v2)
- [Stack overflow in Pascal](/languages/pascal/pascal-stack-overflow-v2)
- [Runtime error in Pascal](/languages/pascal/pascal-runtime-error-v2)
- [Invalid pointer operation in Pascal](/languages/pascal/pascal-invalid-pointer-v2)
