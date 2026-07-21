---
title: "[Solution] Pascal WITH Statement Error"
description: "Fix Pascal WITH statement errors when using with for record field access including variable capture issues."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

WITH statement errors occur when the WITH block creates ambiguous variable references or when nested WITH statements shadow variables.

## Common Causes

- WITH captures local variable unexpectedly
- Nested WITH creates ambiguous field access
- Field name shadows variable name in WITH
- WITH on nil pointer causes crash

## How to Fix

### 1. Avoid variable shadowing in WITH

```pascal
// WRONG: Shadowing
var Name: string;
begin
  with PersonRec do
    Name := PersonName;  // ambiguous: Name or PersonName?
end;

// CORRECT: Avoid WITH
var Name: string;
begin
  Name := PersonRec.PersonName;
end;
```

### 2. Use explicit record access

```pascal
// Safer than WITH
Result := Customer.Name + ' - ' + IntToStr(Customer.Age);
```

## Examples

```pascal
program WithStatementDemo;

type
  TPoint = record
    X, Y: Integer;
  end;

var
  P: TPoint;
  X: Integer;

begin
  X := 10;
  with P do
  begin
    X := 5;  // WARNING: may refer to local X
    Y := 10;
  end;
  WriteLn('P.X = ', P.X);
end.
```

## Related Errors

- [Record error](/languages/pascal/pascal-object-error)
- [Undefined variable](/languages/pascal/pascal-undefined-variable)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
