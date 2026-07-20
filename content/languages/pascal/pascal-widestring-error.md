---
title: "[Solution] Pascal WideString Error — How to Fix"
description: "Fix WideString errors in Pascal when handling Unicode strings with incorrect buffer management."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1060
---

# WideString Error

`WideString` is a COM-compatible, reference-counted Unicode string (UTF-16). Errors occur when passing to APIs expecting `PWideChar` after the string has been freed, or when converting between `AnsiString` and `WideString` loses data.

## Common Causes

- `WideString` passed to API via `PWideChar` — pointer invalid after string goes out of scope
- Implicit conversion between `AnsiString` (code page) and `WideString` (UTF-16)
- No null terminator when used with C APIs expecting `wchar_t*`
- Memory overhead from UTF-16 encoding (2x byte size)

## How to Fix

### Solution 1 — Ensure WideString lifetime exceeds pointer usage

```pascal
program WideStringFix;

uses Windows;

var
  WS: WideString;
begin
  WS := 'Hello, Unicode!';
  MessageBoxW(0, PWideChar(WS), 'Title', 0);
  // WS must remain alive during the API call
end.
```

### Solution 2 — Convert AnsiString to WideString safely

```pascal
program SafeConversion;

var
  Ansi: AnsiString;
  Wide: WideString;
begin
  Ansi := 'Café';
  Wide := WideString(Ansi);   // uses default code page
  WriteLn(Wide);
end.
```

### Solution 3 — Use WideString for COM interop

```pascal
program COMInterop;

var
  WS: WideString;
  P: PWideChar;
begin
  WS := 'COM string';
  P := SysAllocString(PWideChar(WS));
  // use P with COM API
  SysFreeString(P);
end.
```

### Solution 4 — Handle WideString with null terminator

```pascal
program NullTerminated;

var
  WS: WideString;
begin
  WS := 'Test';
  // WideString already includes null terminator in FPC
  // Use PWideChar(WS) directly with C APIs
end.
```

## Examples

A Windows API function receives a `PWideChar` parameter. The code passes `PWideChar(WideString('temp'))` — the temporary `WideString` is freed immediately, and the pointer becomes dangling. Storing the `WideString` in a variable extends its lifetime.

## Related Errors

- [AnsiString Error](/languages/pascal/pascal-ansistring-error) — ANSI encoding
- [PChar Error](/languages/pascal/pascal-pchar-error) — C string pointers
- [Encoding Error](/languages/pascal/pascal-encoding-error) — code page issues
