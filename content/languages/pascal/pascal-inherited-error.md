---
title: "[Solution] Pascal INHERITED Error"
description: "Fix Pascal INHERITED errors when calling parent class methods in Object Pascal."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

INHERITED errors occur when calling parent class methods that do not exist or when using INHERITED incorrectly in constructors.

## Common Causes

- INHERITED on method not defined in parent
- INHERITED in constructor without proper initialization
- Missing INHERITED in virtual method override
- INHERITED with wrong parameter types

## How to Fix

### 1. Ensure parent has the method

```pascal
// WRONG: Parent does not have Method
inherited Method(Args);

// CORRECT: Call inherited version
inherited;  // calls parent's version of current method
```

### 2. Use INHERITED in constructors

```pascal
constructor TChild.Create;
begin
  inherited Create;  // initialize parent
  // initialize child
end;
```

## Examples

```pascal
program InheritedDemo;

type
  TAnimal = class
  public
    function Speak: string; virtual;
  end;

  TDog = class(TAnimal)
  public
    function Speak: string; override;
  end;

function TAnimal.Speak: string;
begin
  Result := '...';
end;

function TDog.Speak: string;
begin
  Result := inherited Speak + ' Woof!';
end;

begin
  WriteLn(TDog.Create.Speak);
end.
```

## Related Errors

- [Virtual method error](/languages/pascal/pascal-virtual-method-error)
- [Constructor error](/languages/pascal/pascal-constructor-error)
- [Runtime error](/languages/pascal/pascal-runtime-error)
