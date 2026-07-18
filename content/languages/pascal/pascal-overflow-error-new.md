---
title: "[Solution] Pascal: arithmetic overflow error"
description: "Fix Pascal arithmetic overflow by using larger integer types and checking value ranges."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Pascal arithmetic overflow error occurs when a calculation produces a value that exceeds the range of the target data type. For standard Pascal, `Integer` is typically 16-bit (range -32768 to 32767) or 32-bit depending on the compiler. When a result exceeds this range, the program triggers Runtime error 206 (overflow) or produces incorrect wraparound values. Real number overflow occurs when intermediate calculations produce values too large for the `Real` type to represent, typically resulting in infinity or a runtime error.

## Why It Happens

Arithmetic overflow happens when calculations grow beyond the capacity of the data type being used. Multiplying two large integers can easily exceed 16-bit or even 32-bit ranges. Factorial calculations grow extremely fast: 13! exceeds 16-bit integer range. Accumulating sums in a loop without checking for overflow is a common source. Using `Byte` (0-255) or `ShortInt` (-128 to 127) for calculations that produce larger values causes overflow. Exponential calculations, particularly `Exp(x)` for large x values, can overflow the `Real` type. Power operations that raise large bases to high exponents frequently overflow. Counter variables in very long loops may overflow if the loop count exceeds the integer range.

## How to Fix It

**Use larger data types:**

```pascal
program LargerTypes;
var
  small_val: Integer;
  large_val: Int64;
  huge_val: QWord;
begin
  { WRONG: Integer overflow }
  { small_val := 50000; }  { Error if Integer is 16-bit }

  { CORRECT: use appropriate type }
  large_val := 50000;
  WriteLn('Large value: ', large_val);
  huge_val := High(QWord);
  WriteLn('Max QWord: ', huge_val);
end.
```

**Check for overflow before operations:**

```pascal
program OverflowCheck;
var
  a, b, result: Int64;
begin
  a := 2000000000;
  b := 2000000000;

  { Check before multiplication }
  if (a > 0) and (b > 0) and (a <= High(Int64) div b) then
  begin
    result := a * b;
    WriteLn('Result: ', result)
  end
  else
    WriteLn('Multiplication would overflow');
end.
```

**Use Int64 for intermediate calculations:**

```pascal
program IntermediateCalc;
var
  a, b: Integer;
  result: Int64;
begin
  a := 50000;
  b := 50000;

  { Promote to Int64 before multiplication }
  result := Int64(a) * Int64(b);
  WriteLn('Result: ', result);
end.
```

**Validate accumulated sums:**

```pascal
program SafeAccumulation;
var
  sum: Int64;
  i: Integer;
begin
  sum := 0;
  for i := 1 to 100000 do
  begin
    if sum <= High(Int64) - i then
      sum := sum + i
    else
    begin
      WriteLn('Overflow at i = ', i);
      Break
    end;
  end;
  WriteLn('Sum = ', sum);
end.
```

**Handle real overflow:**

```pascal
program RealOverflow;
var
  x, result: Real;
begin
  x := 710.0;

  { Exp(710) overflows Double }
  if x < 709.0 then
  begin
    result := Exp(x);
    WriteLn('e^', x:0:1, ' = ', result:0:2)
  end
  else
    WriteLn('Exp would overflow for x = ', x:0:1);
end.
```

## Common Mistakes

- Assuming `Integer` is always 32-bit when some compilers default to 16-bit
- Not considering that intermediate calculations may overflow even if the final result fits
- Using signed types for values that should always be unsigned
- Forgetting that subtraction of unsigned types can underflow
- Not checking for overflow when converting between different integer sizes

## Related Pages

- [Division by zero in Pascal](/languages/pascal/pascal-division-by-zero-v2)
- [Range check error in Pascal](/languages/pascal/pascal-index-error-new)
- [Stack overflow in Pascal](/languages/pascal/pascal-stack-overflow-v2)
- [Runtime error in Pascal](/languages/pascal/pascal-runtime-error-v2)
