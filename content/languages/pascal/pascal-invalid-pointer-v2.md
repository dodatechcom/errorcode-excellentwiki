---
title: "[Solution] Pascal: invalid pointer operation error"
description: "Fix Pascal runtime errors when performing invalid pointer operations like dereferencing nil or accessing freed memory."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["pointer", "invalid", "nil", "dereference", "memory", "pascal"]
weight: 5
---

## What This Error Means

Pascal invalid pointer operations occur when dereferencing a nil pointer, accessing freed memory, or performing illegal pointer arithmetic.

## Common Causes

- Dereferencing nil pointer
- Accessing memory after Dispose
- Invalid pointer arithmetic
- Uninitialized pointer
- Double free

## How to Fix

```pascal
program InvalidPointer;
var
  p: ^Integer;
begin
  New(p);
  Dispose(p);
  p^ := 42;  // Invalid: accessing freed memory
end.
```

```pascal
program SafePointer;
var
  p: ^Integer;
begin
  New(p);
  try
    p^ := 42;
    WriteLn(p^);
  finally
    Dispose(p);
  end;
end.
```

```pascal
program NilCheck;
var
  p: ^Integer;
begin
  p := nil;
  
  if p <> nil then
    WriteLn(p^)
  else
    WriteLn('Pointer is nil');
end.
```

```pascal
program PointerArithmetic;
var
  arr: array[1..5] of Integer;
  p: ^Integer;
begin
  p := @arr[1];
  
  // Valid pointer arithmetic
  Inc(p);  // Move to arr[2]
  WriteLn(p^);
  
  // Check bounds
  if (p >= @arr[1]) and (p <= @arr[5]) then
    WriteLn('Valid pointer');
end.
```

```pascal
program ManagedPointer;
type
  TMyObject = record
    Value: Integer;
  end;

var
  obj: ^TMyObject;
begin
  New(obj);
  try
    obj^.Value := 100;
    WriteLn(obj^.Value);
  finally
    Dispose(obj);
  end;
end.
```

## Related Errors

- [Heap Error](pascal-heap-error) - heap memory errors
- [Stack Overflow](pascal-stack-overflow-v2) - stack errors
- [Runtime Error](pascal-runtime-error-v2) - general runtime
