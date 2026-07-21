---
title: "[Solution] Pascal MARK and RELEASE Error"
description: "Fix Pascal MARK and RELEASE errors when using stack-based heap management."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

MARK and RELEASE errors occur when restoring the heap to a previously marked position, freeing all allocations after the mark.

## Common Causes

- RELEASE to invalid mark position
- Using freed memory after RELEASE
- Nested MARK/RELEASE mismatch
- MARK on corrupted heap

## How to Fix

### 1. Use MARK/RELEASE in matched pairs

```pascal
var
  P: Pointer;
  MarkVar: Pointer;
begin
  Mark(MarkVar);
  GetMem(P, 100);
  // use P
  Release(MarkVar);  // frees P too
end;
```

### 2. Do not use pointers after RELEASE

```pascal
Release(MarkVar);
// P is now invalid, do not use
```

## Examples

```pascal
program MarkReleaseDemo;

type
  PMark = ^Integer;

var
  MarkPtr: Pointer;
  TempPtr: Pointer;

begin
  Mark(MarkPtr);
  GetMem(TempPtr, 256);
  WriteLn('Temporary allocation made');
  Release(MarkPtr);
  WriteLn('Heap restored to mark');
end.
```

## Related Errors

- [Heap error](/languages/pascal/pascal-heap-error)
- [Invalid pointer error](/languages/pascal/pascal-invalid-pointer)
- [Runtime error](/languages/pascal/pascal-runtime-error)
