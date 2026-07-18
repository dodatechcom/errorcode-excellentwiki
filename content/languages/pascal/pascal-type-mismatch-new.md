---
title: "[Solution] Pascal: type mismatch compile or runtime error"
description: "Fix Pascal type mismatches by using compatible types and explicit type conversion functions."
languages: ["pascal"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Pascal type mismatch error occurs when the compiler or runtime system detects an incompatibility between expected and actual types. At compile time, this appears when assigning values between incompatible types, passing arguments to procedures with wrong parameter types, or using operators on incompatible operands. At runtime, type mismatches may occur when reading untyped files into variables, interpreting binary data incorrectly, or when variant records are accessed with the wrong active field. Pascal is strongly typed, meaning implicit type conversions are limited.

## Why It Happens

Type mismatches arise from several situations. Assigning a `Real` value to an `Integer` variable without explicit conversion is a common compile-time error. Passing a `String` to a parameter expecting `Char`, or vice versa, causes type incompatibility. Using the wrong record field type in a procedure call, or passing an `Integer` when a `LongInt` is expected on 16-bit compilers, triggers this error. Variant record misuse, where you access a field of the wrong active variant, causes a runtime type mismatch. Reading from an untyped file (`file`) into a variable of the wrong size produces data corruption. Comparing values of different enumerated types, or using values from different subrange types, also causes type errors.

## How to Fix It

**Use explicit type conversions:**

```pascal
program TypeConversion;
var
  intVal: Integer;
  realVal: Real;
  strVal: string;
  charVal: Char;
begin
  realVal := 3.14;
  intVal := Round(realVal);  { Explicit conversion }
  WriteLn('Integer: ', intVal);

  strVal := 'A';
  charVal := strVal[1];  { String to Char }
  WriteLn('Char: ', charVal);
end.
```

**Match parameter types in procedure calls:**

```pascal
procedure PrintValue(val: Integer);
begin
  WriteLn('Value: ', val);
end;

program ParameterTypes;
var
  x: Integer;
  y: LongInt;
begin
  x := 42;
  PrintValue(x);      { Correct: Integer matches Integer }

  y := 100000;
  { WRONG: PrintValue(y); }  { LongInt does not match Integer }
  WriteLn(y);  { Use writeln directly for LongInt }
end.
```

**Use correct file type matching:**

```pascal
program FileTypeMismatch;
type
  TRecord = record
    id: Integer;
    name: string[20];
  end;

var
  f: file of TRecord;
  rec: TRecord;
begin
  Assign(f, 'data.dat');
  Rewrite(f);

  rec.id := 1;
  rec.name := 'Test';

  Write(f, rec);  { Correct: types match }
  Close(f);
end.
```

**Handle variant record access correctly:**

```pascal
program VariantRecord;
type
  TVariant = record
    case isReal: Boolean of
      True:  (r: Real);
      False: (i: Integer);
  end;

var
  v: TVariant;
begin
  v.isReal := True;
  v.r := 3.14;

  if v.isReal then
    WriteLn('Real: ', v.r:0:2)
  else
    WriteLn('Integer: ', v.i);
end.
```

**Use strict type checking:**

```pascal
{ Free Pascal: enable strict type checking }
{$mode delphi}
{$H-}  { Short strings for strict Char handling }

program StrictTypes;
var
  a: Integer;
  b: Integer;
begin
  a := 10;
  b := 20;
  WriteLn('Sum: ', a + b);
end.
```

## Common Mistakes

- Assuming Pascal will implicitly convert between Integer and Real
- Passing a String where a Char is expected without using string indexing
- Using the wrong field name in a variant record access
- Not converting between string types (AnsiString vs ShortString) when mixing procedures
- Forgetting that `Byte` and `Integer` are different types even though they both hold numbers

## Related Pages

- [Range check error in Pascal](/languages/pascal/pascal-index-error-new)
- [Arithmetic overflow in Pascal](/languages/pascal/pascal-overflow-error-v2)
- [Invalid pointer operation in Pascal](/languages/pascal/pascal-invalid-pointer-v2)
- [Runtime error in Pascal](/languages/pascal/pascal-runtime-error-v2)
