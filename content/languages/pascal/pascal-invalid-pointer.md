---
title: "Invalid pointer in Pascal"
description: "Invalid pointer errors in Pascal occur when using a pointer that is nil, freed, or not properly initialized."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["pointer", "nil", "dangling", "memory", "pascal"]
weight: 5
---

## What This Error Means

Invalid pointer errors occur when dereferencing a nil pointer, accessing freed memory (dangling pointer), or performing invalid pointer arithmetic.

## Common Causes

- Dereferencing nil pointer
- Using pointer after FreeMem/Dispose
- Uninitialized pointer variable
- Double-free of same pointer
- Invalid pointer arithmetic

## How to Fix

```pascal
program InvalidPointerDemo;

type
  PInteger = ^Integer;

var
  p: PInteger;

begin
  // WRONG: Dereferencing nil pointer
  p := nil;
  WriteLn(p^);   // Invalid pointer error

  // CORRECT: Check before dereferencing
  p := nil;
  if p <> nil then
    WriteLn(p^)
  else
    WriteLn('Pointer is nil');
end.
```

```pascal
// CORRECT: Initialize pointer before use
program SafePointerDemo;

var
  p: PInteger;

begin
  New(p);        // Allocate memory
  p^ := 42;
  WriteLn(p^);   // Safe
  Dispose(p);    // Free memory
  p := nil;      // Set to nil after freeing
end.
```

## Examples

```pascal
program Example;
var
  p: ^Integer;
begin
  p := nil;
  p^ := 10;   // Invalid pointer error
end.
```

## Related Errors

- [Runtime Error](/languages/pascal/pascal-runtime-error) - general errors
- [Stack Overflow](/languages/pascal/stack-overflow5) - memory errors
