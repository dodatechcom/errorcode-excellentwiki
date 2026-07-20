---
title: "[Solution] Pascal Encoding Error (WIN1250 vs UTF8) — How to Fix"
description: "Fix encoding errors in Pascal when string data is misinterpreted between WIN1250, UTF8, and other code pages."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1080
---

# WIN1250 vs UTF8 Encoding Error

Character encoding mismatches cause garbled text when data encoded in WIN1250 (Central European) is interpreted as UTF-8 or vice versa. This is common when mixing files, network data, and database strings.

## Common Causes

- Reading a UTF-8 file as WIN1250 (accented characters become multi-byte garbage)
- Writing WIN1250 data to a file expected to be UTF-8
- Database configured for one encoding, application for another
- Delphi `string` type is UTF-16 by default, not UTF-8 or WIN1250

## How to Fix

### Solution 1 — Convert between encodings explicitly

```pascal
program EncodingFix;

uses SysUtils;

var
  UTF8Str: UTF8String;
  ANSIStr: AnsiString;
begin
  UTF8Str := UTF8Encode('Příliš žluťoučký kůň');
  ANSIStr := UTF8Decode(UTF8Str);
  WriteLn(ANSIStr);
end.
```

### Solution 2 — Set default code page

```pascal
program SetCodePage;

uses SysUtils;

begin
  DefaultSystemCodePage := 1250;  // WIN1250
  // Now AnsiString operations use WIN1250
end.
```

### Solution 3 — Use TEncoding for file I/O

```pascal
program TEncodingDemo;

uses SysUtils, Classes;

var
  SL: TStringList;
begin
  SL := TStringList.Create;
  try
    SL.LoadFromFile('data.txt', TEncoding.UTF8);
    SL.SaveToFile('output.txt', TEncoding.ANSI);
  finally
    SL.Free;
  end;
end.
```

### Solution 4 — Detect encoding from BOM

```pascal
program BOMDetect;

uses SysUtils;

function DetectEncoding(const FileName: string): TEncoding;
var
  F: File;
  BOM: array[0..3] of Byte;
begin
  AssignFile(F, FileName);
  Reset(F, 1);
  BlockRead(F, BOM, 3);
  CloseFile(F);

  if (BOM[0] = $EF) and (BOM[1] = $BB) and (BOM[2] = $BF) then
    Result := TEncoding.UTF8
  else if (BOM[0] = $FF) and (BOM[1] = $FE) then
    Result := TEncoding.Unicode
  else
    Result := TEncoding.ANSI;
end;
```

## Examples

A Czech text file saved in WIN1250 is loaded with `LoadFromFile` which defaults to ANSI. Characters like `ř` and `ž` appear as `Ĺ˝` because their UTF-8 byte sequences are misinterpreted. Explicitly specifying the correct encoding fixes the display.

## Related Errors

- [AnsiString Error](/languages/pascal/pascal-ansistring-error) — ANSI strings
- [String Overflow](/languages/pascal/pascal-string-overflow-error) — string size
- [ShortString Error](/languages/pascal/pascal-shortstring-error) — fixed-length strings
