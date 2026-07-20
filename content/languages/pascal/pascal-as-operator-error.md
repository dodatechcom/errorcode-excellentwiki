---
title: "[Solution] Pascal As Operator Error — How to Fix"
description: "Fix as operator errors in Pascal when forced type casting raises an invalid cast exception."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1075
---

# As Operator Error

The `as` operator performs a runtime-checked type cast. If the object is not of the target type (or a descendant), an `EInvalidCast` exception is raised. Misuse causes crashes in production code.

## Common Causes

- Casting to a type the object does not belong to
- Using `as` when `is` check should be used first
- Casting nil object reference with `as`
- Overusing `as` instead of proper polymorphic design

## How to Fix

### Solution 1 — Check with is before using as

```pascal
program IsBeforeAs;

type
  TBase = class end;
  TDerived = class(TBase)
    procedure Special;
  end;

procedure TDerived.Special;
begin
  WriteLn('Special method');
end;

procedure Process(Obj: TBase);
begin
  if Obj is TDerived then
    TDerived(Obj).Special;   // safe cast
end;
```

### Solution 2 — Use try/except for uncertain casts

```pascal
program SafeAs;

type
  TAnimal = class end;
  TDog = class(TAnimal) end;

procedure TryCast(A: TAnimal);
begin
  try
    TDog(A).Bark;
  except
    on E: EInvalidCast do
      WriteLn('Not a dog');
  end;
end;
```

### Solution 3 — Use as for interface queries

```pascal
program AsInterface;

type
  IComparable = interface
    function CompareTo(Other: TObject): Integer;
  end;

  TPerson = class(TInterfacedObject, IComparable)
    Name: string;
    function CompareTo(Other: TObject): Integer;
  end;

function TPerson.CompareTo(Other: TObject): Integer;
begin
  Result := CompareStr(Name, (Other as TPerson).Name);
end;
```

### Solution 4 — Prefer virtual methods over as casts

```pascal
program PreferVirtual;

type
  TShape = class
    function Area: Double; virtual;
  end;

  TCircle = class(TShape)
    Radius: Double;
    function Area: Double; override;
  end;

function TShape.Area: Double;
begin
  Result := 0;
end;

function TCircle.Area: Double;
begin
  Result := Pi * Radius * Radius;
end;

procedure PrintArea(S: TShape);
begin
  WriteLn('Area: ', S.Area:0:2);  // no cast needed
end;
```

## Examples

A list stores `TObject` items. Code does `TStringList(Items[i])` without checking. When a non-string-list item is encountered, EInvalidCast is raised. Adding `if Items[i] is TStringList` before the cast prevents the exception.

## Related Errors

- [Is Operator Error](/languages/pascal/pascal-is-operator-error) — type checking
- [Invalid Pointer](/languages/pascal/pascal-invalid-pointer) — nil dereference
- [Type Mismatch](/languages/pascal/pascal-type-mismatch) — type compatibility
