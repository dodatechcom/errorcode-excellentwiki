---
title: "Stack overflow"
description: "A stack overflow occurs when the call stack exceeds its maximum depth due to infinite recursion."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["stack", "overflow", "recursion", "pascal"]
weight: 5
---

## What This Error Means

A `Stack overflow` error occurs when a function calls itself recursively without reaching a base case, causing the call stack to exceed its memory limit.

## Common Causes

- Infinite recursion with no base case
- Very deep recursion
- Missing termination condition
- Local variables too large for stack

## How to Fix

```pascal
program StackOverflowDemo;

function Factorial(n: Integer): Integer;
begin
  if n <= 0 then
    Factorial := 1
  else
    Factorial := n * Factorial(n - 1);  // may overflow for large n
end;

begin
  WriteLn(Factorial(10000));  // Stack overflow
end.
```

```pascal
program TailRecursionDemo;

function Factorial(n: Integer; acc: Integer): Integer;
begin
  if n <= 0 then
    Factorial := acc
  else
    Factorial := Factorial(n - 1, n * acc);  // tail recursive
end;

begin
  WriteLn(Factorial(10000, 1));  // works (with TCO)
end.
```

```pascal
program IterativeDemo;

function Factorial(n: Integer): Integer;
var
  i, result: Integer;
begin
  result := 1;
  for i := 1 to n do
    result := result * i;
  Factorial := result;
end;

begin
  WriteLn(Factorial(20));  // works iteratively
end.
```

## Examples

```pascal
program StackOverflowExample;

function Infinite: Integer;
begin
  Infinite := Infinite;  // no base case
end;

begin
  WriteLn(Infinite);  // Stack overflow
end.
```

## Related Errors

- [Overflow error](/languages/pascal/overflow-error3)
- [Invalid pointer operation](/languages/pascal/invalid-pointer)
