---
title: "Overflow error in Pascal"
description: "Overflow error in Pascal occurs when an arithmetic result exceeds the maximum value of the integer type."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An overflow error occurs when an arithmetic operation produces a value that cannot be stored in the target data type. Pascal reports this as a runtime error when overflow checking is enabled.

## Common Causes

- Multiplication of large integers
- Accumulating large sums
- Factorial computation on small integers
- Missing overflow checks

## How to Fix

```pascal
program OverflowDemo;

var
  a, b, result: Integer;

begin
  // Enable overflow checking
  {$Q+}

  a := 30000;
  b := 100;
  result := a * b;   // Overflow: exceeds Integer range
end.
```

```pascal
// Use larger data types
program SafeOverflow;

var
  a, b: Integer;
  result: Int64;   // Use 64-bit integer

begin
  a := 30000;
  b := 100;
  result := Int64(a) * Int64(b);   // 3000000 - fits in Int64
  WriteLn('Result: ', result);
end.
```

## Examples

```pascal
program Example;
var
  x: Integer;
begin
  x := 32767;    // Max for 16-bit Integer
  x := x + 1;    // Overflow error
end.
```

## Related Errors

- [Division by Zero](/languages/pascal/division-by-zero) - arithmetic errors
- [Runtime Error](/languages/pascal/pascal-runtime-error) - general errors
