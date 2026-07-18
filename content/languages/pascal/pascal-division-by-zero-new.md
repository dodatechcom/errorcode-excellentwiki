---
title: "[Solution] Pascal: division by zero runtime error"
description: "Fix Pascal division by zero by validating divisors and using SafeDiv functions with checks."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Pascal division by zero error occurs when a `div`, `mod`, or `/` operation has a divisor of zero. For integer division (`div` and `mod`), this causes an immediate runtime error (Runtime error 200). For real division (`/`), the result depends on the compiler and platform: it may produce infinity, NaN, or crash the program. Pascal does not provide built-in exception handling for arithmetic errors in standard Turbo Pascal, though Object Pascal (Delphi/FPC) offers try-except blocks.

## Why It Happens

Division by zero errors occur when divisor variables are not validated before use. User input that is not checked may contain zero values. Computed divisors from formulas or array lookups may unexpectedly be zero. In algorithms where the divisor is derived from data, edge cases such as empty data sets or boundary conditions can produce zero denominators. Loop-based calculations that compute the divisor iteratively may reach zero at certain iterations. Function return values used as divisors may return zero under certain conditions that were not anticipated during code design.

## How to Fix It

**Check the divisor before division:**

```pascal
program SafeDivision;
var
  a, b, result: Real;
begin
  a := 100.0;
  b := 0.0;

  if b <> 0.0 then
  begin
    result := a / b;
    WriteLn('Result: ', result:0:2)
  end
  else
    WriteLn('Error: Cannot divide by zero');
end.
```

**Create a reusable safe division function:**

```pascal
function SafeDiv(a, b: Real): Real;
begin
  if b = 0.0 then
    SafeDiv := 0.0
  else
    SafeDiv := a / b;
end;

function SafeMod(a, b: Integer): Integer;
begin
  if b = 0 then
    SafeMod := 0
  else
    SafeMod := a mod b;
end;
```

**Validate user input:**

```pascal
program ValidatedInput;
var
  numerator, denominator, quotient: Integer;
begin
  Write('Enter numerator: ');
  ReadLn(numerator);
  Write('Enter denominator: ');
  ReadLn(denominator);

  if denominator <> 0 then
  begin
    quotient := numerator div denominator;
    WriteLn('Quotient: ', quotient)
  end
  else
    WriteLn('Error: Denominator cannot be zero');
end.
```

**Use try-except in Object Pascal:**

```pascal
program TryExceptDemo;
{$mode objfpc}

uses SysUtils;

var
  a, b, result: Real;
begin
  a := 10.0;
  b := 0.0;

  try
    result := a / b;
    WriteLn('Result: ', result:0:2)
  except
    on E: EDivByZero do
      WriteLn('Division by zero caught: ', E.Message)
    on E: Exception do
      WriteLn('Error: ', E.Message)
  end;
end.
```

**Check array values before using as divisors:**

```pascal
program ArrayDivision;
var
  values: array[1..5] of Integer;
  quotients: array[1..5] of Real;
  i: Integer;
begin
  values[1] := 10; values[2] := 0; values[3] := 5;
  values[4] := 0; values[5] := 25;

  for i := 1 to 5 do
  begin
    if values[i] <> 0 then
      quotients[i] := 100.0 / values[i]
    else
      quotients[i] := 0.0;
  end;

  for i := 1 to 5 do
    WriteLn('100 / ', values[i], ' = ', quotients[i]:0:2);
end.
```

## Common Mistakes

- Assuming integer division and real division behave the same way on zero divisors
- Not checking divisors in helper functions that are called from multiple locations
- Using computed values as divisors without verifying the computation did not produce zero
- Forgetting that array elements may contain zero if not explicitly initialized
- Not handling the case where the divisor is the result of a subtraction that may yield zero

## Related Pages

- [Arithmetic overflow in Pascal](/languages/pascal/pascal-overflow-error-v2)
- [Range check error in Pascal](/languages/pascal/pascal-index-error-new)
- [Runtime error in Pascal](/languages/pascal/pascal-runtime-error-v2)
- [Stack overflow in Pascal](/languages/pascal/pascal-stack-overflow-v2)
