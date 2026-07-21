---
title: "[Solution] Fortran TEAM Construct Error"
description: "Fix Fortran CHANGE TEAM and SYNC TEAM errors when using team-based execution in Fortran 2018."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

TEAM construct errors occur when CHANGE TEAM is used without proper TEAM_TYPE variables or when SYNC TEAM fails.

## Common Causes

- TEAM_TYPE variable not properly formed
- Missing CHANGE TEAM or END TEAM
- SYNC TEAM on invalid team
- Nested team constructs

## How to Fix

### 1. Form team correctly

```fortran
use iso_fortran_env, only: team_type
type(team_type) :: my_team
form team (1, my_team)
change team (my_team)
    ! team-local code
end team
```

### 2. Use SYNC TEAM for synchronization

```fortran
sync team (my_team)
```

## Examples

```fortran
program team_demo
    use iso_fortran_env, only: team_type
    implicit none
    type(team_type) :: t
    integer :: me
    me = 1
    print *, 'Team demo - image', me
end program
```

## Related Errors

- [Coarray error](/languages/fortran/fortran-coarray)
- [Runtime error](/languages/fortran/runtime-error11)
- [Compile error](/languages/fortran/fortran-compiler-error-new)
