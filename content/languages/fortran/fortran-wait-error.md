---
title: "[Solution] Fortran WAIT Statement Error"
description: "Fix Fortran WAIT statement errors when completing non-blocking I/O operations."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

WAIT statement errors occur when WAIT is called on units without pending non-blocking operations or with invalid unit numbers.

## Common Causes

- WAIT on unit with no pending async I/O
- Invalid unit number in WAIT
- WAIT before any async operation started
- Missing error handling after WAIT

## How to Fix

### 1. Check for pending operations

```fortran
integer :: ierr
logical :: pending
inquire(unit=10, pending=pending)
if (pending) then
    wait(10, iostat=ierr)
    if (ierr /= 0) print *, 'WAIT error:', ierr
end if
```

### 2. Always check iostat after WAIT

```fortran
wait(10, iostat=ierr, err=100)
return
100 print *, 'WAIT failed'
```

## Examples

```fortran
program wait_demo
    implicit none
    real :: buf(100)
    integer :: ierr
    buf = 0.0
    print *, 'Wait demo complete'
end program
```

## Related Errors

- [I/O error](/languages/fortran/fortran-io-error)
- [Async attribute error](/languages/fortran/fortran-async-attribute-error)
- [Runtime error](/languages/fortran/runtime-error11)
