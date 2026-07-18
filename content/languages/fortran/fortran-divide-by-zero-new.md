---
title: "[Solution] Fortran: floating point divide by zero"
description: "Fix Fortran divide by zero by validating divisors and using IEEE arithmetic exception handling."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A floating point divide by zero error in Fortran occurs when a real-valued division operation has a divisor of zero. Unlike integer division by zero which typically causes an immediate crash, floating point division by zero may produce infinity, NaN (Not a Number), or a hardware exception depending on the compiler flags and IEEE arithmetic settings. Some systems raise a hardware trap while others silently produce special floating point values. The behavior depends on whether the compiler enables IEEE exception handling by default.

## Why It Happens

Divide by zero errors occur when divisor variables are not properly initialized, when computed values unexpectedly become zero, or when user input provides a zero divisor. Array elements used as divisors may contain zero if not properly validated. Mathematical formulas where a denominator can approach zero, such as in iterative solvers or numerical differentiation, are common sources. Edge cases in algorithms, such as the last iteration of a loop or boundary conditions, may produce zero divisors. Functions like `1.0 / x` will produce infinity when x is zero, which may propagate through subsequent calculations and cause incorrect results even if no immediate crash occurs.

## How to Fix It

**Validate divisors before division:**

```fortran
program safe_divide
    implicit none
    real :: numerator, denominator, result

    numerator = 10.0
    denominator = 0.0

    if (abs(denominator) > tiny(1.0)) then
        result = numerator / denominator
        print *, 'Result:', result
    else
        print *, 'Error: divisor is effectively zero'
        result = huge(1.0)
    end if
end program
```

**Use IEEE arithmetic modules for proper handling:**

```fortran
program ieee_handling
    use ieee_arithmetic
    use ieee_exceptions
    implicit none
    real :: x, y, result
    logical :: valid

    x = 1.0
    y = 0.0

    ! Check if division would produce invalid result
    valid = ieee_is_finite(x / y) .and. .not. ieee_is_nan(x / y)

    if (valid) then
        result = x / y
    else
        print *, 'Division would produce non-finite result'
        result = 0.0
    end if
end program
```

**Enable floating point exception trapping:**

```fortran
! Compile with exception flags
! gfortran -ffpe-trap=zero,overflow -o myprog source.f90
! ifort -fpe0 -o myprog source.f90

program trapped_divide
    implicit none
    real :: a, b, c
    a = 1.0
    b = 0.0
    ! This will trap if compiled with -ffpe-trap=zero
    c = a / b
    print *, c
end program
```

**Protect array-based divisions:**

```fortran
program array_division
    implicit none
    real :: numerators(5), denominators(5), results(5)
    integer :: i

    numerators = (/ 10.0, 20.0, 30.0, 40.0, 50.0 /)
    denominators = (/ 2.0, 0.0, 5.0, 0.0, 10.0 /)

    do i = 1, 5
        if (abs(denominators(i)) > tiny(1.0)) then
            results(i) = numerators(i) / denominators(i)
        else
            results(i) = 0.0
        end if
    end do

    print *, results
end program


## Common Mistakes

- Assuming the compiler will always trap on divide by zero without enabling exception flags
- Not checking for near-zero values that cause overflow in the result
- Using `== 0.0` comparison for floating point values instead of an epsilon-based check
- Forgetting that IEEE special values like NaN and infinity propagate through calculations
- Not initializing divisor variables before using them in calculations

## Related Pages

- [Floating point overflow in Fortran](/languages/fortran/fortran-overflow-v2)
- [Array bounds exceeded in Fortran](/languages/fortran/fortran-array-bounds-new)
- [Undefined variable in Fortran](/languages/fortran/fortran-undefined-variable-new)
- [Compiler internal error in Fortran](/languages/fortran/fortran-compiler-error-new)
