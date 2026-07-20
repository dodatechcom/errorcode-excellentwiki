---
title: "[Solution] Pascal Property Read/Write Error — How to Fix"
description: "Fix property accessor errors in Pascal when read/write methods or field accessors are incorrectly declared."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1071
---

# Property Read/Write Error

Properties encapsulate field access through getter/setter methods. Errors occur when the read/write methods have mismatched types, when the property type does not match the field, or when write access is missing.

## Common Causes

- Property type does not match the getter method return type
- Write method parameter type mismatch with property type
- Missing `write` specifier making property read-only by accident
- Circular reference in read/write methods (property calls itself)

## How to Fix

### Solution 1 — Match types between property and accessors

```pascal
program PropertyFix;

type
  TPerson = class
  private
    FAge: Integer;
    function GetAge: Integer;
    procedure SetAge(const Value: Integer);
  published
    property Age: Integer read GetAge write SetAge;
  end;

function TPerson.GetAge: Integer;
begin
  Result := FAge;
end;

procedure TPerson.SetAge(const Value: Integer);
begin
  if Value >= 0 then
    FAge := Value;
end;
```

### Solution 2 — Use direct field access for simple properties

```pascal
program DirectField;

type
  TRect = class
  public
    Left, Top, Width, Height: Integer;
    property Right: Integer read Left;  // WRONG: read Left
    property Bottom: Integer read Top;   // WRONG: read Top
  end;

type
  TRectFixed = class
  private
    FLeft, FTop, FWidth, FHeight: Integer;
  public
    property Right: Integer read (FLeft + FWidth);  // not valid syntax
  end;
```

### Solution 3 — Read-only and write-only properties

```pascal
program ReadOnlyProp;

type
  TCounter = class
  private
    FCount: Integer;
  public
    property Count: Integer read FCount;
    // no write specifier — read-only
  end;

procedure Increment(var C: TCounter);
begin
  Inc(C.FCount);  // must access private field directly or use method
end;
```

### Solution 4 — Indexed properties

```pascal
program IndexedProp;

type
  TStringArray = class
  private
    FItems: array[0..99] of string;
  public
    property Items[Index: Integer]: string read FItems write FItems;
  end;

var
  Arr: TStringArray;
begin
  Arr := TStringArray.Create;
  Arr.Items[0] := 'Hello';
  WriteLn(Arr.Items[0]);
  Arr.Free;
end.
```

## Examples

A property `Name: string` has a getter that returns an `AnsiString` but the property is typed as `string` (which may be `UnicodeString` in Delphi). The implicit conversion may cause data loss for non-ASCII characters. Aligning the types fixes the issue.

## Related Errors

- [Published Error](/languages/pascal/pascal-published-error) — RTTI visibility
- [Type Mismatch](/languages/pascal/pascal-type-mismatch) — type compatibility
- [Method Overriding Error](/languages/pascal/pascal-method-overriding-error) — method issues
