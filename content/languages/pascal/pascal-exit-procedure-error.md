---
title: "[Solution] Pascal EXIT Procedure Error"
description: "Fix Pascal EXIT procedure errors when prematurely leaving procedures or functions."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

EXIT procedure errors occur when EXIT is used incorrectly, returning wrong values, or when cleanup code is skipped.

## Common Causes

- EXIT without setting function result
- EXIT in nested loops exits procedure entirely
- Resource leak from EXIT skipping cleanup
- EXIT in initialization section

## How to Fix

### 1. Set function result before EXIT

```pascal
function FindValue: Integer;
begin
  Result := -1;  // default
  if condition then
  begin
    Result := 42;
    Exit;
  end;
end;
```

### 2. Use Exit for early returns

```pascal
procedure Process;
begin
  if not Valid then
    Exit;  // early return
  DoWork;
end;
```

## Examples

```pascal
program ExitDemo;

function Divide(A, B: Integer): Integer;
begin
  if B = 0 then
  begin
    WriteLn('Cannot divide by zero');
    Result := 0;
    Exit;
  end;
  Result := A div B;
end;

begin
  WriteLn(Divide(10, 2));
  WriteLn(Divide(10, 0));
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Try finally error](/languages/pascal/pascal-try-finally-error)
- [Memory leak error](/languages/pascal/pascal-memory-leak-error)
