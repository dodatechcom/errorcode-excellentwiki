---
title: "Division by zero in Fortran"
description: "Division by zero in Fortran causes a runtime error when dividing an integer or real number by zero."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Division by zero in Fortran is undefined behavior that causes a runtime error. With integers, it always crashes. With reals, behavior depends on the compiler (may produce Inf, NaN, or crash).

## Common Causes

- Computed divisor resulting in zero
- Uninitialized variable as divisor
- User input of zero for divisor
- Array index from division by zero

## How to Fix

```fortran
! WRONG: No check before division
program div_zero
    implicit none
    integer :: a, b, result
    a = 10
    b = 0
    result = a / b   ! Runtime error
end program
```

```fortran
! CORRECT: Check divisor before dividing
program div_safe
    implicit none
    integer :: a, b, result
    a = 10
    b = 0
    if (b /= 0) then
        result = a / b
        print *, 'Result:', result
    else
        print *, 'Error: division by zero'
    end if
end program
```

```fortran
! CORRECT: Safe division function
function safe_div(a, b) result(res)
    integer, intent(in) :: a, b
    integer :: res
    if (b == 0) then
        res = 0
    else
        res = a / b
    end if
end function
```

## Examples

```fortran
program example
    implicit none
    integer :: i, j, result
    i = 5
    j = 0
    result = i / j   ! Runtime error: Division by zero
end program
```

## Related Errors

- [Overflow Error](/languages/fortran/overflow-error5) - arithmetic overflow
- [Array Bounds](/languages/fortran/array-bounds2) - index out of range
