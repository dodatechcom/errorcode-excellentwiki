---
title: "[Solution] Pascal Destructor Error — How to Fix"
description: "Fix destructor errors in Pascal when object cleanup is incomplete or destructors are called incorrectly."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1068
---

# Destructor Error

Destructors in Pascal release resources allocated by constructors. Errors occur when destructors are called multiple times, when `inherited Destroy` is not called, or when resources are not properly released.

## Common Causes

- Not calling `inherited Destroy` in a derived destructor
- Double-free: calling `Free` on an already-freed object
- Forgetting to release resources (memory, handles, files)
- Calling methods on an object after `Free` has been called

## How to Fix

### Solution 1 — Always call inherited Destroy

```pascal
program DestructorFix;

type
  TBase = class
    destructor Destroy; override;
  end;

  TDerived = class(TBase)
    Buffer: Pointer;
    destructor Destroy; override;
  end;

destructor TBase.Destroy;
begin
  inherited Destroy;
end;

destructor TDerived.Destroy;
begin
  if Buffer <> nil then
    FreeMem(Buffer);
  inherited Destroy;       // call TBase.Destroy
end;
```

### Solution 2 — Use Free (nil-safe) instead of Destroy

```pascal
program UseFree;

var
  Obj: TObject;
begin
  Obj := TObject.Create;
  try
    // use Obj
  finally
    Obj.Free;            // Free calls Destroy only if Self <> nil
  end;
end.
```

### Solution 3 — Check nil before freeing

```pascal
program SafeFree;

type
  TWidget = class
    Data: Pointer;
    destructor Destroy; override;
  end;

destructor TWidget.Destroy;
begin
  if Data <> nil then
  begin
    FreeMem(Data);
    Data := nil;         // prevent double-free
  end;
  inherited Destroy;
end;

var
  W: TWidget;
begin
  W := TWidget.Create;
  W.Free;
  W := nil;              // prevent use-after-free
end.
```

### Solution 4 — Try/finally for destructor safety

```pascal
program DestructorSafety;

type
  TFileHolder = class
    F: Text;
    destructor Destroy; override;
  end;

destructor TFileHolder.Destroy;
begin
  try
    CloseFile(F);
  except
    // ignore close errors in destructor
  end;
  inherited Destroy;
end;
```

## Examples

A class allocates memory in its constructor. The destructor calls `FreeMem` but forgets `inherited Destroy`. The parent class's cleanup (like closing a file handle) is skipped, leaking the handle. Adding `inherited Destroy` fixes the leak.

## Related Errors

- [Constructor Error](/languages/pascal/pascal-constructor-error) — initialization
- [Memory Leak](/languages/pascal/pascal-memory-leak-error) — resource leaks
- [Invalid Pointer](/languages/pascal/pascal-invalid-pointer) — nil pointer access
