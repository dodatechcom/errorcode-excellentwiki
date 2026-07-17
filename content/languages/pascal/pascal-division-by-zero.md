---
title: "Division by zero in Pascal"
description: "Division by zero in Pascal occurs when dividing an integer by zero, causing a runtime error."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Pascal raises a runtime error when dividing an integer by zero using `div` or `/` with integers. This is undefined behavior that must be prevented by checking the divisor.

## Common Causes

- Direct division by zero
- Computed divisor that evaluates to zero
- User input resulting in zero divisor
- Uninitialized divisor variable

## How to Fix

```pascal
program DivByZeroDemo;

var
  a, b, result: Integer;

begin
  a := 100;
  b := 0;

  // Check before dividing
  if b <> 0 then
    result := a div b
  else
    WriteLn('Error: divisor is zero');
end.
```

```pascal
// Safe division function
function SafeDiv(a, b: Integer): Integer;
begin
  if b = 0 then
  begin
    WriteLn('Warning: division by zero');
    SafeDiv := 0;
  end
  else
    SafeDiv := a div b;
end;

// Usage
var
  q: Integer;
begin
  q := SafeDiv(100, 0);   // Returns 0 with warning
end.
```

## Examples

```pascal
program Example;
var
  numerator, denominator, quotient: Integer;
begin
  numerator := 42;
  denominator := 0;
  quotient := numerator div denominator;   // Runtime error
end.
```

## Related Errors

- [Overflow Error](/languages/pascal/overflow-error3) - arithmetic overflow
- [Index Out of Range](/languages/pascal/range-check) - array bounds
