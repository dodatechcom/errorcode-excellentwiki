---
title: "[Solution] Pascal GETTIME Procedure Error"
description: "Fix Pascal GETTIME procedure errors when retrieving the current system time."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

GETTIME procedure errors occur when retrieving system time values that are out of expected ranges.

## Common Causes

- Hour value outside 0..23
- Minute value outside 0..59
- Second value outside 0..59
- GETTIME on unsupported platform

## How to Fix

### 1. Validate time components

```pascal
var
  H, M, S, MS: Word;
begin
  GetTime(H, M, S, MS);
  if (H <= 23) and (M <= 59) and (S <= 59) then
    WriteLn(H:2, ':', M:2, ':', S:2);
end;
```

### 2. Use DateTimeUtils for better handling

```pascal
var
  Now: TDateTime;
begin
  Now := Now;
  WriteLn('Time: ', FormatDateTime('hh:nn:ss', Now));
end;
```

## Examples

```pascal
program GetTimeDemo;

var
  Hour, Min, Sec, MS: Word;

begin
  GetTime(Hour, Min, Sec, MS);
  WriteLn('Current time: ', Hour:2, ':', Min:2, ':', Sec:2);
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Compile error](/languages/pascal/pascal-compiler-error-new)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
