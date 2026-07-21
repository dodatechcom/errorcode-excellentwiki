---
title: "[Solution] Pascal READLN Error"
description: "Fix Pascal READLN errors when reading text input including buffer overflow and format mismatch."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

READLN errors occur when reading past end of file, reading into variables of wrong type, or reading into undersized string buffers.

## Common Causes

- Reading past end of file
- Type mismatch between input and variable
- String buffer too small for input line
- READLN on binary file

## How to Fix

### 1. Check for end of file

```pascal
while not Eof(f) do
begin
  ReadLn(f, Line);
  ProcessLine(Line);
end;
```

### 2. Use adequate buffer size

```pascal
var
  Line: string[200];  // large enough
begin
  if not Eof(f) then
    ReadLn(f, Line);
end;
```

## Examples

```pascal
program ReadLnDemo;

var
  f: TextFile;
  Name: string;
  Age: Integer;

begin
  AssignFile(f, 'input.txt');
  Reset(f);
  while not Eof(f) do
  begin
    ReadLn(f, Name, Age);
    WriteLn(Name, ' is ', Age, ' years old');
  end;
  CloseFile(f);
end.
```

## Related Errors

- [File not found](/languages/pascal/pascal-file-not-found)
- [EOLN error](/languages/pascal/pascal-eoln-error)
- [Runtime error](/languages/pascal/pascal-runtime-error)
