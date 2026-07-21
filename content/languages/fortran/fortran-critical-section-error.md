---
title: "[Solution] Fortran CRITICAL Section Error"
description: "Fix Fortran CRITICAL construct errors when synchronizing concurrent execution in OpenMP."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

CRITICAL section errors occur when the CRITICAL construct is used incorrectly or when deadlock occurs from nested critical sections.

## Common Causes

- Nested CRITICAL causing deadlock
- Missing END CRITICAL
- CRITICAL on wrong code section
- Named CRITICAL with inconsistent names

## How to Fix

### 1. Use named CRITICAL sections

```fortran
! Named critical sections to avoid deadlock
!$omp critical(section1)
    call do_work_1()
!$omp end critical(section1)

!$omp critical(section2)
    call do_work_2()
!$omp end critical(section2)
```

### 2. Avoid nested CRITICAL

```fortran
! WRONG: Nested critical can deadlock
!$omp critical
    call outer()
    !$omp critical  ! deadlock risk
        call inner()
    !$omp end critical
!$omp end critical
```

## Examples

```fortran
program critical_demo
    use omp_lib
    implicit none
    integer :: shared_counter
    shared_counter = 0
    !$omp parallel
    !$omp critical
    shared_counter = shared_counter + 1
    !$omp end critical
    !$omp end parallel
    print *, 'Counter:', shared_counter
end program
```

## Related Errors

- [Runtime error](/languages/fortran/runtime-error11)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Do loop error](/languages/fortran/fortran-do-loop)
