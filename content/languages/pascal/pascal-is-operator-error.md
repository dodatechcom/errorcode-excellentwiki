---
title: "[Solution] Pascal Is Operator Error — How to Fix"
description: "Fix is operator errors in Pascal when runtime type checking fails due to incorrect type hierarchy."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1074
---

# Is Operator Error

The `is` operator checks whether an object belongs to a class or any of its ancestors. Errors occur when using `is` on nil objects, when the type hierarchy is not correctly established, or when `is` is used with non-class types.

## Common Causes

- Assuming `is` checks for exact type rather than ancestry
- Using `is` on a nil reference (returns False, not an exception)
- Forgetting that descendants also pass the check
- Using `is` with interface types that lack RTTI

## How to Fix

### Solution 1 — Use is for safe type checking

```pascal
program IsFix;

type
  TAnimal = class end;
  TDog = class(TAnimal) end;
  TCat = class(TAnimal) end;

procedure Identify(A: TAnimal);
begin
  if A is TDog then
    WriteLn('It is a dog')
  else if A is TCat then
    WriteLn('It is a cat')
  else
    WriteLn('Unknown animal');
end;

var
  A: TAnimal;
begin
  A := TDog.Create;
  Identify(A);
  A.Free;
end.
```

### Solution 2 — Use is before as

```pascal
program IsThenAs;

type
  TBase = class
    procedure BaseMethod; virtual;
  end;

  TDerived = class(TBase)
    procedure DerivedMethod;
  end;

procedure TBase.BaseMethod;
begin
  WriteLn('Base');
end;

procedure TDerived.DerivedMethod;
begin
  WriteLn('Derived specific');
end;

procedure Process(Obj: TBase);
begin
  if Obj is TDerived then
    TDerived(Obj).DerivedMethod;
end;
```

### Solution 3 — Check exact type with ClassType

```pascal
program ExactTypeCheck;

type
  TBase = class end;
  TDerived = class(TBase) end;

var
  Obj: TBase;
begin
  Obj := TDerived.Create;
  if Obj.ClassType = TDerived then
    WriteLn('Exact type is TDerived');
  Obj.Free;
end.
```

### Solution 4 — Use is for nil-safe patterns

```pascal
program NilSafe;

type
  TWidget = class
    procedure Paint; virtual;
  end;

procedure PaintIfValid(W: TWidget);
begin
  if (W <> nil) and (W is TWidget) then
    W.Paint;
end;
```

## Examples

A VCL application checks `if Sender is TButton`. This returns True for TSpeedButton too (if it descends from TButton). Using `Sender.ClassType = TButton` for exact match when subclass handling is not desired.

## Related Errors

- [As Operator Error](/languages/pascal/pascal-as-operator-error) — type casting
- [Class Reference Error](/languages/pascal/pascal-class-reference-error) — metaclass
- [Virtual Method Error](/languages/pascal/pascal-virtual-method-error) — dispatch
