---
title: "[Solution] Pascal EOLN Error — How to Fix"
description: "Fix EOLN (end-of-line) errors in Pascal when reading text files line by line."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1057
---

# EOLN Error

`Eoln` returns `True` when the file pointer is at the end-of-line marker. Errors occur when `Eoln` is used on a non-text file, or when `Read` is called past the line ending without consuming it.

## Common Causes

- Using `Eoln` on a typed file (only valid for `Text`)
- Reading characters past the line ending without `ReadLn`
- `Eoln` returns `True` at EOF as well — double-check with `EOF`
- Not handling `CR+LF` vs `LF` line endings

## How to Fix

### Solution 1 — Read text file character by character

```pascal
program SafeEoln;

var
  F: Text;
  Ch: Char;
  Line: string;
begin
  AssignFile(F, 'input.txt');
  Reset(F);
  while not EOF(F) do
  begin
    Line := '';
    while not Eoln(F) do
    begin
      Read(F, Ch);
      Line := Line + Ch;
    end;
    ReadLn(F);  // consume line ending
    WriteLn(Line);
  end;
  CloseFile(F);
end.
```

### Solution 2 — Distinguish Eoln from EOF

```pascal
program EolnVsEOF;

var
  F: Text;
  Line: string;
begin
  AssignFile(F, 'data.txt');
  Reset(F);
  while not EOF(F) do
  begin
    ReadLn(F, Line);
    if Eoln(F) then
      WriteLn('End of line at: ', Line)
    else if EOF(F) then
      WriteLn('End of file at: ', Line);
  end;
  CloseFile(F);
end.
```

### Solution 3 — Handle different line endings

```pascal
program CrossPlatformLineEnding;

uses SysUtils;

var
  F: Text;
  Line: string;
begin
  AssignFile(F, 'data.txt');
  Reset(F);
  while not EOF(F) do
  begin
    ReadLn(F, Line);
    // FPC handles CR, LF, CR+LF automatically
    WriteLn(Line);
  end;
  CloseFile(F);
end.
```

### Solution 4 — Skip blank lines

```pascal
program SkipBlankLines;

var
  F: Text;
  Line: string;
begin
  AssignFile(F, 'data.txt');
  Reset(F);
  while not EOF(F) do
  begin
    ReadLn(F, Line);
    if Trim(Line) <> '' then
      WriteLn(Line);
  end;
  CloseFile(F);
end.
```

## Examples

A line-counting utility reads a text file but does not call `ReadLn` after reading to the end of a line. The `Eoln` check returns `True` indefinitely, creating an infinite loop. Adding `ReadLn(F)` inside the inner loop fixes the issue.

## Related Errors

- [EOF Error](/languages/pascal/pascal-eof-error) — end-of-file
- [Text File Error](/languages/pascal/pascal-text-file-error) — text mode
- [IO Error](/languages/pascal/io-error) — I/O failures
