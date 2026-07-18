---
title: "[Solution] Fortran: memory allocation failed"
description: "Fix Fortran memory allocation failures by checking STAT values and managing heap memory."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Fortran memory allocation error occurs when the ALLOCATE statement fails to obtain the requested memory from the system. The error is indicated by a non-zero STAT value returned by the ALLOCATE statement. This typically means the program has exhausted available memory, requested an excessively large allocation, or the system has insufficient resources. Memory allocation failures can crash the program or leave allocatable arrays in an undefined state if not handled properly.

## Why It Happens

Memory allocation failures occur when a program tries to allocate more memory than is available. Allocating very large arrays, especially multi-dimensional ones, can quickly consume available RAM. For example, allocating a 3D array of double precision with dimensions 1000 x 1000 x 1000 requires approximately 8 gigabytes. Memory leaks from repeated allocation without deallocation cause gradual memory exhaustion. Allocating arrays inside loops without deallocating previous allocations accumulates memory usage. The system may also be low on memory due to other running processes. requesting negative or zero sizes for allocation is another source of errors. Platform-specific limits on memory per process may also be exceeded.

## How to Fix It

**Always check the STAT parameter:**

```fortran
program safe_alloc
    implicit none
    real, allocatable :: big_array(:)
    integer :: alloc_status

    allocate(big_array(1000000), stat=alloc_status)
    if (alloc_status /= 0) then
        print *, 'Allocation failed with status:', alloc_status
        stop
    end if

    big_array = 42.0
    print *, 'Allocation successful'

    deallocate(big_array)
end program
```

**Deallocate before reallocating:**

```fortran
program realloc_pattern
    implicit none
    real, allocatable :: buffer(:)
    integer :: n, alloc_status

    n = 100
    allocate(buffer(n), stat=alloc_status)

    do while (alloc_status == 0)
        ! Use buffer
        buffer = real(n)

        ! Check if we need more space
        if (n > 10000) exit

        ! Deallocate before reallocating
        deallocate(buffer)
        n = n * 2
        allocate(buffer(n), stat=alloc_status)
    end do

    if (allocated(buffer)) deallocate(buffer)
end program
```

**Pre-calculate memory requirements:**

```fortran
program memory_check
    implicit none
    integer, parameter :: dp = selected_real_kind(15)
    real(kind=dp), allocatable :: matrix(:, :)
    integer :: n, alloc_status
    real :: mem_mb

    n = 10000
    mem_mb = real(n) * real(n) * 8.0 / (1024.0 * 1024.0)
    print *, 'Requested memory:', mem_mb, 'MB'

    if (mem_mb > 1000.0) then
        print *, 'Warning: requesting more than 1GB'
    end if

    allocate(matrix(n, n), stat=alloc_status)
    if (alloc_status /= 0) then
        print *, 'Allocation failed, trying smaller size'
        n = n / 2
        allocate(matrix(n, n), stat=alloc_status)
    end if

    if (alloc_status == 0) deallocate(matrix)
end program
```

**Use automatic allocation with bounds:**

```fortran
program auto_alloc
    implicit none
    real, allocatable :: data(:)
    integer :: n

    n = 1000
    allocate(data(n))
    data = [(real(i), i = 1, n)]

    ! Shrink allocation
    deallocate(data)
    n = 500
    allocate(data(n))
    data = [(real(i), i = 1, n)]

    deallocate(data)
end program
```

## Common Mistakes

- Not checking the STAT value after ALLOCATE, allowing silent failures
- Forgetting to deallocate arrays when they are no longer needed
- Allocating inside tight loops without first checking if the array is already allocated
- Using hardcoded large array sizes without considering available system memory
- Not using `ALLOCATED()` to check allocation status before deallocation

## Related Pages

- [Deallocate failed in Fortran](/languages/fortran/fortran-deallocate-error-new)
- [Array bounds exceeded in Fortran](/languages/fortran/fortran-array-bounds-new)
- [Floating point overflow in Fortran](/languages/fortran/fortran-overflow-new)
- [Undefined variable in Fortran](/languages/fortran/fortran-undefined-variable-new)
