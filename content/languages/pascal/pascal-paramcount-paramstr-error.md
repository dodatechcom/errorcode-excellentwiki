---
title: "[Solution] Pascal PARAMCOUNT and PARAMSTR Error"
description: "Fix Pascal PARAMCOUNT and PARAMSTR errors when accessing command-line arguments."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

PARAMCOUNT and PARAMSTR errors occur when accessing command-line arguments with out-of-range indices.

## Common Causes

- PARAMSTR with index > PARAMCOUNT
- Not checking PARAMCOUNT before access
- PARAMSTR(0) used as first argument (it is program name)
- Empty command line

## How to Fix

### 1. Check argument count

```pascal
if ParamCount >= 1 then
  WriteLn('First arg: ', ParamStr(1))
else
  WriteLn('No arguments');
```

### 2. Know that ParamStr(0) is program name

```pascal
WriteLn('Program: ', ParamStr(0));  // executable path
if ParamCount > 0 then
  WriteLn('Args: ', ParamStr(1));
```

## Examples

```pascal
program ParamDemo;

var
  i: Integer;

begin
  WriteLn('Program: ', ParamStr(0));
  WriteLn('Argument count: ', ParamCount);
  for i := 1 to ParamCount do
    WriteLn('Arg ', i, ': ', ParamStr(i));
end.
```

## Related Errors

- [Range check error](/languages/pascal/range-check)
- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Compile error](/languages/pascal/pascal-compiler-error-new)
