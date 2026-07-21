---
title: "[Solution] Fortran DO CONCURRENT Error"
description: "Fix Fortran DO CONCURRENT errors when using concurrent loop constructs for parallel execution."
languages: ["fortran"]
error-types: ["syntax-error"]
severities: ["error"]
---

DO CONCURRENT errors occur when the concurrent loop has dependencies between iterations or uses invalid constructs.

## Common Causes

- Data dependency between iterations
- EXIT or CYCLE in DO CONCURRENT
- Procedure call with side effects
- I/O operations in DO CONCURRENT

## How to Fix

### 1. Ensure iteration independence

```fortran
! WRONG: Dependency between iterations
do concurrent (i = 1:10)
    arr(i) = arr(i-1) + 1  ! dependency
end do

! CORRECT: Independent iterations
do concurrent (i = 1:10)
    arr(i) = i * 2  ! no dependency
end do
```

### 2. No EXIT or CYCLE allowed

```fortran
! WRONG
do concurrent (i = 1:10)
    if (arr(i) == 0) cycle  ! not allowed
end do
```

## Examples

```fortran
program do_concurrent_demo
    implicit none
    integer :: arr(100)
    integer :: i
    do concurrent (i = 1:100)
        arr(i) = i ** 2
    end do
    print *, 'First:', arr(1), ' Last:', arr(100)
end program
```

## Related Errors

- [Do loop error](/languages/fortran/fortran-do-loop)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
- [Runtime error](/languages/fortran/runtime-error11)
