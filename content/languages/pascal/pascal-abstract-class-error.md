---
title: "[Solution] Pascal Abstract Class Error — How to Fix"
description: "Fix abstract class errors in Pascal when trying to instantiate classes with abstract methods."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1070
---

# Abstract Class Error

An abstract class contains methods declared with `abstract` that must be overridden by derived classes. Attempting to instantiate an abstract class directly causes a runtime error.

## Common Causes

- Calling `Create` on a class with unoverridden abstract methods
- Forgetting to override all abstract methods in a derived class
- Declaring a method as `abstract` without `virtual`
- Using `reintroduce` on an abstract method instead of `override`

## How to Fix

### Solution 1 — Never instantiate abstract classes directly

```pascal
program AbstractFix;

type
  TBase = class
    procedure DoSomething; virtual; abstract;
  end;

  TDerived = class(TBase)
    procedure DoSomething; override;
  end;

procedure TDerived.DoSomething;
begin
  WriteLn('Derived implementation');
end;

var
  Obj: TBase;
begin
  // WRONG: Obj := TBase.Create;  // runtime error
  Obj := TDerived.Create;         // correct
  Obj.DoSomething;
  Obj.Free;
end.
```

### Solution 2 — Use class reference for factory

```pascal
program FactoryPattern;

type
  TBase = class
    procedure Process; virtual; abstract;
  end;

  TImplA = class(TBase)
    procedure Process; override;
  end;

  TImplB = class(TBase)
    procedure Process; override;
  end;

procedure TImplA.Process;
begin
  WriteLn('A');
end;

procedure TImplB.Process;
begin
  WriteLn('B');
end;

function Create(Kind: TClass): TBase;
begin
  Result := TBase(Kind.Create);
end;

begin
  Create(TImplA).Process;
  Create(TImplB).Process;
end.
```

### Solution 3 — Check for abstract methods at runtime

```pascal
program CheckAbstract;

uses TypInfo;

function IsAbstract(Obj: TObject; const MethodName: string): Boolean;
var
  MT: TMethodTableEntry;
  PMTI: PMethodInfo;
  I: Integer;
begin
  Result := False;
  PMTI := PMethodInfo(GetMethodTable(Obj));
  // Simplified check — use RTTI for proper implementation
end;
```

### Solution 4 — Provide default implementation

```pascal
program DefaultImpl;

type
  TBase = class
    procedure Log(const Msg: string); virtual;
  end;

  TDerived = class(TBase)
    procedure Log(const Msg: string); override;
  end;

procedure TBase.Log(const Msg: string);
begin
  WriteLn('Default: ', Msg);
end;

procedure TDerived.Log(const Msg: string);
begin
  WriteLn('Custom: ', Msg);
end;
```

## Examples

A plugin system defines `TPlugin` with an abstract `Execute` method. Code accidentally calls `TPlugin.Create` instead of `TMyPlugin.Create`. Runtime error 210 occurs. The fix is to only instantiate concrete subclasses.

## Related Errors

- [Virtual Method Error](/languages/pascal/pascal-virtual-method-error) — dispatch issues
- [Method Overriding Error](/languages/pascal/pascal-method-overriding-error) — override mismatch
- [Constructor Error](/languages/pascal/pascal-constructor-error) — initialization
