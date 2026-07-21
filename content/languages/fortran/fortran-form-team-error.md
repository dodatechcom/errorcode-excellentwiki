---
title: "[Solution] Fortran FORM TEAM Error"
description: "Fix Fortran FORM TEAM errors when creating new teams of images."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

FORM TEAM errors occur when the team index is invalid or when FORM TEAM is called with incorrect arguments.

## Common Causes

- Invalid team index
- FORM TEAM with non TEAM_TYPE variable
- Missing CHANGE TEAM after FORM TEAM
- FORM TEAM on images not in same team

## How to Fix

### 1. Use valid team index

```fortran
type(team_type) :: new_team
form team (1, new_team)  ! team index must be positive
```

### 2. Always pair with CHANGE TEAM

```fortran
form team (my_team_number, new_team)
change team (new_team)
    ! team-local code
end team
```

## Examples

```fortran
program form_team_demo
    use iso_fortran_env, only: team_type
    implicit none
    type(team_type) :: t
    integer :: me
    me = this_image()
    print *, 'Image', me, 'ready for team formation'
end program
```

## Related Errors

- [Team error](/languages/fortran/fortran-team-error)
- [Coarray error](/languages/fortran/fortran-coarray)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
