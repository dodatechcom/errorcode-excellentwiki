---
title: "[Solution] Pascal SetLength Error — How to Fix"
description: "Fix SetLength errors in Pascal when allocating or resizing dynamic arrays and strings."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1063
---

# SetLength Error

`SetLength` allocates or resizes a dynamic array or long string. Errors occur when passing negative sizes, exceeding available memory, or calling `SetLength` on a non-dynamic variable.

## Common Causes

- Passing a negative value to `SetLength` (runtime error)
- Requesting more memory than available (out of memory)
- Calling `SetLength` on a static array or constant
- `SetLength` on a string type with non-UTF8 encoding causing unexpected behavior

## How to Fix

### Solution 1 — Validate size before SetLength

```pascal
program SafeSetLength;

var
  Arr: array of Integer;
  NewSize: Integer;
begin
  NewSize := 1000;
  if NewSize >= 0 then
    SetLength(Arr, NewSize)
  else
    WriteLn('Invalid size');
end.
```

### Solution 2 — Handle out-of-memory gracefully

```pascal
program OOMSafe;

var
  Arr: array of Byte;
begin
  try
    SetLength(Arr, 100 * 1024 * 1024);  // 100 MB
  except
    on E: OutOfMemoryError do
      WriteLn('Not enough memory');
  end;
end.
```

### Solution 3 — SetLength on strings

```pascal
program StringSetLength;

var
  S: AnsiString;
begin
  SetLength(S, 100);     // allocate 100-character string
  FillChar(S[1], Length(S), 'A');
  WriteLn(S);
end.
```

### Solution 4 — Shrink arrays safely

```pascal
program ShrinkArray;

var
  Arr: array of Integer;
  I: Integer;
begin
  SetLength(Arr, 100);
  for I := 0 to 99 do Arr[I] := I;
  SetLength(Arr, 10);    // shrink — elements 10..99 are discarded
  WriteLn('New length: ', Length(Arr));
end.
```

## Examples

A user enters a negative number for array size. `SetLength(Arr, -5)` triggers runtime error 201. Adding a range check before the call prevents the crash.

## Related Errors

- [Dynamic Array Error](/languages/pascal/pascal-dynamic-array-error) — array management
- [Heap Error](/languages/pascal/pascal-heap-error) — memory allocation
- [Index Out of Range](/languages/pascal/pascal-index-out-of-range) — bounds checking
