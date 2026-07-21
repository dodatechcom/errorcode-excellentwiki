---
title: "[Solution] Fortran REWIND Statement Error"
description: "Fix Fortran REWIND statement errors when repositioning files to the beginning."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

REWIND errors occur when REWIND is called on units that are not open for sequential access or on invalid unit numbers.

## Common Causes

- REWIND on direct-access file
- REWIND on unopened unit
- Invalid unit number
- REWIND on stdin/stdout

## How to Fix

### 1. Ensure file is sequential

```fortran
open(unit=10, file='data.txt', status='old', access='sequential')
rewind(10)
```

### 2. Check unit is open

```fortran
inquire(unit=10, opened=is_open)
if (is_open) rewind(10)
```

## Examples

```fortran
program rewind_demo
    implicit none
    integer :: iu
    iu = 10
    open(unit=iu, file='temp.txt', status='replace')
    write(iu, *) 'First write'
    rewind(iu)
    write(iu, *) 'Second write (overwrites first)'
    close(iu)
end program
```

## Related Errors

- [I/O error](/languages/fortran/fortran-io-error)
- [Open error](/languages/fortran/fortran-open-error)
- [Runtime error](/languages/fortran/runtime-error11)
