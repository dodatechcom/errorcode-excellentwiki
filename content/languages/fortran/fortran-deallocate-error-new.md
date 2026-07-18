---
title: "[Solution] Fortran: duplicate deallocation or deallocate failed"
description: "Fix Fortran deallocation errors by checking allocation status and avoiding double-free bugs."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Fortran deallocate error occurs when a DEALLOCATE statement is executed on an array that is either not currently allocated, has already been deallocated, or was never allocated. This is known as a double-free error and can cause memory corruption, program crashes, or undefined behavior. The error is indicated by a non-zero STAT value returned by the DEALLOCATE statement. Some compilers and runtime environments may also detect this condition and terminate the program with a descriptive error message.

## Why It Happens

Deallocate errors happen when program logic incorrectly manages the lifecycle of allocatable arrays. Calling DEALLOCATE on an array that has already been freed is the most common cause, often resulting from redundant cleanup code or incorrect control flow. Attempting to deallocate an array that was never allocated, perhaps because an earlier allocation failed, is another frequent scenario. Arrays allocated with automatic allocation (allocatable assignment) may have different ownership semantics that lead to confusion. Module-level allocatable arrays that are cleaned up by both the module and the calling program can be double-freed. Error handling paths that execute deallocation without checking allocation status also contribute to this problem.

## How to Fix It

**Check allocation status before deallocating:**

```fortran
program safe_dealloc
    implicit none
    real, allocatable :: data(:)
    integer :: alloc_status, dealloc_status

    allocate(data(100), stat=alloc_status)
    if (alloc_status /= 0) then
        print *, 'Allocation failed'
        stop
    end if

    data = 42.0

    ! Check before deallocating
    if (allocated(data)) then
        deallocate(data, stat=dealloc_status)
        if (dealloc_status /= 0) then
            print *, 'Dealloc failed with status:', dealloc_status
        end if
    end if
end program
```

**Use a flag to track allocation state:**

```fortran
program flag_tracking
    implicit none
    real, allocatable :: buffer(:)
    logical :: is_allocated

    is_allocated = .false.

    ! Allocation
    allocate(buffer(1000))
    is_allocated = .true.

    ! Use buffer...

    ! Safe deallocation
    if (is_allocated) then
        deallocate(buffer)
        is_allocated = .false.
    end if
end program
```

**Avoid deallocating in multiple code paths:**

```fortran
program single_cleanup
    implicit none
    real, allocatable :: matrix(:,:)
    integer :: ios

    allocate(matrix(100, 100))
    matrix = 0.0

    ! Process data
    call process(matrix, ios)

    ! Single cleanup point at the end
    if (allocated(matrix)) deallocate(matrix)

    if (ios /= 0) then
        print *, 'Processing error'
        stop
    end if

contains
    subroutine process(arr, status)
        real, allocatable, intent(in) :: arr(:,:)
        integer, intent(out) :: status
        status = 0
        ! Do not deallocate arr here, it is intent(in)
    end subroutine
end program
```

**Handle error paths carefully:**

```fortran
program error_handling
    implicit none
    real, allocatable :: temp(:)
    integer :: stat

    allocate(temp(500), stat=stat)
    if (stat /= 0) then
        print *, 'Cannot allocate temp'
        stop
    end if

    ! If an error occurs, clean up properly
    call risky_operation(temp, stat)
    if (stat /= 0) then
        print *, 'Operation failed, cleaning up'
    end if

    ! Always deallocate at the end, regardless of errors
    if (allocated(temp)) deallocate(temp)

contains
    subroutine risky_operation(arr, status)
        real, allocatable :: arr(:)
        integer, intent(out) :: status
        status = 0
        ! Process without deallocating arr
    end subroutine
end program
```

## Common Mistakes

- Not checking `allocated()` before calling DEALLOCATE
- Deallocating arrays in error handling paths that also deallocate at the end of the program
- Confusing intent(in) dummy arguments with allocatable arrays that the callee might deallocate
- Forgetting that allocatable assignment (`arr = value`) automatically deallocates the old array
- Leaving dangling pointers by not nullifying references after deallocation

## Related Pages

- [Memory allocation failed in Fortran](/languages/fortran/fortran-allocate-error-new)
- [Array bounds exceeded in Fortran](/languages/fortran/fortran-array-bounds-new)
- [End of file encountered in Fortran](/languages/fortran/fortran-end-of-file-v2)
- [I/O error in Fortran](/languages/fortran/fortran-io-error-v2)
