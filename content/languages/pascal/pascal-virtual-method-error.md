---
title: "[Solution] Pascal Virtual Method Error — How to Fix"
description: "Fix virtual method errors in Pascal when dynamic dispatch fails due to incorrect method declarations."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1069
---

# Virtual Method Error

Virtual methods enable runtime polymorphism. Errors occur when a method is not declared `virtual` in the base class, when `override` is used without `virtual`, or when calling a method on a nil object reference.

## Common Causes

- Base class method not declared `virtual` — no dynamic dispatch
- Derived class uses `reintroduce` instead of `override`, hiding the base method
- Calling virtual method through a nil object reference
- Mismatched method signatures between base and derived

## How to Fix

### Solution 1 — Declare methods as virtual in base class

```pascal
program VirtualFix;

type
  TAnimal = class
    procedure Speak; virtual;
  end;

  TDog = class(TAnimal)
    procedure Speak; override;
  end;

procedure TAnimal.Speak;
begin
  WriteLn('...');
end;

procedure TDog.Speak;
begin
  WriteLn('Woof!');
end;

var
  A: TAnimal;
begin
  A := TDog.Create;
  A.Speak;              // calls TDog.Speak (virtual dispatch)
  A.Free;
end.
```

### Solution 2 — Use abstract methods

```pascal
program AbstractMethod;

type
  TShape = class
    function Area: Double; virtual; abstract;
  end;

  TCircle = class(TShape)
    Radius: Double;
    function Area: Double; override;
  end;

function TCircle.Area: Double;
begin
  Result := Pi * Radius * Radius;
end;
```

### Solution 3 — Check for nil before virtual calls

```pascal
program NilCheck;

var
  A: TAnimal;
begin
  A := nil;
  if A <> nil then
    A.Speak
  else
    WriteLn('No animal');
end.
```

### Solution 4 — Use classOf for factory pattern

```pascal
program Factory;

type
  TAnimal = class
    procedure Speak; virtual;
  end;

  TDog = class(TAnimal)
    procedure Speak; override;
  end;

function CreateAnimal(Kind: TClass): TAnimal;
begin
  Result := TAnimal(Kind.Create);
end;

var
  A: TAnimal;
begin
  A := CreateAnimal(TDog);
  A.Speak;
  A.Free;
end.
```

## Examples

A base class has `procedure Draw;` without `virtual`. A derived class adds `procedure Draw; override;`. The compiler generates a hidden method instead of overriding, and the base class pointer always calls the base version. Adding `virtual` to the base method fixes the dispatch.

## Related Errors

- [Abstract Class Error](/languages/pascal/pascal-abstract-class-error) — abstract methods
- [Method Overriding Error](/languages/pascal/pascal-method-overriding-error) — override issues
- [Invalid Pointer](/languages/pascal/pascal-invalid-pointer) — nil object access
