---
title: "[Solution] Pascal GETDATE Procedure Error"
description: "Fix Pascal GETDATE procedure errors when retrieving the current system date."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

GETDATE procedure errors occur when retrieving system date values with out-of-range month, day, or year values.

## Common Causes

- Month value outside 1..12
- Day value outside valid range for month
- Year value outside supported range
- GETDATE on system with incorrect date

## How to Fix

### 1. Validate date components

```pascal
var
  Year, Month, Day, DOW: Word;
begin
  GetDate(Year, Month, Day, DOW);
  if (Month >= 1) and (Month <= 12) and
     (Day >= 1) and (Day <= 31) then
    WriteLn(Year, '-', Month:2, '-', Day:2);
end;
```

### 2. Use TDateTime for modern code

```pascal
var
  Today: TDateTime;
begin
  Today := Date;
  WriteLn('Today: ', DateToStr(Today));
end;
```

## Examples

```pascal
program GetDateDemo;

var
  Year, Month, Day, DOW: Word;

begin
  GetDate(Year, Month, Day, DOW);
  WriteLn('Date: ', Year, '-', Month:2, '-', Day:2);
  WriteLn('Day of week: ', DOW);
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Compile error](/languages/pascal/pascal-compiler-error-new)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
