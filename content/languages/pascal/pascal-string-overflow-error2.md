---
title: "[Solution] Pascal STRING Overflow Error"
description: "Fix Pascal short string overflow when assigning strings longer than declared maximum length."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

String overflow errors occur when assigning a string to a short string variable that is too small to hold the value.

## Common Causes

- String assignment exceeds declared length
- Concatenation result too long for target
- Input larger than string buffer
- Copy function with too-large range

## How to Fix

### 1. Use adequate string length

```pascal
// WRONG: String too short
var ShortStr: string[5];
begin
  ShortStr := 'Hello World';  // overflow!
end;

// CORRECT
var LongStr: string[20];
begin
  LongStr := 'Hello World';
end;
```

### 2. Use AnsiString for dynamic length

```pascal
var S: AnsiString;
begin
  S := 'Any length string is fine';
end.
```

## Examples

```pascal
program StringOverflowDemo;

var
  Name: string[20];
  FullName: string[50];

begin
  Name := 'John';
  FullName := Name + ' Doe the Third';
  WriteLn(FullName);
end.
```

## Related Errors

- [String comparison error](/languages/pascal/pascal-string-comparison-error)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
- [Overflow error](/languages/pascal/pascal-overflow-error)
