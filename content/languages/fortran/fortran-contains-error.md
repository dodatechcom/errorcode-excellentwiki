---
title: "[Solution] Fortran Contains Error"
description: "Fix Fortran CONTAINS section syntax errors caused by misplaced procedures or missing module boundaries."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

## Why It Happens

CONTAINS section error

## Common Error Messages

1. **Fortran syntax error at CONTAINS**
2. **invalid placement of CONTAINS statement**
3. **CONTAINS without preceding program unit**

## How to Fix It

### Solution 1: Check allocation status before using

```fortran
program safe_alloc
    implicit none
    integer, allocatable :: arr(:)
    integer :: ierr
    allocate(arr(1000), stat=ierr)
    if (ierr /= 0) then
        print *, "Allocation failed with error:", ierr
        stop
    end if
    arr = 42
    print *, "Allocation succeeded, arr(1) =", arr(1)
    deallocate(arr)
end program safe_alloc
```

### Solution 2: Use deallocate before reallocating

```fortran
program realloc_example
    implicit none
    integer, allocatable :: data(:)
    integer :: ierr
    allocate(data(100))
    data = 1
    ! Always deallocate before reallocating
    if (allocated(data)) deallocate(data)
    allocate(data(200), stat=ierr)
    if (ierr /= 0) then
        print *, "Reallocation failed"
        stop
    end if
    data = 2
    deallocate(data)
end program realloc_example
```

### Solution 3: Enable runtime bounds checking during development

```fortran
program bounds_check
    implicit none
    integer :: arr(10)
    integer :: i
    arr = (/ (i, i = 1, 10) /)
    ! Compile with -fcheck=all for bounds checking
    do i = 1, 10
        print *, "arr(", i, ") =", arr(i)
    end do
end program bounds_check
```

## Common Scenarios

### Scenario 1: Memory allocation failure in CONTAINS section error

Memory allocation failure in CONTAINS section error often occurs when developers forget to handle edge cases in their code. For example:

```fortran
! Example scenario demonstrating the issue
! This commonly happens in production code
! Always validate inputs before processing
```

### Scenario 2: Resource exhaustion during CONTAINS section error

Another frequent cause is incorrect type usage or missing declarations. Consider this pattern:

```fortran
! Common pattern that leads to this error
! Always check types and dimensions
! Use compiler/runtime flags for early detection
```

### Scenario 3: Edge case triggering CONTAINS section error

Performance-related issues can also trigger this error under load:

```fortran
! Performance scenario example
! Monitor resource usage in production
! Add graceful degradation for resource limits
```

## Prevent It

- **Always validate input parameters before allocation or processing**
- **Use compiler flags like -fcheck=all for Fortran to catch issues early**
- **Add proper error handling and cleanup with STAT= and deallocate**

## Related Errors

- [Fortran best practices](/languages/fortran)
- [Fortran error handling guide](/languages/fortran/_index)
