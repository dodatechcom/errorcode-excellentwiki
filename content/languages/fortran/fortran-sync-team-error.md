---
title: "[Solution] Fortran SYNC TEAM Error"
description: "Fix Fortran SYNC TEAM errors when synchronizing teams of images in Fortran 2018."
languages: ["fortran"]
error-types: ["runtime-error"]
severities: ["error"]
---

SYNC TEAM errors occur when the team variable is invalid or when team members have inconsistent state.

## Common Causes

- SYNC TEAM on invalid team
- Team not formed properly
- Missing FORM TEAM before SYNC TEAM
- TEAM_TYPE variable not properly initialized

## How to Fix

### 1. Form team before sync

```fortran
type(team_type) :: team
form team (image_index, team)
sync team (team)
```

### 2. Use proper team variable

```fortran
type(team_type) :: my_team
! ... form team ...
sync team (my_team, STAT= ierr)
if (ierr /= 0) print *, 'SYNC TEAM error:', ierr
```

## Examples

```fortran
program sync_team_demo
    use iso_fortran_env, only: team_type
    implicit none
    type(team_type) :: t
    integer :: me
    me = this_image()
    print *, 'Image', me, 'in team'
end program
```

## Related Errors

- [Team error](/languages/fortran/fortran-team-error)
- [Coarray error](/languages/fortran/fortran-coarray)
- [Runtime error](/languages/fortran/runtime-error11)
