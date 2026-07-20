---
title: "[Solution] Pascal Ordinal Type Error — How to Fix"
description: "Fix ordinal type errors in Pascal when operations require ordinal values but receive non-ordinal types."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1041
---

# Ordinal Type Error

Ordinal types in Pascal include integers, characters, booleans, and enumerations. Operations like `Ord()`, `Succ()`, `Pred()`, `Inc()`, `Dec()` require ordinal type operands. Passing a non-ordinal type (real, string, record) causes a compilation error.

## Common Causes

- Calling `Ord()` on a `Real` or `String` variable
- Using `Inc()`/`Dec()` on a float or pointer type
- Comparing non-ordinal types with `<`, `>`, `<=`, `>=`
- Using `Succ()`/`Pred()` on a set or array type

## How to Fix

### Solution 1 — Convert to ordinal before using ordinal functions

```pascal
program OrdinalFix;

var
  r: Real;
  i: Integer;
begin
  r := 3.14;
  i := Round(r);         // convert Real to Integer (ordinal)
  WriteLn(Ord(Chr(i)));  // now Ord works
end.
```

### Solution 2 — Use Round/Trunc for real-to-ordinal

```pascal
program RealToOrdinal;

var
  x: Real;
  n: Integer;
begin
  x := 42.7;
  n := Round(x);    // 43
  WriteLn(n);
end.
```

### Solution 3 — Check type before ordinal operations

```pascal
program SafeOrdinal;

procedure ProcessValue(const V: Variant);
begin
  if VarIsOrdinal(V) then
    WriteLn('Ordinal: ', Ord(V))
  else
    WriteLn('Not ordinal');
end;
```

### Solution 4 — Define custom Ord-like for records

```pascal
program CustomOrdinal;

type
  TPoint = record
    X, Y: Integer;
  end;

function PointToOrd(const P: TPoint): Integer;
begin
  Result := P.X * 1000 + P.Y;
end;

var
  pt: TPoint;
begin
  pt.X := 5;
  pt.Y := 3;
  WriteLn(PointToOrd(pt));  // 5003
end.
```

## Examples

A developer calls `Ord(myRealVariable)` expecting the integer part. Pascal rejects this because `Real` is not an ordinal type. Using `Round()` first converts the real to an integer, which is then an ordinal type that `Ord()` accepts.

## Related Errors

- [Subrange Type](/languages/pascal/pascal-subrange-type-error) — range restrictions
- [Enumerated Type](/languages/pascal/pascal-enumerated-type-error) — enum operations
- [Type Mismatch](/languages/pascal/pascal-type-mismatch) — type compatibility
