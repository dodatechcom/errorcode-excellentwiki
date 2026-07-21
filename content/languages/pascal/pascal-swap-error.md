---
title: "[Solution] Pascal SWAP Function Error"
description: "Fix Pascal SWAP function errors when byte-swapping values with incorrect types."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

SWAP function errors occur when swapping bytes of values that are not 16-bit integers.

## Common Causes

- SWAP on 32-bit integer (only swaps low 16 bits)
- SWAP on byte or char type
- Using SWAP on string types
- Endianness assumptions incorrect

## How to Fix

### 1. Use SWAP on 16-bit types

```pascal
var
  W: Word;
begin
  W := $1234;
  W := Swap(W);  // $3412
end;
```

### 2. Use for correct types

```pascal
var
  Short: SmallInt;
begin
  Short := 256;
  Short := Swap(Short);  // byte swap
end;
```

## Examples

```pascal
program SwapDemo;

var
  Original: Word;
  Swapped: Word;

begin
  Original := $ABCD;
  Swapped := Swap(Original);
  WriteLn('Original: $', HexStr(Original, 4));
  WriteLn('Swapped: $', HexStr(Swapped, 4));
end.
```

## Related Errors

- [Type mismatch](/languages/pascal/pascal-type-mismatch)
- [Range check error](/languages/pascal/range-check)
- [Runtime error](/languages/pascal/pascal-runtime-error)
