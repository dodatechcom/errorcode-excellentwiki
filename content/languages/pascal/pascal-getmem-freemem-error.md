---
title: "[Solution] Pascal GETMEM and FREEMEM Error"
description: "Fix Pascal low-level memory allocation errors when using GETMEM and FREEMEM directly."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

GETMEM and FREEMEM errors occur when allocating or freeing memory incorrectly at the low-level heap manager.

## Common Causes

- FREEMEM on pointer not from GETMEM
- Double FREEMEM on same pointer
- Size mismatch in FREEMEM
- Memory leak from missing FREEMEM

## How to Fix

### 1. Always match GETMEM with FREEMEM

```pascal
var
  P: Pointer;
begin
  GetMem(P, 100);
  // use P
  FreeMem(P, 100);  // same size
  P := nil;
end;
```

### 2. Initialize to nil

```pascal
var
  P: Pointer;
begin
  P := nil;
  GetMem(P, SizeOf(Integer));
  PInteger(P)^ := 42;
  FreeMem(P, SizeOf(Integer));
  P := nil;
end;
```

## Examples

```pascal
program GetMemDemo;

var
  Buffer: Pointer;
  BufSize: Integer;

begin
  BufSize := 1024;
  GetMem(Buffer, BufSize);
  FillChar(Buffer^, BufSize, 0);
  WriteLn('Allocated ', BufSize, ' bytes');
  FreeMem(Buffer, BufSize);
  Buffer := nil;
end.
```

## Related Errors

- [Heap error](/languages/pascal/pascal-heap-error)
- [Invalid pointer error](/languages/pascal/pascal-invalid-pointer)
- [Memory leak error](/languages/pascal/pascal-memory-leak-error)
