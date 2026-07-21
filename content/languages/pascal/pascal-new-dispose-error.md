---
title: "[Solution] Pascal NEW and DISPOSE Error"
description: "Fix Pascal pointer allocation errors when using NEW and DISPOSE for dynamic memory management."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

NEW and DISPOSE errors occur when allocating nil pointers, double-disposing, or disposing uninitialized memory.

## Common Causes

- DISPOSE on nil pointer
- Double DISPOSE on same pointer
- Using pointer after DISPOSE (dangling pointer)
- NEW on type without valid constructor

## How to Fix

### 1. Check for nil before DISPOSE

```pascal
// WRONG: Double dispose
Dispose(P);
Dispose(P);  // error!

// CORRECT: Nil check and set to nil
if P <> nil then
begin
  Dispose(P);
  P := nil;
end;
```

### 2. Initialize pointers

```pascal
var P: ^Integer;
begin
  P := nil;  // initialize
  New(P);
  P^ := 42;
  Dispose(P);
  P := nil;  // clear after dispose
end.
```

## Examples

```pascal
program NewDisposeDemo;

type
  PString = ^String;

var
  S: PString;

begin
  New(S);
  S^ := 'Hello, dynamic memory!';
  WriteLn(S^);
  Dispose(S);
  S := nil;
end.
```

## Related Errors

- [Invalid pointer error](/languages/pascal/pascal-invalid-pointer)
- [Heap error](/languages/pascal/pascal-heap-error)
- [Memory leak error](/languages/pascal/pascal-memory-leak-error)
