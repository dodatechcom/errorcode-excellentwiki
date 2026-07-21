---
title: "[Solution] Pascal SLEEP Procedure Error"
description: "Fix Pascal SLEEP procedure errors when pausing program execution for specified milliseconds."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

SLEEP procedure errors occur when SLEEP is called with negative values or when the underlying system call fails.

## Common Causes

- Negative sleep duration
- SLEEP on non-interactive systems
- System timer resolution too coarse
- SLEEP in critical section blocking other threads

## How to Fix

### 1. Validate sleep duration

```pascal
var
  Duration: Cardinal;
begin
  Duration := 1000;  // 1 second
  if Duration > 0 then
    Sleep(Duration);
end;
```

### 2. Use for timing purposes

```pascal
// Poll with sleep
while not Done do
begin
  CheckStatus;
  Sleep(100);  // avoid busy-wait
end;
```

## Examples

```pascal
program SleepDemo;

var
  i: Integer;

begin
  for i := 1 to 5 do
  begin
    WriteLn('Tick ', i);
    Sleep(1000);
  end;
  WriteLn('Done');
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Compile error](/languages/pascal/pascal-compiler-error-new)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
