---
title: "[Solution] Pascal: stack overflow error"
description: "Fix Pascal runtime errors when the call stack exceeds its allocated size due to deep recursion or large local variables."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["stack", "overflow", "recursion", "local-variable", "memory", "pascal"]
weight: 5
---

## What This Error Means

Pascal stack overflow occurs when the program's call stack exceeds its allocated memory, typically from deep recursion or excessive local variable allocation.

## Common Causes

- Infinite recursion
- Deep recursion without base case
- Large local arrays
- Too many nested procedure calls
- Stack size too small

## How to Fix

```pascal
program StackOverflow;
procedure Recursive;
begin
  Recursive;  // Infinite recursion
end;

begin
  Recursive;
end.
```

```pascal
program SafeRecursion;
function Factorial(n: Integer): Integer;
begin
  if n <= 1 then
    Factorial := 1  // Base case
  else
    Factorial := n * Factorial(n - 1);
end;

begin
  WriteLn(Factorial(10));
end.
```

```pascal
program LargeLocalArray;
var
  arr: array[1..1000000] of Integer;  // Too large for stack
begin
  // Use heap instead
end.
```

```pascal
program HeapAllocation;
var
  arr: ^array[1..1000000] of Integer;
begin
  New(arr);
  try
    // Use arr^
  finally
    Dispose(arr);
  end;
end.
```

```pascal
program IterativeSolution;
function Factorial(n: Integer): Integer;
var
  i, result: Integer;
begin
  result := 1;
  for i := 2 to n do
    result := result * i;
  Factorial := result;
end;

begin
  WriteLn(Factorial(100));
end.
```

## Related Errors

- [Runtime Error](pascal-runtime-error-v2) - general runtime
- [Invalid Pointer](pascal-invalid-pointer-v2) - pointer errors
- [Heap Error](pascal-heap-error) - heap errors
