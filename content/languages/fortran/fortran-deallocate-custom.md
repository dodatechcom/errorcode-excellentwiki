---
title: "[Solution] Fortran Deallocate Error — Memory Deallocation Issues"
description: "Fix Fortran deallocate errors. Actionable solutions with code examples."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1058
---

The `deallocate` statement frees allocated memory. Errors involve double deallocation, deallocating an unallocated array, or deallocating non-allocatable variables.

## Common Causes

- Double deallocation: calling deallocate on an already deallocated array
- Deallocating an array that was never allocated
- Deallocating a non-allocatable, non-pointer variable
- Missing `stat=` to handle deallocation errors gracefully

## How to Fix

### 1. Check allocated status before deallocating

```fortran
real, allocatable :: arr(:)
if (allocated(arr)) then
  deallocate(arr)
end if
```

### 2. Use stat= to catch errors

```fortran
integer :: ierr
real, allocatable :: arr(:)
deallocate(arr, stat=ierr)
if (ierr /= 0) then
  print *, 'Deallocation error:', ierr
end if
```

### 3. Set arrays to unallocated after deallocation

```fortran
deallocate(arr)
! arr is now unallocated; check with allocated(arr)
```

### 4. Use allocatable instead of pointer for simpler memory management

```fortran
! allocatable: automatic deallocation on scope exit
subroutine process()
  real, allocatable :: temp(:)
  allocate(temp(100))
  temp = 1.0
  ! temp is automatically deallocated when subroutine exits
end subroutine
```

### 5. In derived types with allocatable components, deallocate in proper order

```fortran
type :: container
  real, allocatable :: data(:)
end type

type(container) :: c
allocate(c%data(10))
deallocate(c%data)  ! component first
```

## Examples

Safe allocation/deallocation pattern:

```fortran
program safe_alloc
  implicit none
  real, allocatable :: arr(:)
  integer :: n, ierr

  n = 100
  allocate(arr(n), stat=ierr)
  if (ierr /= 0) stop 'Allocation failed'

  arr = [(real(i), i=1,n)]
  print *, sum(arr)

  if (allocated(arr)) deallocate(arr, stat=ierr)
  if (ierr /= 0) stop 'Deallocation failed'
end program
```

## Related Errors

- [Fortran Allocate Error](../fortran-allocate-error)
- [Fortran Realloc Error](../fortran-realloc-error)
- [Fortran Runtime Error](../fortran-runtime-error)
