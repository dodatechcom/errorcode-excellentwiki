---
title: "Division by zero"
description: "A division by zero error occurs when attempting to divide an integer by zero."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["division", "zero", "arithmetic", "pascal"]
weight: 5
---

## What This Error Means

A `Division by zero` error occurs when you attempt to divide an integer by zero. This is undefined mathematically and raises a runtime error in Pascal.

## Common Causes

- Dividing by variable that evaluates to zero
- Missing zero-check before division
- User input not validated
- Denominator computation error

## How to Fix

```pascal
program DivByZeroDemo;

var
  a, b, result: Integer;

begin
  a := 10;
  b := 0;

  if b = 0 then
    WriteLn('Cannot divide by zero')
  else
  begin
    result := a div b;
    WriteLn('Result: ', result);
  end;
end.
```

```pascal
program SafeDivide;

function SafeDiv(a, b: Integer): Integer;
begin
  if b = 0 then
    SafeDiv := 0  // or raise exception
  else
    SafeDiv := a div b;
end;

begin
  WriteLn(SafeDiv(10, 0));  // 0
  WriteLn(SafeDiv(10, 2));  // 5
end.
```

## Examples

```pascal
program DivByZeroExample;

var
  a, b: Integer;

begin
  a := 10;
  b := 0;
  WriteLn(a div b);  // Division by zero

  WriteLn(a / b);    // Division by zero (real division)
end.
```

## Related Errors

- [Overflow error](/languages/pascal/overflow-error3)
- [Range check error](/languages/pascal/range-check)
