---
title: "[Solution] Fortran EQUIVALENCE Error"
description: "Fix Fortran EQUIVALENCE statement errors when aliasing variables in memory."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

EQUIVALENCE errors occur when aliased variables have incompatible types or when EQUIVALENCE causes unexpected memory overlaps.

## Common Causes

- EQUIVALENCE on variables of different types
- EQUIVALENCE overlapping array bounds
- Using EQUIVALENCE with allocatable arrays
- Aliasing causing unintended data modification

## How to Fix

### 1. Use UNION for compatible types

```fortran
! WRONG: Incompatible types
equivalence (a, b)  ! real and integer

! CORRECT: Use UNION
union
  map
    real :: x
  end map
  map
    integer :: i
  end map
end union
```

### 2. Avoid EQUIVALENCE in modern code

```fortran
! Use pointer or associate instead
real, target :: x
real, pointer :: p
p => x
```

## Examples

```fortran
program equivalence_demo
    implicit none
    integer :: i
    real :: r
    equivalence (i, r)

    i = 1065353216  ! IEEE 754 representation of 1.0
    print *, 'i =', i, ' r =', r
end program
```

## Related Errors

- [Array bounds error](/languages/fortran/array-bounds)
- [Runtime error](/languages/fortran/runtime-error11)
- [Undefined variable](/languages/fortran/undefined-variable)
