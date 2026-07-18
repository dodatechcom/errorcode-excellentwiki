---
title: "[Solution] Pascal: file not found error"
description: "Fix Pascal file not found errors by verifying paths and handling directory separators correctly."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Pascal file not found error occurs when an `Assign` or `Reset`/`Rewrite` statement references a file that does not exist at the specified path. This triggers Runtime error 2 or an I/O error with status 2. The error means the operating system could not locate the file at the path provided to the Pascal program. This is one of the most common runtime errors in Pascal file I/O operations and can occur with both text files and binary files.

## Why It Happens

File not found errors have several causes. The file path may be incorrect, containing typos or wrong directory separators. Pascal compilers on different platforms handle path separators differently: Windows uses backslashes while Unix uses forward slashes. Relative paths depend on the current working directory, which may not be what you expect when the program is run from a different location. The file may not exist yet if `Reset` is used instead of `Rewrite` for creating new files. File permissions may prevent the file from being accessed, causing the OS to report it as not found. Case sensitivity matters on Unix systems where `Data.txt` and `data.txt` are different files. Using `Assign` with a variable that contains uninitialized or garbage data will also produce this error.

## How to Fix It

**Verify file paths exist before opening:**

```pascal
program SafeFileOpen;
var
  f: TextFile;
  filePath: string;
begin
  filePath := 'data/input.txt';

  Assign(f, filePath);

  { Check if file exists before opening }
  if FileExists(filePath) then
  begin
    Reset(f);
    { Read file... }
    Close(f)
  end
  else
    WriteLn('File not found: ', filePath);
end.
```

**Use platform-independent path construction:**

```pascal
program PortablePaths;
uses SysUtils;
var
  basePath, fileName, fullPath: string;
begin
  basePath := ExtractFilePath(ParamStr(0));
  fileName := 'data.txt';
  fullPath := IncludeTrailingPathDelimiter(basePath) + fileName;

  WriteLn('Full path: ', fullPath);

  if FileExists(fullPath) then
    WriteLn('File exists')
  else
    WriteLn('File not found');
end.
```

**Create files with Rewrite instead of Reset:**

```pascal
program CreateFile;
var
  f: TextFile;
begin
  Assign(f, 'output.txt');
  Rewrite(f);    { Creates file if it does not exist }
  WriteLn(f, 'Hello, World!');
  Close(f);
end.
```

**Handle case sensitivity on Unix:**

```pascal
program CaseSensitive;
var
  f: TextFile;
begin
  { On Unix, these are different files }
  Assign(f, 'Data.TXT');  { Must match exact case on Linux }
  if FileExists('Data.TXT') then
    Reset(f)
  else
    WriteLn('Check exact filename case');
end.
```

**Check current working directory:**

```pascal
program CheckCWD;
begin
  WriteLn('Current directory: ', GetCurrentDir);
  WriteLn('Program location: ', ParamStr(0));

  { Use absolute paths for reliability }
  Assign(f, '/home/user/project/data.txt');
end.
```

## Common Mistakes

- Using `Reset` on a file that has not been created yet instead of `Rewrite`
- Not using `FileExists` to check before attempting to open
- Mixing path separators between Windows and Unix
- Forgetting that the current working directory changes when you change directories in code
- Not initializing the filename variable before passing it to `Assign`

## Related Pages

- [Invalid pointer operation in Pascal](/languages/pascal/pascal-invalid-pointer-v2)
- [Runtime error in Pascal](/languages/pascal/pascal-runtime-error-v2)
- [Out of heap space in Pascal](/languages/pascal/pascal-heap-error-new)
- [Type mismatch in Pascal](/languages/pascal/pascal-type-mismatch-v2)
