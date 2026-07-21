---
title: "[Solution] Pascal SETTIME Procedure Error"
description: "Fix Pascal SETTIME procedure errors when attempting to set the system time."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

SETTIME procedure errors occur when setting invalid time values or when the program lacks permission to change system time.

## Common Causes

- Invalid time values (hour > 23, etc.)
- Permission denied to change system time
- SETTIME in restricted environment
- Time value out of valid range

## How to Fix

### 1. Validate before setting

```pascal
var
  H, M, S: Word;
begin
  H := 14;  // 2 PM
  M := 30;
  S := 0;
  if (H <= 23) and (M <= 59) and (S <= 59) then
    SetTime(H, M, S, 0);
end;
```

### 2. Check return value

```pascal
// On some systems SetTime returns error code
SetTime(H, M, S, 0);
if IOResult <> 0 then
  WriteLn('Cannot set time');
```

## Examples

```pascal
program SetTimeDemo;

begin
  WriteLn('Attempting to set time...');
  // SetTime requires admin privileges
  // SetTime(14, 30, 0, 0);
  WriteLn('Time set demo complete');
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Permission denied](/languages/pascal/pascal-file-locking-error)
- [GetTime error](/languages/pascal/pascal-gettime-error)
