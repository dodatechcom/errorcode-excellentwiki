---
title: "[Solution] Pascal COPY Function Error"
description: "Fix Pascal COPY function errors when extracting substrings with incorrect start or length parameters."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

COPY function errors occur when the start position or length is negative, zero, or exceeds the string length.

## Common Causes

- Start position less than 1
- Length parameter negative or zero
- Start position beyond string length
- Result assigned to too-short string variable

## How to Fix

### 1. Validate parameters before COPY

```pascal
// WRONG: Unvalidated parameters
var Sub: string;
begin
  Sub := Copy(S, Start, Len);
end;

// CORRECT: Validate first
if (Start >= 1) and (Start <= Length(S)) and (Len > 0) then
  Sub := Copy(S, Start, Len)
else
  Sub := '';
```

### 2. Use Length function for bounds

```pascal
var Sub: string;
begin
  if Length(S) >= Start then
    Sub := Copy(S, Start, Length(S) - Start + 1)
  else
    Sub := '';
end.
```

## Examples

```pascal
program CopyDemo;

var
  Text: string;
  Sub: string;

begin
  Text := 'Hello, World!';
  Sub := Copy(Text, 8, 5);
  WriteLn('Substring: ', Sub);
end.
```

## Related Errors

- [String overflow error](/languages/pascal/pascal-string-overflow-error)
- [Range check error](/languages/pascal/range-check)
- [Runtime error](/languages/pascal/pascal-runtime-error)
