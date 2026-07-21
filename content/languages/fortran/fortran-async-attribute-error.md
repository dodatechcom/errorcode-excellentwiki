---
title: "[Solution] Fortran ASYNCHRONOUS Attribute Error"
description: "Fix Fortran ASYNCHRONOUS attribute errors when using asynchronous I/O with non-blocking operations."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

ASYNCHRONOUS attribute errors occur when the attribute is applied to variables not used with non-blocking I/O operations.

## Common Causes

- ASYNCHRONOUS on variable not used with WAIT
- Missing ASYNCHRONOUS on variable used with non-blocking I/O
- ASYNCHRONOUS preventing optimization of local variables
- ASYNCHRONOUS with INTENT(OUT) arrays

## How to Fix

### 1. Use ASYNCHRONOUS for non-blocking I/O

```fortran
real, asynchronous :: buffer(100)
read(10, async='yes', iostat=ierr) buffer
! Process other work
wait(10, iostat=ierr)
```

### 2. Match ASYNCHRONOUS with actual usage

```fortran
subroutine async_read(buf)
    real, asynchronous :: buf(:)
    read(10, async='yes') buf
end subroutine
```

## Examples

```fortran
program async_demo
    implicit none
    real, asynchronous :: data(100)
    integer :: ierr
    data = 0.0
    print *, 'Async I/O demo'
end program
```

## Related Errors

- [I/O error](/languages/fortran/fortran-io-error)
- [Runtime error](/languages/fortran/runtime-error11)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
