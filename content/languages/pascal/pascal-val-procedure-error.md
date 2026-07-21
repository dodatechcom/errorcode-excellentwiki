---
title: "[Solution] Pascal VAL Procedure Error"
description: "Fix Pascal VAL procedure errors when converting strings to numbers including invalid format and overflow."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

VAL procedure errors occur when converting non-numeric strings to numbers or when the result overflows the target variable.

## Common Causes

- String contains non-numeric characters
- Number too large for target integer type
- VAL with empty string
- Not checking the error code parameter

## How to Fix

### 1. Check VAL error code

```pascal
var
  Code: Integer;
  Num: Integer;
begin
  Val('123abc', Num, Code);
  if Code <> 0 then
    WriteLn('Error at position ', Code)
  else
    WriteLn('Value: ', Num);
end;
```

### 2. Use appropriate type for large numbers

```pascal
var
  LargeNum: Int64;
  Code: Integer;
begin
  Val('9999999999', LargeNum, Code);
end;
```

## Examples

```pascal
program ValDemo;

var
  Input: string;
  Num: Integer;
  Code: Integer;

begin
  Input := '42';
  Val(Input, Num, Code);
  if Code = 0 then
    WriteLn('Parsed: ', Num)
  else
    WriteLn('Parse error at position ', Code);
end.
```

## Related Errors

- [Type mismatch](/languages/pascal/pascal-type-mismatch)
- [Overflow error](/languages/pascal/pascal-overflow-error)
- [Runtime error](/languages/pascal/pascal-runtime-error)
