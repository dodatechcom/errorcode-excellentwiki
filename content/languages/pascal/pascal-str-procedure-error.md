---
title: "[Solution] Pascal STR Procedure Error"
description: "Fix Pascal STR procedure errors when converting numbers to strings with incorrect formatting."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

STR procedure errors occur when converting numbers to strings with format specifications that exceed the target string length.

## Common Causes

- Format width exceeds target string capacity
- Invalid format specification
- STR with negative width
- Target string too small for formatted output

## How to Fix

### 1. Use adequate string length

```pascal
// WRONG: String too short for format
var S: string[5];
begin
  Str(12345678:10, S);  // overflow!
end;

// CORRECT
var S: string[20];
begin
  Str(12345678:10, S);
  WriteLn(S);
end;
```

### 2. Use format parameters correctly

```pascal
Str(PI:0:4, S);  // decimal places
Str(42:5, S);    // field width
```

## Examples

```pascal
program StrDemo;

var
  Num: Integer;
  S: string[20];

begin
  Num := 42;
  Str(Num, S);
  WriteLn('Number as string: ', S);
  Str(Num:10, S);
  WriteLn('Right-aligned: ', S);
end.
```

## Related Errors

- [String overflow error](/languages/pascal/pascal-string-overflow-error)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
- [Runtime error](/languages/pascal/pascal-runtime-error)
