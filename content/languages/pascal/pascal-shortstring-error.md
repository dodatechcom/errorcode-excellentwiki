---
title: "[Solution] Pascal ShortString Error — How to Fix"
description: "Fix ShortString errors in Pascal when fixed-length strings overflow or are used incorrectly."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1058
---

# ShortString Error

`ShortString` is a fixed-length string type (default 255 characters). Assigning a longer string truncates silently or causes overflow errors. Mixing `ShortString` with `AnsiString` creates encoding and size issues.

## Common Causes

- Assigning a string longer than the declared ShortString capacity
- Using `ShortString` in modern Delphi/FPC code where `AnsiString` is preferred
- Not reserving space for the length byte at position 0
- Comparing `ShortString` with `AnsiString` using `=` (type mismatch)

## How to Fix

### Solution 1 — Declare adequate ShortString length

```pascal
program ShortStringFix;

var
  Name: string[100];    // ShortString with 100 char capacity
begin
  Name := 'Alice';      // OK — within capacity
  WriteLn(Name);
end.
```

### Solution 2 — Use Copy for truncation control

```pascal
program SafeTruncation;

var
  Short: string[20];
  Long: string;
begin
  Long := 'This is a very long string that exceeds 20 characters';
  Short := Copy(Long, 1, 20);  // explicit truncation
  WriteLn(Short);
end.
```

### Solution 3 — Convert between ShortString and AnsiString

```pascal
program ConvertStrings;

var
  Short: string[50];
  Long: AnsiString;
begin
  Long := 'Hello, World!';
  Short := ShortString(Long);    // AnsiString to ShortString
  Long := AnsiString(Short);     // ShortString to AnsiString
  WriteLn(Short, ' | ', Long);
end.
```

### Solution 4 — Use SizeOf for capacity checks

```pascal
function FitsInShort(const S: string; MaxLen: Byte): Boolean;
begin
  Result := Length(S) <= MaxLen;
end;

var
  Short: string[30];
  Input: string;
begin
  Input := 'User input here';
  if FitsInShort(Input, 30) then
    Short := Input
  else
    WriteLn('Input too long');
end.
```

## Examples

A legacy database stores names as `string[20]`. A user enters a 25-character name. Without the `Copy` truncation, the assignment silently drops the last 5 characters. Using `Copy` with explicit length makes the truncation visible and controlled.

## Related Errors

- [AnsiString Error](/languages/pascal/pascal-ansistring-error) — ANSI string handling
- [String Overflow](/languages/pascal/pascal-string-overflow-error) — string size limits
- [Type Mismatch](/languages/pascal/pascal-type-mismatch) — type compatibility
