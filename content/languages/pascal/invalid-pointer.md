---
title: "Invalid pointer operation"
description: "An invalid pointer operation occurs when dereferencing or freeing an invalid pointer."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["pointer", "invalid", "memory", "pascal"]
weight: 5
---

## What This Error Means

An `Invalid pointer operation` occurs when you try to dereference, free, or manipulate a pointer that doesn't point to valid memory. This can happen with dangling pointers, double frees, or uninitialized pointers.

## Common Causes

- Dereferencing nil pointer
- Freeing already freed memory
- Using pointer after dispose
- Uninitialized pointer

## How to Fix

```pascal
program InvalidPointerDemo;

type
  PInteger = ^Integer;

var
  p: PInteger;

begin
  New(p);
  p^ := 42;
  Dispose(p);
  WriteLn(p^);  // Invalid pointer operation

  // CORRECT: Set to nil after dispose
  New(p);
  p^ := 42;
  Dispose(p);
  p := nil;
end.
```

```pascal
program NilPointerDemo;

var
  p: PInteger;

begin
  p := nil;
  WriteLn(p^);  // Invalid pointer operation

  // CORRECT: Check before dereferencing
  if p <> nil then
    WriteLn(p^)
  else
    WriteLn('Pointer is nil');
end.
```

## Examples

```pascal
program InvalidPointerExample;

var
  p: PInteger;

begin
  // Example 1: Uninitialized pointer
  GetMem(p, SizeOf(Integer));
  p^ := 10;
  FreeMem(p, SizeOf(Integer));
  p^ := 20;  // Invalid pointer operation

  // Example 2: Double free
  GetMem(p, SizeOf(Integer));
  FreeMem(p, SizeOf(Integer));
  FreeMem(p, SizeOf(Integer));  // Invalid pointer operation
end.
```

## Related Errors

- [Stack overflow](/languages/pascal/stack-overflow5)
- [I/O error](/languages/pascal/io-error)
