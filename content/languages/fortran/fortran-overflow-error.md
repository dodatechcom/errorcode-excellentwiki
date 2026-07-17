---
title: "Overflow error in Fortran"
description: "Overflow error in Fortran occurs when an arithmetic result exceeds the maximum value the data type can hold."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An overflow error occurs when a calculation produces a value larger than the data type can represent. Integer overflow wraps around (undefined behavior), while real overflow produces Infinity.

## Common Causes

- Multiplication of large integers
- Accumulating large sums
- Factorial computation on small data types
- Missing range checking

## How to Fix

```fortran
! WRONG: Integer overflow
program overflow_example
    implicit none
    integer :: i, result
    result = 1
    do i = 1, 20
        result = result * i   ! Overflow after i=12 (32-bit int)
    end do
    print *, 'Factorial:', result
end program
```

```fortran
! CORRECT: Use larger data types or check range
program overflow_safe
    implicit none
    integer(8) :: i, result   ! Use 64-bit integer
    result = 1_8
    do i = 1, 20
        result = result * i
    end do
    print *, 'Factorial:', result
end program
```

## Examples

```fortran
program example
    implicit none
    integer :: x
    x = 2147483647   ! Max 32-bit integer
    x = x + 1        ! Overflow
    print *, x       ! May print -2147483648
end program
```

## Related Errors

- [Division by Zero](/languages/fortran/division-zero8) - arithmetic errors
- [Array Bounds](/languages/fortran/array-bounds2) - index errors
