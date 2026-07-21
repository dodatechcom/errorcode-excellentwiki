---
title: "[Solution] Pascal INC and DEC Procedure Error"
description: "Fix Pascal INC and DEC procedure errors when incrementing or decrementing ordinal variables."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

INC and DEC errors occur when incrementing or decrementing values past their ordinal boundaries.

## Common Causes

- INC past maximum ordinal value
- DEC below minimum ordinal value
- INC/DEC on non-ordinal types
- INC/DEC with step exceeding range

## How to Fix

### 1. Check bounds before incrementing

```pascal
var
  N: Integer;
begin
  N := MaxInt;
  if N < MaxInt then
    Inc(N)
  else
    WriteLn('Cannot increment: at maximum');
end;
```

### 2. Use step parameter safely

```pascal
var
  Counter: Integer;
begin
  Counter := 0;
  Inc(Counter, 10);  // Counter := 10
  Dec(Counter, 5);   // Counter := 5
end;
```

## Examples

```pascal
program IncDecDemo;

var
  Count: Integer;
  Ch: Char;

begin
  Count := 0;
  Inc(Count, 5);
  WriteLn('Count: ', Count);
  Dec(Count, 2);
  WriteLn('Count: ', Count);
  Ch := 'A';
  Inc(Ch);
  WriteLn('Next char: ', Ch);
end.
```

## Related Errors

- [Overflow error](/languages/pascal/pascal-overflow-error)
- [Range check error](/languages/pascal/range-check)
- [Runtime error](/languages/pascal/pascal-runtime-error)
