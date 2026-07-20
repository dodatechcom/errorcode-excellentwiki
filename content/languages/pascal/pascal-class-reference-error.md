---
title: "[Solution] Pascal Class Reference Error — How to Fix"
description: "Fix class reference (metaclass) errors in Pascal when using TClass variables for factory patterns."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1073
---

# Class Reference (Metaclass) Error

A class reference (`class of T`) stores a class type at runtime. Errors occur when using the class reference to call methods not declared in the base, when assigning an incompatible class, or when creating instances without proper type casting.

## Common Causes

- Using class reference to call a method only in the derived class
- Assigning a class reference to an incompatible `class of` type
- Not casting the result of `TClass.Create` back to the correct type
- Passing nil class reference to a factory function

## How to Fix

### Solution 1 — Use class reference for factory creation

```pascal
program FactoryFix;

type
  TBase = class
    procedure Greet; virtual;
  end;

  TDerived = class(TBase)
    procedure Greet; override;
  end;

procedure TBase.Greet;
begin
  WriteLn('Hello from Base');
end;

procedure TDerived.Greet;
begin
  WriteLn('Hello from Derived');
end;

function CreateInstance(AClass: TClass): TBase;
begin
  Result := TBase(AClass.Create);
end;

var
  Obj: TBase;
begin
  Obj := CreateInstance(TDerived);
  Obj.Greet;
  Obj.Free;
end.
```

### Solution 2 — Validate class reference before creation

```pascal
program SafeFactory;

function CreateSafe(AClass: TClass): TObject;
begin
  if AClass = nil then
    raise Exception.Create('Nil class reference');
  Result := AClass.Create;
end;
```

### Solution 3 — Use Is operator with class references

```pascal
program ClassCheck;

type
  TAnimal = class end;
  TDog = class(TAnimal) end;
  TCat = class(TAnimal) end;

procedure Identify(AClass: TClass);
begin
  if AClass = TDog then
    WriteLn('Dog')
  else if AClass = TCat then
    WriteLn('Cat')
  else
    WriteLn('Unknown');
end;

begin
  Identify(TDog);
  Identify(TCat);
end.
```

### Solution 4 — Store class references in arrays

```pascal
program ClassArray;

type
  TAnimal = class of TAnimalBase;
  TAnimalBase = class
    class function Name: string; virtual;
  end;

  TDog = class(TAnimalBase)
    class function Name: string; override;
  end;

var
  Classes: array[0..1] of TAnimal;
begin
  Classes[0] := TAnimalBase;
  Classes[1] := TDog;
end.
```

## Examples

A plugin loader reads a class name from a config file and uses `FindClass` to get the TClass reference. If the class name is misspelled, `FindClass` raises an exception. Wrapping the call in `try/except` handles the error gracefully.

## Related Errors

- [Is Operator Error](/languages/pascal/pascal-is-operator-error) — type checking
- [As Operator Error](/languages/pascal/pascal-as-operator-error) — type casting
- [Constructor Error](/languages/pascal/pascal-constructor-error) — initialization
