---
title: "[Solution] Pascal Published Section Error — How to Fix"
description: "Fix published section errors in Pascal when RTTI visibility is incorrectly configured."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1072
---

# Published Section Error

The `published` section in a class exposes properties and methods to RTTI (Run-Time Type Information). Errors occur when published properties use unsupported types, when RTTI is not enabled, or when the VMT is missing.

## Common Causes

- Published properties must have simple types (ordinals, strings, classes, interfaces)
- Records and variants cannot be published
- `{$M+}` directive not enabled for a class that needs RTTI
- Published methods must use `__cdecl` or `__register` calling convention

## How to Fix

### Solution 1 — Use valid published types

```pascal
program PublishedFix;

{$M+}  // enable RTTI generation

type
  TMyComponent = class
  private
    FName: string;
    FEnabled: Boolean;
    FCount: Integer;
  published
    property Name: string read FName write FName;
    property Enabled: Boolean read FEnabled write FEnabled;
    property Count: Integer read FCount write FCount;
  end;
```

### Solution 2 — Avoid unsupported published types

```pascal
program NoRecordPublished;

{$M+}

type
  TBad = class
  private
    FRect: TPoint;   // record — cannot be published!
  published
    // property Rect: TPoint read FRect write FRect;  // ERROR
  end;

type
  TGood = class
  private
    FLeft: Integer;
    FTop: Integer;
  published
    property Left: Integer read FLeft write FLeft;  // OK
    property Top: Integer read FTop write FTop;      // OK
  end;
```

### Solution 3 — Use published methods with correct calling convention

```pascal
program PublishedMethods;

{$M+}

type
  THandler = class
  public
    procedure OnClick(Sender: TObject);  // public, not published
  published
    procedure OnChange;  // published for event binding
  end;

procedure THandler.OnChange;
begin
  WriteLn('Changed');
end;
```

### Solution 4 — Access RTTI at runtime

```pascal
program RTTIAccess;

{$M+}

uses TypInfo;

type
  TWidget = class
  private
    FVisible: Boolean;
  published
    property Visible: Boolean read FVisible write FVisible;
  end;

var
  W: TWidget;
begin
  W := TWidget.Create;
  W.Visible := True;
  WriteLn('Visible: ', GetOrdProp(W, 'Visible'));
  W.Free;
end.
```

## Examples

A designer tool uses RTTI to enumerate published properties. A class with a `TPoint` field in the published section causes a compiler error. Moving the property to the public section and splitting it into `Left` and `Top` published integer properties fixes the issue.

## Related Errors

- [Property Error](/languages/pascal/pascal-property-error) — accessor issues
- [Class Reference Error](/languages/pascal/pascal-class-reference-error) — metaclass
- [RTTI Error](/languages/pascal/pascal-rtti-error) — RTTI access
