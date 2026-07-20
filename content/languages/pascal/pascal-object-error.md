---
title: "[Solution] Pascal Object Type Error — How to Fix"
description: "Fix object type errors in Pascal when using legacy Turbo Pascal-style objects incorrectly."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1066
---

# Object Type Error

The `object` type in Object Pascal is a legacy construct from Turbo Pascal. Unlike `class`, objects are value types (not reference-counted) and do not support polymorphism. Misusing them causes lifetime and assignment issues.

## Common Causes

- Assigning an object variable copies the value, not a reference
- Calling methods on a nil/uninitialized object variable
- Using `object` instead of `class` when polymorphism is needed
- Not initializing the VMT pointer in manually allocated objects

## How to Fix

### Solution 1 — Use object as value type correctly

```pascal
program ObjectFix;

type
  TPoint = object
    X, Y: Integer;
    procedure Init(AX, AY: Integer);
    function Distance: Double;
  end;

procedure TPoint.Init(AX, AY: Integer);
begin
  X := AX;
  Y := AY;
end;

function TPoint.Distance: Double;
begin
  Result := Sqrt(X * X + Y * Y);
end;

var
  P1, P2: TPoint;
begin
  P1.Init(3, 4);
  P2 := P1;               // value copy
  P2.X := 10;
  WriteLn(P1.X, ' ', P2.X);  // 3  10
end.
```

### Solution 2 — Use class for reference semantics

```pascal
program UseClassInstead;

type
  TPoint = class
    X, Y: Integer;
    constructor Create(AX, AY: Integer);
  end;

constructor TPoint.Create(AX, AY: Integer);
begin
  X := AX;
  Y := AY;
end;

var
  P1, P2: TPoint;
begin
  P1 := TPoint.Create(3, 4);
  P2 := P1;               // reference copy
  P2.X := 10;
  WriteLn(P1.X);          // 10 — same object
  P1.Free;
end.
```

### Solution 3 — Initialize objects before use

```pascal
program InitObject;

type
  TCounter = object
    Count: Integer;
    procedure Incr;
    function GetCount: Integer;
  end;

procedure TCounter.Incr;
begin
  Inc(Count);
end;

function TCounter.GetCount: Integer;
begin
  Result := Count;
end;

var
  C: TCounter;
begin
  FillChar(C, SizeOf(C), 0);  // zero-initialize
  C.Incr;
  WriteLn(C.GetCount);
end.
```

### Solution 4 — Use pointer to object for dynamic allocation

```pascal
program ObjectPointer;

type
  PPoint = ^TPoint;
  TPoint = object
    X, Y: Integer;
  end;

var
  P: PPoint;
begin
  New(P);
  P^.X := 10;
  P^.Y := 20;
  WriteLn(P^.X, ' ', P^.Y);
  Dispose(P);
end.
```

## Examples

A developer uses `object` expecting reference semantics. Two variables are assigned the same object. Modifying one does not affect the other because objects are value types. Switching to `class` gives the expected reference behavior.

## Related Errors

- [Constructor Error](/languages/pascal/pascal-constructor-error) — initialization
- [Destructor Error](/languages/pascal/pascal-destructor-error) — cleanup
- [Memory Leak](/languages/pascal/pascal-memory-leak-error) — allocation
