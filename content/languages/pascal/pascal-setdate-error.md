---
title: "[Solution] Pascal SETDATE Procedure Error"
description: "Fix Pascal SETDATE procedure errors when attempting to set the system date."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

SETDATE procedure errors occur when setting invalid date values or when the program lacks permission to change system date.

## Common Causes

- Invalid date values (month 0 or 13)
- Day value exceeds days in month
- Permission denied to change date
- Leap year validation missing

## How to Fix

### 1. Validate date before setting

```pascal
var
  Year, Month, Day: Word;
begin
  Year := 2026;
  Month := 7;
  Day := 21;
  if (Month >= 1) and (Month <= 12) and
     (Day >= 1) and (Day <= 31) then
    SetDate(Year, Month, Day);
end;
```

### 2. Check leap year for February

```pascal
function IsLeapYear(Year: Word): Boolean;
begin
  IsLeapYear := (Year mod 4 = 0) and
    ((Year mod 100 <> 0) or (Year mod 400 = 0));
end;
```

## Examples

```pascal
program SetDateDemo;

begin
  WriteLn('Date set demo');
  // SetDate(2026, 7, 21);  // requires privileges
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Permission denied](/languages/pascal/pascal-file-locking-error)
- [GetDate error](/languages/pascal/pascal-getdate-error)
