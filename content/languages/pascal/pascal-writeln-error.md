---
title: "[Solution] Pascal WRITELN Error"
description: "Fix Pascal WRITELN errors when writing formatted output with incorrect field widths or types."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

WRITELN errors occur when writing output with format specifications that do not match the variable type or width.

## Common Causes

- Negative field width in write
- Writing string to integer field
- Format width too small for value
- Writing to closed or unassigned file

## How to Fix

### 1. Use correct format

```pascal
// WRONG: Wrong format for real
WriteLn(RealValue:10);  // missing decimal places

// CORRECT
WriteLn(RealValue:10:2);  // 10 width, 2 decimals
```

### 2. Match type to format

```pascal
WriteLn(IntValue:5);      // integer
WriteLn(StrValue:20);     // string
WriteLn(RealValue:12:4);  // real with decimals
```

## Examples

```pascal
program WriteLnDemo;

var
  Name: string;
  Score: Real;
  Rank: Integer;

begin
  Name := 'Alice';
  Score := 95.5;
  Rank := 1;
  WriteLn(Name:10, Rank:5, Score:10:1);
end.
```

## Related Errors

- [File not found](/languages/pascal/pascal-file-not-found)
- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
