---
title: "[Solution] Pascal POS Function Error"
description: "Fix Pascal POS function errors when searching for substrings with invalid parameters."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

POS function errors occur when searching for empty substrings or when parameters are not valid string types.

## Common Causes

- Searching for empty string returns 0
- POS with non-string arguments
- Using POS result without checking for 0
- POS on uninitialized string variable

## How to Fix

### 1. Check POS result before use

```pascal
var
  Idx: Integer;
begin
  Idx := Pos('needle', Haystack);
  if Idx > 0 then
    WriteLn('Found at position ', Idx)
  else
    WriteLn('Not found');
end;
```

### 2. Validate search string is not empty

```pascal
if Length(SearchStr) > 0 then
  Idx := Pos(SearchStr, Text)
else
  Idx := 0;
```

## Examples

```pascal
program PosDemo;

var
  Text: string;
  Sub: string;
  Idx: Integer;

begin
  Text := 'Find the needle in the haystack';
  Sub := 'needle';
  Idx := Pos(Sub, Text);
  if Idx > 0 then
    WriteLn(Sub, ' found at position ', Idx)
  else
    WriteLn(Sub, ' not found');
end.
```

## Related Errors

- [String comparison error](/languages/pascal/pascal-string-comparison-error)
- [Range check error](/languages/pascal/range-check)
- [Runtime error](/languages/pascal/pascal-runtime-error)
