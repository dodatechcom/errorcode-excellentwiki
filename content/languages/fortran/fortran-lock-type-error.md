---
title: "[Solution] Fortran LOCK_TYPE Error"
description: "Fix Fortran LOCK_TYPE errors when using coarray locks for mutual exclusion."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

LOCK_TYPE errors occur when locks are used incorrectly or when lock operations deadlock.

## Common Causes

- LOCK without corresponding UNLOCK
- Nested LOCK causing deadlock
- LOCK on non-LOCK_TYPE variable
- Missing STAT= for lock error handling

## How to Fix

### 1. Always unlock after lock

```fortran
lock(lock_var)
! critical section
unlock(lock_var)
```

### 2. Use named locks

```fortran
lock(my_lock)
! ... work ...
unlock(my_lock)
```

## Examples

```fortran
program lock_demo
    use iso_fortran_env, only: lock_type
    implicit none
    type(lock_type) :: my_lock
    integer :: me
    me = this_image()
    print *, 'Image', me, 'lock demo'
end program
```

## Related Errors

- [Coarray error](/languages/fortran/fortran-coarray)
- [Critical section error](/languages/fortran/fortran-critical-section-error)
- [Runtime error](/languages/fortran/runtime-error11)
