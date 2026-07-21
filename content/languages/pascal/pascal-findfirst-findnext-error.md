---
title: "[Solution] Pascal FINDFIRST/FINDNEXT Error"
description: "Fix Pascal FINDFIRST and FINDNEXT errors when searching for files in directories."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

FINDFIRST and FINDNEXT errors occur when searching for files with invalid patterns or when the search handle is not properly closed.

## Common Causes

- Invalid file search pattern
- FINDFIRST without matching FINDNEXT cleanup
- Search pattern containing invalid characters
- Not closing search with FindClose

## How to Fix

### 1. Always close search with FindClose

```pascal
var
  SearchRec: TSearchRec;
begin
  if FindFirst('*.txt', faAnyFile, SearchRec) = 0 then
  begin
    repeat
      WriteLn(SearchRec.Name);
    until FindNext(SearchRec) <> 0;
  end;
  FindClose(SearchRec);
end;
```

### 2. Use valid search patterns

```pascal
FindFirst('*.*', faAnyFile, SearchRec);
// or more specific
FindFirst('data_*.csv', faArchive, SearchRec);
```

## Examples

```pascal
program FindFirstNextDemo;

var
  SR: TSearchRec;

begin
  if FindFirst('*', faAnyFile, SR) = 0 then
  begin
    repeat
      WriteLn(SR.Name);
    until FindNext(SR) <> 0;
  end;
  FindClose(SR);
end.
```

## Related Errors

- [File not found](/languages/pascal/pascal-file-not-found)
- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Directory error](/languages/pascal/pascal-directory-error)
