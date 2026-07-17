---
title: "[Solution] Pascal Division by Zero — Runtime Error Fix"
description: "Fix Pascal division by zero errors. Learn why dividing by zero crashes and how to add checks before division operations."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Division by Zero — Runtime Error Fix

A `Division by zero` error occurs when you attempt to divide an integer by zero. Pascal raises a runtime error for integer division by zero (unlike some languages that return `Infinity` for floats).

## Description

In Pascal, dividing an integer by zero is undefined and causes a runtime error. The standard `div` operator and the `/` operator (when used with integers) both trigger this error when the divisor is zero. With floating-point types, the behavior depends on the compiler — some may produce `Infinity` or `NaN`, while others raise an error.

Common scenarios:

- **Direct division by zero** — `x div 0` or `x / 0`.
- **Computed divisor** — the divisor is computed at runtime and happens to be zero.
- **User input** — a denominator entered by the user is zero.
- **Array index from division** — using a division result as an array index.

## Common Causes

```pascal
program DivisionByZeroDemo;

var
  a, b, result: Integer;
  floatResult: Real;

begin
  // Cause 1: Direct division by zero
  result := 10 div 0;  // Runtime error: Division by zero

  // Cause 2: Divisor from computation
  a := 10;
  b := a - 10;  // b = 0
  result := 100 div b;  // Runtime error

  // Cause 3: User input
  Write('Enter divisor: ');
  ReadLn(b);
  result := 100 div b;  // Runtime error if b = 0

  // Cause 4: Float division by zero
  floatResult := 10.0 / 0.0;  // May produce Infinity or error
end.
```

## How to Fix

### Fix 1: Check divisor before dividing

```pascal
// Wrong
result := 100 div divisor;

// Correct
if divisor <> 0 then
  result := 100 div divisor
else
  WriteLn('Cannot divide by zero');
```

### Fix 2: Use a function with built-in check

```pascal
function SafeDiv(a, b: Integer): Integer;
begin
  if b = 0 then
  begin
    WriteLn('Warning: division by zero, returning 0');
    SafeDiv := 0;
  end
  else
    SafeDiv := a div b;
end;

// Usage
result := SafeDiv(100, 0);  // Returns 0 with warning
```

### Fix 3: Validate user input before use

```pascal
// Wrong
Write('Enter a number: ');
ReadLn(divisor);
result := 100 div divisor;

// Correct
Write('Enter a non-zero number: ');
ReadLn(divisor);
if divisor = 0 then
  WriteLn('Error: divisor cannot be zero')
else
  result := 100 div divisor;
```

### Fix 4: Guard in loops with computed divisors

```pascal
// Wrong
for i := 1 to 10 do
begin
  result := 100 div (i - i);  // Always zero on first iteration
end;

// Correct
for i := 1 to 10 do
begin
  divisor := i - 1;
  if divisor <> 0 then
    result := 100 div divisor
  else
    WriteLn('Skipping i = ', i, ': division by zero');
end;
```

## Examples

```pascal
program DivisionByZeroExample;

var
  numerator, denominator, quotient: Integer;

begin
  numerator := 42;
  denominator := 0;

  // This triggers: Division by zero
  quotient := numerator div denominator;
  WriteLn('Quotient: ', quotient);
end.
```

## Related Errors

- [range-check] — value assigned outside the allowed range.
- [Overflow error] — arithmetic result exceeds integer capacity.
- [Invalid numeric format] — string cannot be converted to a number.
