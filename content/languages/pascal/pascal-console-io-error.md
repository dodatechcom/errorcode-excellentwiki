---
title: "[Solution] Pascal CONSOLE I/O Error"
description: "Fix Pascal console I/O errors when reading from or writing to the standard input/output handles."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

Console I/O errors occur when standard input/output handles are redirected or closed, causing READ and WRITE operations to fail.

## Common Causes

- Input redirected but program expects console
- Output pipe broken (reader closed)
- Console handle closed by parent process
- WRITE to closed standard output

## How to Fix

### 1. Check for redirected I/O

```pascal
var
  InputIsConsole: Boolean;
begin
  InputIsConsole := IsConsole;
  if InputIsConsole then
    WriteLn('Interactive mode')
  else
    WriteLn('Batch mode');
end;
```

### 2. Handle I/O errors gracefully

```pascal
begin
  try
    WriteLn('Output');
  except
    on E: Exception do
      { ignore I/O errors };
  end;
end;
```

## Examples

```pascal
program ConsoleDemo;

begin
  WriteLn('Enter your name:');
  WriteLn('Hello, User!');
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [File not found](/languages/pascal/pascal-file-not-found)
- [File mode error](/languages/pascal/pascal-file-mode-error)
