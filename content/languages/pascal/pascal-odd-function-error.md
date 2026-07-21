---
title: "[Solution] Pascal ODD Function Error"
description: "Fix Pascal ODD function errors when checking whether integer values are odd."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

ODD function errors occur when ODD is called on non-integer types or when the result is used incorrectly in boolean expressions.

## Common Causes

- ODD called on real or string type
- Misunderstanding ODD returns boolean
- ODD on negative numbers giving unexpected results
- Using ODD with bitwise AND incorrectly

## How to Fix

### 1. Use ODD only on integers

```pascal
var
  N: Integer;
  B: Boolean;
begin
  N := 42;
  B := Odd(N);  // returns False
end;
```

### 2. Use ODD correctly in conditions

```pascal
if Odd(N) then
  WriteLn('N is odd')
else
  WriteLn('N is even');
```

## Examples

```pascal
program OddDemo;

var
  Num: Integer;

begin
  for Num := 1 to 10 do
  begin
    if Odd(Num) then
      WriteLn(Num, ' is odd')
    else
      WriteLn(Num, ' is even');
  end;
end.
```

## Related Errors

- [Type mismatch](/languages/pascal/pascal-type-mismatch)
- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Compile error](/languages/pascal/pascal-compiler-error-new)
