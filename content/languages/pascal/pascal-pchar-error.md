---
title: "[Solution] Pascal PChar Error — How to Fix"
description: "Fix PChar errors in Pascal when using C-style null-terminated string pointers."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1061
---

# PChar Error

`PChar` is a pointer to a null-terminated character array. Errors occur when dereferencing a nil PChar, accessing memory after the pointed-to string has been freed, or passing a non-null-terminated string to C functions.

## Common Causes

- Dereferencing a nil or uninitialized `PChar`
- String pointed to by `PChar` has been freed (dangling pointer)
- Missing null terminator when constructing a `PChar` manually
- Assigning `PChar(@MyString)` when `MyString` is not null-terminated

## How to Fix

### Solution 1 — Validate PChar before use

```pascal
program SafePChar;

var
  P: PChar;
begin
  P := nil;
  if P <> nil then
    WriteLn(StrLen(P))
  else
    WriteLn('PChar is nil');
end.
```

### Solution 2 — Ensure null termination

```pascal
program NullTerminate;

var
  Buf: array[0..255] of AnsiChar;
begin
  FillChar(Buf, SizeOf(Buf), 0);
  Buf[0] := 'H';
  Buf[1] := 'i';
  // Buf is null-terminated due to FillChar
  WriteLn(PChar(@Buf));
end.
```

### Solution 3 — Use StrPas for safe conversion

```pascal
program PCharToString;

var
  P: PChar;
  S: string;
begin
  P := 'Hello';   // string literal → PChar
  S := StrPas(P); // PChar → string (safe)
  WriteLn(S);
end.
```

### Solution 4 — Lifetime management

```pascal
program PCharLifetime;

var
  S: AnsiString;
  P: PChar;
begin
  S := 'Persistent string';
  P := PAnsiChar(S);
  // P is valid as long as S is alive
  WriteLn(P);
  // Do NOT set S := '' before using P
end.
```

## Examples

A Windows API receives a `PChar` filename. The code constructs the filename in a local `string` variable and passes `PChar(FileName)`. The local string is freed when the function returns, but the API call is still in progress. Storing the string in a wider scope prevents the dangling pointer.

## Related Errors

- [AnsiString Error](/languages/pascal/pascal-ansistring-error) — ANSI string handling
- [String Overflow](/languages/pascal/pascal-string-overflow-error) — size limits
- [Type Mismatch](/languages/pascal/pascal-type-mismatch) — type compatibility
