---
title: "[Solution] Pascal SET TYPE Error"
description: "Fix Pascal set type errors when performing operations on set variables with incompatible or oversized elements."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

SET TYPE errors occur when set operations are performed with elements outside the allowed ordinal range or when sets exceed maximum size.

## Common Causes

- Set element value exceeds 255 (byte-sized)
- Assigning set of different base types
- Set intersection with incompatible types
- Set containing more than 256 possible values

## How to Fix

### 1. Limit set base type to byte

```pascal
// WRONG: Set of Integer (too large)
type LargeSet = set of Integer;

// CORRECT: Set of 0..255
type SmallSet = set of 0..255;
var MySet: SmallSet;
```

### 2. Match set types

```pascal
var
  A: set of 'A'..'Z';
  B: set of 'A'..'Z';
begin
  A := ['A', 'B', 'C'];
  B := ['D', 'E'];
  A := A + B;  // union
end.
```

## Examples

```pascal
program SetTypeDemo;

type
  TCharSet = set of Char;
  TNumSet = set of 1..100;

var
  Letters: TCharSet;
  Numbers: TNumSet;
  Common: TCharSet;

begin
  Letters := ['A', 'B', 'C', 'D'];
  Numbers := [1, 2, 3, 4, 5];
  Common := Letters * ['A', 'C', 'E'];
  WriteLn('Common: ', Common);
end.
```

## Related Errors

- [Range check error](/languages/pascal/range-check)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
- [Overflow error](/languages/pascal/pascal-overflow-error)
