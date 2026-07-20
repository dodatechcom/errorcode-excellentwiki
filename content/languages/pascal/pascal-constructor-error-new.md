---
title: "[Solution] Pascal Constructor Error — How to Fix"
description: "Fix constructor errors in Pascal when object initialization fails or constructors are misused."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1067
---

# Constructor Error

Constructors in Pascal initialize objects and allocate resources. Errors occur when the constructor does not call `inherited Create`, when it fails to allocate memory, or when `Self` is used before initialization.

## Common Causes

- Not calling `inherited Create` in a derived class constructor
- Constructor allocating resources that are never freed (no matching destructor)
- Using `Self` before calling `inherited Create`
- Constructor raising an exception without proper cleanup

## How to Fix

### Solution 1 — Always call inherited Create

```pascal
program ConstructorFix;

type
  TBase = class
    Name: string;
    constructor Create(const AName: string);
  end;

  TDerived = class(TBase)
    Age: Integer;
    constructor Create(const AName: string; AAge: Integer);
  end;

constructor TBase.Create(const AName: string);
begin
  inherited Create;       // call TObject.Create
  Name := AName;
end;

constructor TDerived.Create(const AName: string; AAge: Integer);
begin
  inherited Create(AName);  // call TBase.Create
  Age := AAge;
end;
```

### Solution 2 — Handle constructor failure

```pascal
program SafeConstructor;

type
  TResource = class
    Data: Pointer;
    constructor Create(Size: Integer);
    destructor Destroy; override;
  end;

constructor TResource.Create(Size: Integer);
begin
  inherited Create;
  GetMem(Data, Size);
  if Data = nil then
    raise Exception.Create('Out of memory');
end;

destructor TResource.Destroy;
begin
  if Data <> nil then
    FreeMem(Data);
  inherited Destroy;
end;
```

### Solution 3 — Initialize fields in constructor

```pascal
program InitFields;

type
  TConfig = class
    Host: string;
    Port: Integer;
    Active: Boolean;
    constructor Create;
  end;

constructor TConfig.Create;
begin
  inherited Create;
  Host := 'localhost';
  Port := 8080;
  Active := False;
end;
```

### Solution 4 — Use try/except in constructor

```pascal
program ConstructorException;

type
  TDatabase = class
    Connected: Boolean;
    constructor Create(const DBPath: string);
    destructor Destroy; override;
  end;

constructor TDatabase.Create(const DBPath: string);
begin
  inherited Create;
  Connected := False;
  try
    // attempt connection
    Connected := True;
  except
    on E: Exception do
    begin
      Connected := False;
      raise;  // re-raise after cleanup
    end;
  end;
end;

destructor TDatabase.Destroy;
begin
  if Connected then
    ; // disconnect
  inherited Destroy;
end;
```

## Examples

A derived class constructor forgets to call `inherited Create`. The VMT pointer is not initialized, and calling any virtual method causes an access violation. Adding `inherited Create` at the beginning of the constructor fixes the initialization.

## Related Errors

- [Destructor Error](/languages/pascal/pascal-destructor-error) — cleanup issues
- [Memory Leak](/languages/pascal/pascal-memory-leak-error) — resource leaks
- [Invalid Pointer](/languages/pascal/pascal-invalid-pointer) — nil pointer access
