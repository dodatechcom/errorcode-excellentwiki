---
title: "[Solution] Pascal: type mismatch error"
description: "Fix Pascal compile-time and runtime errors when types don't match in assignments, comparisons, or function calls."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Pascal type mismatch errors occur when assigning a value of one type to a variable of an incompatible type, or when comparing incompatible types.

## Common Causes

- Assigning string to integer
- Comparing incompatible types
- Wrong parameter type in function call
- Implicit conversion failure
- Variant type mismatch

## How to Fix

```pascal
program TypeMismatch;
var
  x: Integer;
begin
  x := 'Hello';  // Error: string to integer
end.
```

```pascal
program SafeConversion;
var
  x: Integer;
  s: string;
begin
  s := '42';
  x := StrToInt(s);  // Explicit conversion
  WriteLn(x);
end.
```

```pascal
program TypeChecking;
var
  a: Integer;
  b: Real;
begin
  a := 10;
  b := 3.14;
  
  // Don't mix types in comparisons
  if a = Round(b) then
    WriteLn('Equal');
end.
```

```pascal
program SafeAssignment;
var
  v: Variant;
  i: Integer;
begin
  v := 42;
  
  if VarIsNumeric(v) then
  begin
    i := v;  // Safe conversion
    WriteLn(i);
  end;
end.
```

```pascal
program FunctionParams;
function Add(a, b: Integer): Integer;
begin
  Add := a + b;
end;

var
  x: Integer;
begin
  x := Add(10, 20);  // Correct types
  WriteLn(x);
end.
```

## Related Errors

- [Runtime Error](pascal-runtime-error-v2) - general runtime
- [Index Out of Range](pascal-index-out-of-range-v2) - bounds errors
- [Exception Error](pascal-exception-error-v2) - exception handling
