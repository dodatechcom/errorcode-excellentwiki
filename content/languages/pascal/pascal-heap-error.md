---
title: "[Solution] Pascal: heap memory error"
description: "Fix Pascal runtime errors related to heap memory allocation, deallocation, and memory leaks."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Pascal heap errors occur when memory allocation fails, memory is accessed after being freed, or there are memory leaks from unfreed allocations.

## Common Causes

- Out of heap memory
- Accessing freed memory
- Memory leak (missing Dispose)
- Double free
- Invalid pointer operations

## How to Fix

```pascal
program HeapError;
var
  p: ^Integer;
begin
  New(p);
  Dispose(p);
  p^ := 42;  // Error: accessing freed memory
end.
```

```pascal
program SafeHeap;
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
program HeapAllocation;
var
  arr: array of Integer;
  i: Integer;
begin
  SetLength(arr, 1000);  // Allocates on heap
  
  for i := 0 to High(arr) do
    arr[i] := i;
  
  // Memory automatically freed when arr goes out of scope
end.
```

```pascal
program MemoryLeak;
var
  p: ^Integer;
begin
  p := New(p);
  p^ := 100;
  // Forgot Dispose(p) - memory leak!
end.
```

```pascal
program SafeMemory;
var
  p: ^Integer;
begin
  p := nil;
  
  New(p);
  try
    p^ := 100;
    WriteLn(p^);
  finally
    if p <> nil then
    begin
      Dispose(p);
      p := nil;
    end;
  end;
end.
```

```pascal
program ArrayHeap;
var
  matrix: array of array of Integer;
  i, j: Integer;
begin
  SetLength(matrix, 10, 10);
  
  for i := 0 to 9 do
    for j := 0 to 9 do
      matrix[i][j] := i * j;
  
  // Use matrix...
  
  SetLength(matrix, 0);  // Free memory
end.
```

## Related Errors

- [Invalid Pointer](pascal-invalid-pointer-v2) - pointer errors
- [Stack Overflow](pascal-stack-overflow-v2) - stack errors
- [Runtime Error](pascal-runtime-error-v2) - general runtime
