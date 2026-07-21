---
title: "[Solution] Pascal DISPOSE Error"
description: "Fix Pascal DISPOSE errors when freeing pointer memory including nil checks and dangling pointer issues."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

DISPOSE errors occur when freeing nil pointers, double-disposing, or accessing memory after it has been disposed.

## Common Causes

- DISPOSE on nil pointer
- Double DISPOSE on same pointer
- Accessing pointer after DISPOSE
- DISPOSE on uninitialized pointer

## How to Fix

### 1. Always nil-check before dispose

```pascal
if P <> nil then
begin
  Dispose(P);
  P := nil;
end;
```

### 2. Set pointer to nil after dispose

```pascal
Dispose(P);
P := nil;  // prevent dangling pointer
```

## Examples

```pascal
program DisposeDemo;

type
  PData = ^TData;
  TData = record
    Value: Integer;
  end;

var
  D: PData;

begin
  New(D);
  D^.Value := 100;
  WriteLn(D^.Value);
  Dispose(D);
  D := nil;
end.
```

## Related Errors

- [Invalid pointer error](/languages/pascal/pascal-invalid-pointer)
- [Heap error](/languages/pascal/pascal-heap-error)
- [Memory leak error](/languages/pascal/pascal-memory-leak-error)
