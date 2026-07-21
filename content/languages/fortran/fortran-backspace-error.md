---
title: "[Solution] Fortran BACKSPACE Statement Error"
description: "Fix Fortran BACKSPACE statement errors when moving file position backward by one record."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

BACKSPACE errors occur when BACKSPACE is called on units that are not open for sequential access or at the beginning of file.

## Common Causes

- BACKSPACE on direct-access file
- BACKSPACE at beginning of file
- BACKSPACE on unopened unit
- BACKSPACE on non-record file

## How to Fix

### 1. Ensure sequential access

```fortran
open(unit=10, file='data.txt', access='sequential')
backspace(10)
```

### 2. Check position before backspacing

```fortran
inquire(unit=10, pos=pos)
if (pos > 1) backspace(10)
```

## Examples

```fortran
program backspace_demo
    implicit none
    integer :: iu, val
    iu = 10
    open(unit=iu, file='bs_temp.txt', status='replace')
    write(iu, *) 100
    write(iu, *) 200
    backspace(iu)
    read(iu, *) val
    print *, 'Read back:', val
    close(iu)
end program
```

## Related Errors

- [I/O error](/languages/fortran/fortran-io-error)
- [Open error](/languages/fortran/fortran-open-error)
- [Runtime error](/languages/fortran/runtime-error11)
