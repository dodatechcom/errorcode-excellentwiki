---
title: "[Solution] Fortran: format descriptor error"
description: "Fix Fortran format descriptor errors by matching edit descriptors to data types correctly."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A format descriptor error in Fortran occurs when an I/O statement contains a format specification that is incompatible with the data being transferred. This includes mismatched edit descriptors, invalid field widths, incorrect repeat counts, or format strings that do not provide enough descriptors for all data items. The error may appear as a runtime crash or produce garbled output. Fortran format specifications are powerful but rigid, and even small mistakes can cause I/O failures.

## Why It Happens

Format errors arise from several common mistakes. Using an integer edit descriptor like `I5` for a real variable, or `F8.3` for an integer, creates a type mismatch. Providing a field width that is too small for the data causes overflow in the output. Forgetting to provide enough format descriptors for all variables in a WRITE or READ statement leads to undefined behavior. Using parentheses incorrectly in nested format specifications, or having mismatched parentheses in the format string, is another frequent source. Negative field widths, zero repeat counts, or decimal points in integer descriptors are all invalid. The format string may also be malformed when constructed dynamically using string concatenation or character variables.

## How to Fix It

**Match edit descriptors to data types:**

```fortran
program format_types
    implicit none
    integer :: i
    real :: x
    character(len=10) :: s

    i = 42
    x = 3.14159
    s = 'hello'

    ! CORRECT: matching descriptors to types
    write(*, '(I5)') i          ! I for integer
    write(*, '(F10.4)') x       ! F for real
    write(*, '(A10)') s         ! A for character
end program
```

**Ensure enough descriptors for all data items:**

```fortran
program format_count
    implicit none
    integer :: a, b, c

    a = 1; b = 2; c = 3

    ! WRONG: only two descriptors for three items
    ! write(*, '(I5, I5)') a, b, c

    ! CORRECT: three descriptors
    write(*, '(I5, I5, I5)') a, b, c

    ! Or use list-directed I/O
    write(*, *) a, b, c
end program
```

**Use repeat counts for repeated patterns:**

```fortran
program repeat_format
    implicit none
    integer :: arr(5), i

    do i = 1, 5
        arr(i) = i * 10
    end do

    ! Repeat count: 5I6 means five integers each width 6
    write(*, '(5I6)') arr

    ! Or use a general format
    write(*, '(I6)') (arr(i), i = 1, 5)
end program
```

**Fix nested parentheses:**

```fortran
program nested_format
    implicit none
    real :: x, y

    x = 1.5
    y = 2.5

    ! WRONG: mismatched parentheses
    ! write(*, '((F5.2, F5.2)' ) x, y

    ! CORRECT: balanced parentheses
    write(*, '((F5.2, F5.2))') x, y
end program
```

**Use derived format strings carefully:**

```fortran
program dynamic_format
    implicit none
    character(len=20) :: fmt
    integer :: n
    n = 5

    ! Build format string dynamically
    write(fmt, '(A, I2, A)') '(', n, 'I6)'
    print trim(fmt), 1, 2, 3, 4, 5
end program
```

## Common Mistakes

- Using `F` descriptor for integer data or `I` descriptor for real data
- Specifying a field width too small to hold the actual value
- Not providing enough format descriptors for all items in the I/O list
- Using `E` descriptor without a decimal point specification
- Forgetting that list-directed I/O (`*`) does not guarantee consistent formatting across compilers

## Related Pages

- [Array bounds exceeded in Fortran](/languages/fortran/fortran-array-bounds-new)
- [Undefined variable in Fortran](/languages/fortran/fortran-undefined-variable-new)
- [End of file encountered in Fortran](/languages/fortran/fortran-end-of-file-v2)
- [I/O error in Fortran](/languages/fortran/fortran-io-error-v2)
