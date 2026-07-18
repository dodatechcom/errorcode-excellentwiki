---
title: "[Solution] Pascal: invalid pointer operation error"
description: "Fix Pascal invalid pointer operations by checking nil before dereferencing and using New correctly."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An invalid pointer operation in Pascal occurs when a program attempts to dereference a pointer that is nil, has already been freed, or was never properly initialized. This triggers Runtime error 204 or an access violation. Pointer errors are particularly dangerous because they can cause silent memory corruption, crashes, or unpredictable behavior that manifests far from the original bug. Pascal's pointer type system provides some safety but does not prevent all invalid operations at runtime.

## Why It Happens

Invalid pointer operations arise from several common mistakes. Dereferencing a pointer variable that has not been assigned a valid address (and thus contains nil or garbage) is the most frequent cause. Using `Dispose` to free memory and then continuing to use the pointer creates a dangling pointer. Accessing fields of a pointer to a record after the record has been freed is another scenario. Double-freeing the same pointer with `Dispose` corrupts the heap. Not initializing pointer variables in records or arrays leaves them with random values. Using `New` to allocate but forgetting to call it before using the pointer results in nil dereference. Incorrect pointer arithmetic or casting can also produce invalid pointer values.

## How to Fix It

**Check pointers before dereferencing:**

```pascal
program SafeDereference;
type
  PNode = ^TNode;
  TNode = record
    value: Integer;
    next: PNode;
  end;

var
  node: PNode;
begin
  New(node);
  node^.value := 42;
  node^.next := nil;

  { WRONG: dereference without check }
  { WriteLn(node^.next^.value); }  { nil dereference }

  { CORRECT: check before dereferencing }
  if node^.next <> nil then
    WriteLn(node^.next^.value)
  else
    WriteLn('Next node is nil');

  Dispose(node);
end.
```

**Always initialize pointers:**

```pascal
program InitPointers;
type
  PData = ^TData;
  TData = record
    value: Integer;
    next: PData;
  end;

var
  head: PData;
begin
  head := nil;  { Initialize to nil }

  New(head);
  head^.value := 10;
  head^.next := nil;  { Initialize next to nil }

  Dispose(head);
end.
```

**Do not use pointers after Dispose:**

```pascal
program NoDangling;
type
  PItem = ^TItem;
  TItem = record
    data: Integer;
  end;

var
  item: PItem;
begin
  New(item);
  item^.data := 100;

  Dispose(item);
  item := nil;  { Set to nil after dispose }

  { WRONG: using item after dispose }
  { WriteLn(item^.data); }

  { CORRECT: check for nil }
  if item <> nil then
    WriteLn(item^.data)
  else
    WriteLn('Item has been disposed');
end.
```

**Use try-finally for safe cleanup:**

```pascal
program SafeCleanup;
{$mode objfpc}
uses SysUtils;

type
  PNode = ^TNode;
  TNode = record
    value: Integer;
  end;

var
  node: PNode;
begin
  node := nil;
  try
    New(node);
    node^.value := 42;
    WriteLn('Value: ', node^.value);
  finally
    if node <> nil then
    begin
      Dispose(node);
      node := nil;
    end;
  end;
end.
```

## Common Mistakes

- Dereferencing a pointer without first checking it against nil
- Using a pointer after calling Dispose on it
- Forgetting to call New before using a pointer variable
- Not setting pointers to nil after disposing them
- Double-disposing the same pointer without reassigning between disposes

## Related Pages

- [Stack overflow in Pascal](/languages/pascal/pascal-stack-overflow-v2)
- [Out of heap space in Pascal](/languages/pascal/pascal-heap-error-new)
- [Runtime error in Pascal](/languages/pascal/pascal-runtime-error-v2)
- [Range check error in Pascal](/languages/pascal/pascal-index-error-new)
