---
title: "[Solution] Pascal SUCC and PRED Error"
description: "Fix Pascal SUCC and PRED function errors when computing successor or predecessor of ordinal values."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

SUCC and PRED errors occur when computing successor or predecessor of values at the boundaries of their ordinal range.

## Common Causes

- SUCC of maximum ordinal value overflows
- PRED of minimum ordinal value underflows
- SUCC/PRED on real types (not ordinal)
- Using SUCC/PRED on non-contiguous types

## How to Fix

### 1. Check bounds before calling

```pascal
var
  N: Integer;
begin
  N := MaxInt;
  if N < MaxInt then
    WriteLn(Succ(N))
  else
    WriteLn('Cannot compute successor');
end;
```

### 2. Use Inc/Dec for better performance

```pascal
var N: Integer;
begin
  N := 10;
  Inc(N);  // same as N := Succ(N)
  Dec(N);  // same as N := Pred(N)
end;
```

## Examples

```pascal
program SuccPredDemo;

var
  Ch: Char;
  Num: Integer;

begin
  Ch := 'A';
  WriteLn('Succ of A is ', Succ(Ch));
  WriteLn('Pred of C is ', Pred('C'));
  Num := 42;
  WriteLn('Succ of 42 is ', Succ(Num));
end.
```

## Related Errors

- [Overflow error](/languages/pascal/pascal-overflow-error)
- [Range check error](/languages/pascal/range-check)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
