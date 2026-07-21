---
title: "[Solution] Fortran FLUSH Statement Error"
description: "Fix Fortran FLUSH statement errors when forcing output buffers to disk."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

FLUSH statement errors occur when FLUSH is called on units that are not open for writing or when the unit number is invalid.

## Common Causes

- FLUSH on unit not open
- FLUSH on read-only unit
- Invalid unit number
- FLUSH on stdin/stdout without buffering

## How to Fix

### 1. Check unit is open

```fortran
integer :: iu
iu = 10
open(unit=iu, file='output.txt', status='replace')
write(iu, *) 'Data'
flush(iu)  ! force to disk
close(iu)
```

### 2. Use FLUSH after critical writes

```fortran
write(6, *) 'Progress:', progress
flush(6)  ! flush stdout
```

## Examples

```fortran
program flush_demo
    implicit none
    integer :: iu
    iu = 20
    open(unit=iu, file='log.txt', status='replace')
    do i = 1, 100
        write(iu, *) 'Log entry', i
        if (mod(i, 10) == 0) flush(iu)
    end do
    close(iu)
end program
```

## Related Errors

- [I/O error](/languages/fortran/fortran-io-error)
- [Open error](/languages/fortran/fortran-open-error)
- [Runtime error](/languages/fortran/runtime-error11)
