---
title: "[Solution] Pascal FILLCHAR Error"
description: "Fix Pascal FILLCHAR errors when filling memory buffers with values including incorrect size or fill value."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

FILLCHAR errors occur when filling memory with a size that exceeds the buffer, or when using invalid fill characters.

## Common Causes

- Fill size exceeds buffer size
- FillChar on nil pointer
- Using string type with FillChar incorrectly
- FillChar on read-only memory

## How to Fix

### 1. Use SizeOf for buffer size

```pascal
var
  Buf: array[1..100] of Byte;
begin
  FillChar(Buf, SizeOf(Buf), 0);  // clear all
end;
```

### 2. Use FillChar correctly on strings

```pascal
var
  S: string;
begin
  S := 'Hello';
  FillChar(S[1], Length(S), #0);  // clear content
  S[0] := #0;  // set length to 0
end;
```

## Examples

```pascal
program FillCharDemo;

var
  Buffer: array[1..50] of Byte;
  i: Integer;

begin
  FillChar(Buffer, SizeOf(Buffer), $FF);
  for i := 1 to 10 do
    Write(Buffer[i]:4);
  WriteLn;
end.
```

## Related Errors

- [Invalid pointer error](/languages/pascal/pascal-invalid-pointer)
- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Memory leak error](/languages/pascal/pascal-memory-leak-error)
