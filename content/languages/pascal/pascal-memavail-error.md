---
title: "[Solution] Pascal MEMAVAIL Function Error"
description: "Fix Pascal MEMAVAIL function errors when querying available heap memory incorrectly."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

MEMAVAIL function errors occur when the heap is corrupted or when MEMAVAIL returns misleading values.

## Common Causes

- MEMAVAIL on corrupted heap
- Not accounting for heap fragmentation
- MEMAVAIL returning wrong value after large allocation
- Using MEMAVAIL to decide allocation without checking return

## How to Fix

### 1. Always check allocation result

```pascal
var
  P: Pointer;
begin
  if MemAvail > 1024 then
  begin
    GetMem(P, 1024);
    if P <> nil then
      // use P
    else
      WriteLn('Allocation failed');
  end;
end;
```

### 2. Do not rely solely on MEMAVAIL

```pascal
// Heap may be fragmented
// MEMAVAIL may show enough but GetMem still fails
```

## Examples

```pascal
program MemAvailDemo;

var
  FreeMem: LongInt;

begin
  FreeMem := MemAvail;
  WriteLn('Available heap: ', FreeMem, ' bytes');
end.
```

## Related Errors

- [Heap error](/languages/pascal/pascal-heap-error)
- [Memory leak error](/languages/pascal/pascal-memory-leak-error)
- [Runtime error](/languages/pascal/pascal-runtime-error)
