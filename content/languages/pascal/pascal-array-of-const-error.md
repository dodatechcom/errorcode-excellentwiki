---
title: "[Solution] Pascal Array of Const Error — How to Fix"
description: "Fix array of const errors in Pascal when passing variant open arrays to variadic-style procedures."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1064
---

# Array of Const Error

`array of const` accepts a variable number of arguments as `TVarRec` records. Errors occur when accessing the wrong field of `TVarRec`, not checking `VType`, or passing incompatible types.

## Common Causes

- Accessing `VInteger` when `VType` indicates a string argument
- Not checking `VType` before accessing the appropriate union field
- Passing record types that are not supported by `TVarRec`
- Forgetting that `array of const` parameters are open arrays (no Length)

## How to Fix

### Solution 1 — Check VType before accessing fields

```pascal
program ArrayOfConstFix;

procedure PrintValues(const Args: array of const);
var
  I: Integer;
begin
  for I := 0 to High(Args) do
  begin
    case Args[I].VType of
      vtInteger: WriteLn('Integer: ', Args[I].VInteger);
      vtString:  WriteLn('String: ', Args[I].VString^);
      vtBoolean: WriteLn('Boolean: ', Args[I].VBoolean);
      vtPointer: WriteLn('Pointer: ', PtrUInt(Args[I].VPointer));
    else
      WriteLn('Unknown type: ', Args[I].VType);
    end;
  end;
end;

begin
  PrintValues([42, 'hello', True]);
end.
```

### Solution 2 — Handle string types safely

```pascal
program SafeStrings;

procedure LogMsg(const Args: array of const);
var
  I: Integer;
begin
  for I := 0 to High(Args) do
  begin
    if Args[I].VType = vtString then
      WriteLn(Args[I].VString^)
    else if Args[I].VType = vtAnsiString then
      WriteLn(AnsiString(Args[I].VAnsiString))
    else if Args[I].VType = vtUnicodeString then
      WriteLn(UnicodeString(Args[I].VUnicodeString));
  end;
end;

begin
  LogMsg(['test', 'values']);
end.
```

### Solution 3 — Build a Format-like function

```pascal
program FormatLike;

function MyFormat(const Fmt: string; const Args: array of const): string;
var
  I: Integer;
begin
  Result := Fmt;
  for I := 0 to High(Args) do
  begin
    if Args[I].VType = vtInteger then
      Result := StringReplace(Result, '%d', IntToStr(Args[I].VInteger), []);
  end;
end;

begin
  WriteLn(MyFormat('Value: %d', [42]));
end.
```

### Solution 4 — Pass dynamic arrays as array of const

```pascal
program PassDynamicArray;

procedure SumValues(const Vals: array of const);
var
  I, Total: Integer;
begin
  Total := 0;
  for I := 0 to High(Vals) do
    if Vals[I].VType = vtInteger then
      Total := Total + Vals[I].VInteger;
  WriteLn('Sum: ', Total);
end;

var
  Arr: array of Integer;
begin
  SetLength(Arr, 3);
  Arr[0] := 10; Arr[1] := 20; Arr[2] := 30;
  // Note: cannot pass dynamic array directly as array of const
  // Use: SumValues([Arr[0], Arr[1], Arr[2]]);
end.
```

## Examples

A logging function uses `array of const` to accept mixed types. It accesses `VInteger` for all arguments without checking `VType`. When a string is passed, the `VInteger` field contains garbage. Adding a `case` statement on `VType` fixes the issue.

## Related Errors

- [Variant Error](/languages/pascal/pascal-variant-error) — variant type issues
- [Type Mismatch](/languages/pascal/pascal-type-mismatch) — type compatibility
- [Dynamic Array Error](/languages/pascal/pascal-dynamic-array-error) — array issues
