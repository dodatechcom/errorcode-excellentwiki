---
title: "[Solution] Pascal: out of heap space error"
description: "Fix Pascal out of heap space errors by freeing unused memory and avoiding heap fragmentation."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An out of heap space error in Pascal occurs when the program requests more memory from the heap than is available. The heap is the area of memory used for dynamic allocation with `New`, `GetMem`, `AllocMem`, and `ReallocMem`. Pascal programs have a configurable heap size, and when it is exhausted, allocation requests fail. This triggers Runtime error 203 or returns nil from allocation functions. The error indicates that the program has consumed all available dynamic memory, either through excessive allocation, memory leaks, or insufficient heap size configuration.

## Why It Happens

Heap exhaustion results from several scenarios. Allocating many large records, arrays, or objects without freeing them causes gradual memory consumption. Memory leaks occur when `New` or `GetMem` is called but the corresponding `Dispose` or `FreeMem` is never executed, often due to early exits or error paths. Allocating inside tight loops without cleanup accumulates memory usage. The configured heap size may be too small for the program's needs, especially in Turbo Pascal where the default heap is limited. Fragmentation of the heap, where free memory exists in small scattered blocks but not in a contiguous block large enough for the request, can cause allocation failure even when total free memory is sufficient. Creating many linked list nodes, trees, or graph structures without proper cleanup is a classic source of heap exhaustion.

## How to Fix It

**Free memory when it is no longer needed:**

```pascal
program HeapManagement;
type
  PNode = ^TNode;
  TNode = record
    value: Integer;
    next: PNode;
  end;

var
  head, temp: PNode;
  i: Integer;
begin
  head := nil;

  { Create a linked list }
  for i := 1 to 1000 do
  begin
    New(temp);
    temp^.value := i;
    temp^.next := head;
    head := temp;
  end;

  { Free the entire list }
  while head <> nil do
  begin
    temp := head;
    head := head^.next;
    Dispose(temp);
  end;
end.
```

**Increase heap size in Turbo Pascal:**

```pascal
{ Set minimum and maximum heap sizes }
{ $M 16384,0,655360 }
{ 16KB stack minimum, heap up to 640KB }

program LargeHeap;
begin
  WriteLn('Heap size: ', MemAvail, ' bytes free');
end.
```

**Use GetMem and FreeMem for raw memory:**

```pascal
program RawMemory;
var
  buffer: Pointer;
  size: Integer;
begin
  size := 1000000;  { 1MB }
  GetMem(buffer, size);

  if buffer <> nil then
  begin
    { Use buffer... }
    FillChar(buffer^, size, 0);
    FreeMem(buffer, size);
    buffer := nil;
  end
  else
    WriteLn('Allocation failed');
end.
```

**Avoid fragmentation with batch allocation:**

```pascal
program BatchAlloc;
type
  TItem = record
    data: Integer;
  end;

  TItemArray = array of TItem;

var
  items: TItemArray;
  i: Integer;
begin
  { WRONG: many small allocations }
  { for i := 1 to 10000 do New(items[i]); }

  { CORRECT: single large allocation }
  SetLength(items, 10000);
  for i := 0 to 9999 do
    items[i].data := i;

  { Single deallocation }
  items := nil;
end.


## Common Mistakes

- Not calling `Dispose` or `FreeMem` on every allocated pointer
- Exiting a procedure with early `Exit` statements without freeing allocated memory
- Assuming garbage collection exists in standard Pascal (it does not)
- Allocating large objects on the heap when stack allocation would suffice
- Not checking if heap allocation succeeded before using the pointer

## Related Pages

- [Stack overflow in Pascal](/languages/pascal/pascal-stack-overflow-v2)
- [Invalid pointer operation in Pascal](/languages/pascal/pascal-invalid-pointer-v2)
- [Runtime error in Pascal](/languages/pascal/pascal-runtime-error-v2)
- [Range check error in Pascal](/languages/pascal/pascal-index-error-new)
