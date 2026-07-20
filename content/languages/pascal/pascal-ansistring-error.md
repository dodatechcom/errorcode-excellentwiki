---
title: "[Solution] Pascal AnsiString Error — How to Fix"
description: "Fix AnsiString errors in Pascal when handling ANSI-encoded strings with incorrect code pages."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1059
---

# AnsiString Error

`AnsiString` is a reference-counted, heap-allocated string with code page awareness. Errors occur when mixing code pages, passing to PChar without conversion, or when the reference count drops to zero prematurely.

## Common Causes

- Mixing `AnsiString` with different code pages (e.g., WIN1250 vs UTF8)
- Implicit conversion losing non-ASCII characters
- Passing `AnsiString` to a function expecting `PChar` without `PAnsiChar` cast
- Memory leak from manual `New(PAnsiChar)` without `Dispose`

## How to Fix

### Solution 1 — Set code page explicitly

```pascal
program AnsiStringFix;

uses SysUtils;

var
  S: AnsiString;
begin
  S := 'Hello';  // default code page
  SetCodePage(RawByteString(S), 1250, True);  // WIN1250
  WriteLn(S);
end.
```

### Solution 2 — Convert between AnsiString and PChar safely

```pascal
program SafePChar;

var
  S: AnsiString;
  P: PAnsiChar;
begin
  S := 'Hello, World!';
  P := PAnsiChar(S);     // valid while S is alive
  WriteLn(P);
  // Do not free S while P is in use
end.
```

### Solution 3 — Handle mixed encoding

```pascal
program MixedEncoding;

uses SysUtils;

var
  Utf8Str: AnsiString;
  WinStr: AnsiString;
begin
  Utf8Str := UTF8Encode('Příliš žluťoučký kůň');
  WinStr := AnsiToUtf8(Utf8Str);
  WriteLn(WinStr);
end.
```

### Solution 4 — Use RawByteString for encoding-agnostic storage

```pascal
program RawByteStringDemo;

var
  Raw: RawByteString;
begin
  Raw := 'Binary data with accents: é, ž, š';
  // RawByteString preserves byte values without code page conversion
end.
```

## Examples

A text file encoded in WIN1250 is loaded into an `AnsiString`. The program then passes it to a function expecting UTF8. Characters like `ř` and `ž` are mangled. Explicitly converting with `AnsiToUtf8` before passing fixes the encoding mismatch.

## Related Errors

- [ShortString Error](/languages/pascal/pascal-shortstring-error) — fixed-length strings
- [PChar Error](/languages/pascal/pascal-pchar-error) — pointer strings
- [Encoding Error](/languages/pascal/pascal-encoding-error) — code page issues
