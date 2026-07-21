---
title: "[Solution] Pascal MOVE Procedure Error"
description: "Fix Pascal MOVE procedure errors when copying memory blocks with incorrect source, destination, or count."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

MOVE procedure errors occur when copying memory blocks that overlap, have invalid sizes, or point to deallocated memory.

## Common Causes

- Count exceeds source or destination buffer size
- Source and destination overlap (undefined behavior)
- MOVE on nil pointers
- Size mismatch between source and destination types

## How to Fix

### 1. Validate buffer sizes

```pascal
var
  Src: array[1..10] of Byte;
  Dst: array[1..10] of Byte;
begin
  Move(Src, Dst, SizeOf(Src));  // use SizeOf
end;
```

### 2. Use SizeOf for type safety

```pascal
Move(Source^, Dest^, SizeOf(Source^));
```

## Examples

```pascal
program MoveDemo;

var
  Source: array[1..5] of Integer;
  Dest: array[1..5] of Integer;
  i: Integer;

begin
  for i := 1 to 5 do
    Source[i] := i * 10;
  Move(Source, Dest, SizeOf(Source));
  for i := 1 to 5 do
    WriteLn('Dest[', i, '] = ', Dest[i]);
end.
```

## Related Errors

- [Invalid pointer error](/languages/pascal/pascal-invalid-pointer)
- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Memory leak error](/languages/pascal/pascal-memory-leak-error)
