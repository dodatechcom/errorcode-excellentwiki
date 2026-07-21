---
title: "[Solution] Pascal CONSOLECTRLBREAK Error"
description: "Fix Pascal Ctrl+Break handling errors when programs do not properly handle interrupt signals."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

Ctrl+Break handling errors occur when programs crash or behave unexpectedly due to improper signal handling.

## Common Causes

- No Ctrl+Break handler installed
- Ctrl+Break during critical section
- Break key handler conflicts with debugger
- Missing CheckCtrlBreak in loops

## How to Fix

### 1. Install break handler

```pascal
var
  BreakPressed: Boolean;

procedure CheckBreak;
begin
  if KeyPressed then
  begin
    if ReadKey = #3 then
    begin
      BreakPressed := True;
      WriteLn('Break pressed');
    end;
  end;
end;
```

### 2. Check for break in loops

```pascal
while not Done and not BreakPressed do
begin
  ProcessData;
  CheckBreak;
end;
```

## Examples

```pascal
program BreakDemo;

var
  I: Integer;

begin
  for I := 1 to 1000000 do
  begin
    if I mod 100000 = 0 then
      WriteLn('Processed: ', I);
  end;
  WriteLn('Done');
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Signal error](/languages/pascal/pascal-signal-error)
- [Exception error](/languages/pascal/pascal-exception-error)
