---
title: "[Solution] Pascal Text File Error — How to Fix"
description: "Fix text file errors in Pascal when reading or writing to text-mode files with incorrect procedures."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1045
---

# Text File Error

Text files in Pascal are line-oriented, using `ReadLn`/`WriteLn` for I/O. Errors occur when mixing typed and text file operations, reading past EOF, or using `Seek` on text files.

## Common Causes

- Using `Seek` on a text file (not supported for text files)
- `ReadLn` without `Eoln` check causing reads past end of line
- Writing binary data to a text file variable
- Using `file of Char` instead of `Text` for text I/O

## How to Fix

### Solution 1 — Use correct text file procedures

```pascal
program TextFileFix;

var
  F: Text;
  S: string;
begin
  AssignFile(F, 'data.txt');
  Rewrite(F);
  WriteLn(F, 'Hello, World!');
  WriteLn(F, 'Second line');
  CloseFile(F);

  Reset(F);
  while not Eof(F) do
  begin
    ReadLn(F, S);
    WriteLn(S);
  end;
  CloseFile(F);
end.
```

### Solution 2 — Check Eoln before reading a line

```pascal
program SafeReadLn;

var
  F: Text;
  Ch: Char;
  Line: string;
begin
  AssignFile(F, 'input.txt');
  Reset(F);
  Line := '';
  while not Eof(F) do
  begin
    if not Eoln(F) then
    begin
      Read(F, Ch);
      Line := Line + Ch;
    end
    else
    begin
      WriteLn('Line: ', Line);
      Line := '';
      ReadLn(F);  // consume end-of-line
    end;
  end;
  CloseFile(F);
end.
```

### Solution 3 — Use Assign/Append for appending to text files

```pascal
program AppendText;

var
  F: Text;
begin
  AssignFile(F, 'log.txt');
  Append(F);              // open for appending (at end)
  WriteLn(F, 'New log entry');
  CloseFile(F);
end.
```

### Solution 4 — Convert text file to typed file for Seek

```pascal
program TextToTyped;

var
  F: file of Char;
  Ch: Char;
begin
  AssignFile(F, 'data.bin');
  Reset(F);
  Seek(F, 100);          // OK for typed file
  Read(F, Ch);
  CloseFile(F);
end.
```

## Examples

A log processor reads a large text file line by line. Using `Read(F, Ch)` without checking `Eoln` causes the line buffer to include newline characters. Adding `ReadLn(F)` after reading the last character of each line fixes the parsing.

## Related Errors

- [EOF Error](/languages/pascal/pascal-eof-error) — end-of-file detection
- [EOLN Error](/languages/pascal/pascal-eoln-error) — end-of-line detection
- [IO Error](/languages/pascal/io-error) — I/O failures
