---
title: "[Solution] Fortran: floating point overflow error"
description: "Fix Fortran floating point overflow by using larger data types and scaling calculations safely."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A floating point overflow error in Fortran occurs when a calculation produces a result that exceeds the representable range of the data type. For `REAL(KIND=4)` (single precision), values beyond approximately 3.4 x 10^38 overflow. Double precision (`REAL(KIND=8)`) overflows beyond approximately 1.8 x 10^308. The result becomes infinity or triggers a hardware exception. This error is particularly common in iterative calculations where values grow exponentially, or in power and exponential functions applied to large arguments.

## Why It Happens

Floating point overflow stems from calculations that produce values too large for the data type. Exponential growth in iterative algorithms, such as population models or compound interest calculations, can quickly exceed single precision limits. Computing large powers, exponentials, or factorials without proper scaling is a frequent cause. Intermediate calculations may overflow even when the final result should be within range, a problem known as intermediate overflow. Summing many large numbers can also overflow. Using single precision (`REAL(4)`) when double precision (`REAL(8)`) is needed is a common oversight. Multiplying two large numbers together can overflow even though each factor individually fits in the type's range.

## How to Fix It

**Use double precision for extended range:**

```fortran
program double_precision
    implicit none
    ! WRONG: single precision may overflow
    ! real :: result
    ! result = exp(1000.0)  ! Overflows single precision

    ! CORRECT: use double precision
    real(kind=8) :: result
    result = exp(1000.0d0)
    print *, result  ! Large but finite value
end program
```

**Scale calculations to prevent intermediate overflow:**

```fortran
program scaled_calculation
    implicit none
    real(kind=8) :: x, y, result

    x = 1.0d100
    y = 1.0d100

    ! WRONG: intermediate product overflows
    ! result = x * y * 0.001d0

    ! CORRECT: scale before multiplication
    result = (x * 0.001d0) * y
    print *, result
end program
```

**Use logarithmic arithmetic for products:**

```fortran
program log_arithmetic
    implicit none
    real(kind=8) :: a, b, log_result

    a = 1.0d200
    b = 1.0d200

    ! WRONG: direct multiplication overflows
    ! result = a * b

    ! CORRECT: use logarithms
    log_result = log(a) + log(b)
    print *, 'Log of result:', log_result
    ! Actual result = exp(log_result)
end program
```

**Check for overflow before operations:**

```fortran
program overflow_check
    use ieee_arithmetic
    implicit none
    real(kind=8) :: x, y, result
    logical :: overflow

    x = 1.0d300
    y = 10.0d0

    result = x * y
    overflow = .not. ieee_is_finite(result)

    if (overflow) then
        print *, 'Result would overflow'
    else
        print *, 'Result:', result
    end if
end program
```

**Enable overflow trapping during development:**

```bash
# GFortran: trap on overflow
gfortran -ffpe-trap=overflow -o myprog source.f90

# Intel Fortran: floating point exception level 0
ifort -fpe0 -o myprog source.f90
```

## Common Mistakes

- Using `REAL(4)` when `REAL(8)` or `REAL(16)` is needed for the calculation range
- Not considering intermediate values that overflow even when the final result would fit
- Forgetting that `exp(x)` overflows for x greater than about 709 in double precision
- Assuming compiler defaults will catch overflow without enabling exception flags
- Comparing results to infinity or NaN without using IEEE inquiry functions

## Related Pages

- [Divide by zero in Fortran](/languages/fortran/fortran-divide-by-zero-new)
- [Memory allocation failed in Fortran](/languages/fortran/fortran-allocate-error-v2)
- [Array bounds exceeded in Fortran](/languages/fortran/fortran-array-bounds-new)
- [Namelist read/write error in Fortran](/languages/fortran/fortran-namelist-error-new)
