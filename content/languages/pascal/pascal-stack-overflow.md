---
title: "Stack overflow in Pascal"
description: "Stack overflow in Pascal occurs when the call stack exceeds its limit, usually from unbounded recursion."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["stack", "overflow", "recursion", "memory", "pascal"]
weight: 5
---

## What This Error Means

Stack overflow in Pascal occurs when too many nested function calls exhaust the stack memory. This is most commonly caused by unbounded recursion.

## Common Causes

- Infinite recursion (missing base case)
- Very deep recursion
- Large local variables consuming stack space
- Circular function references

## How to Fix

```pascal
program StackOverflowDemo;

// WRONG: Infinite recursion
function BadFactorial(n: Integer): Integer;
begin
  BadFactorial := n * BadFactorial(n - 1);   // Stack overflow
end;
```

```pascal
// CORRECT: With base case
function GoodFactorial(n: Integer): Integer;
begin
  if n <= 1 then
    GoodFactorial := 1
  else
    GoodFactorial := n * GoodFactorial(n - 1);
end;
```

```pascal
// Use iterative approach to avoid recursion
function IterativeFactorial(n: Integer): Integer;
var
  i, result: Integer;
begin
  result := 1;
  for i := 2 to n do
    result := result * i;
  IterativeFactorial := result;
end;
```

## Examples

```pascal
program Example;

procedure InfiniteProc;
begin
  InfiniteProc;   // No base case - stack overflow
end;

begin
  InfiniteProc;
end.
```

## Related Errors

- [Runtime Error](/languages/pascal/pascal-runtime-error) - general errors
- [Invalid Pointer](/languages/pascal/invalid-pointer) - memory errors
