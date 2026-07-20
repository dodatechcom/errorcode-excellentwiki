---
title: "[Solution] Pascal Subrange Type Error — How to Fix"
description: "Fix subrange type errors in Pascal when values exceed the declared subrange boundaries."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1042
---

# Subrange Type Error

A subrange type restricts values to a specific range within an ordinal type. Assigning a value outside the subrange causes a compile-time or range-check runtime error.

## Common Causes

- Assigning a value outside `1..10` to a variable of that subrange
- Using `Inc()` that pushes value past the upper bound
- Passing an out-of-range value to a subrange parameter
- Range checking disabled at compile time hiding the error

## How to Fix

### Solution 1 — Validate before assignment

```pascal
program SubrangeFix;

type
  TPercentage = 0..100;

var
  p: TPercentage;
  raw: Integer;
begin
  raw := 150;
  if (raw >= 0) and (raw <= 100) then
    p := TPercentage(raw)
  else
    WriteLn('Value out of range: ', raw);
end.
```

### Solution 2 — Enable range checking

```bash
# Free Pascal: enable range checking
fpc -Cr program.pas
```

```pascal
program RangeCheckDemo;

{$R+}  // enable range checking

type
  TDay = 1..7;
var
  d: TDay;
begin
  d := 8;  // runtime error 201 if range check enabled
end.
```

### Solution 3 — Use Clamp function

```pascal
function Clamp(V, Lo, Hi: Integer): Integer;
begin
  if V < Lo then Result := Lo
  else if V > Hi then Result := Hi
  else Result := V;
end;

var
  p: 0..100;
begin
  p := Clamp(150, 0, 100);  // safely clamped to 100
end.
```

### Solution 4 — Use try/except for runtime checks

```pascal
program SafeSubrange;

type
  TScore = 0..1000;

var
  s: TScore;
begin
  try
    s := StrToInt(InputBox('Score', 'Enter score:', ''));
  except
    on E: Exception do
      s := 0;
  end;
end.
```

## Examples

A `TMonth` variable is declared as `1..12`. User input of `13` triggers a range check error. The fix is to validate input before assignment or use a clamping function.

## Related Errors

- [Ordinal Type](/languages/pascal/pascal-ordinal-type-error) — ordinal restrictions
- [Enumerated Type](/languages/pascal/pascal-enumerated-type-error) — enum values
- [Type Mismatch](/languages/pascal/pascal-type-mismatch) — type compatibility
