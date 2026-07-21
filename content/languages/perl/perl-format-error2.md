---
title: "[Solution] Perl Format Error"
description: "Fix Perl format and write errors when using format declarations and report printing with write function."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Format errors occur when Perl report formats are incorrectly defined or when write() is called with mismatched format names.

## Common Causes

- Format name does not match subroutine or package
- Picture line contains invalid format codes
- write() called without matching format definition
- Field variables undefined at write time

## How to Fix

### 1. Define format before use

```perl
# WRONG: No format defined
write;  # no format to use

# CORRECT: Define format
format STDOUT =
@<<<<<<<<<<<<<<<<<  @>>>>>>>
$name,              $score
.

# Or use a named format
format USER_REPORT =
User: @<<<<<<<<<<<<
      $name
.
```

### 2. Match format to output handle

```perl
my $fh;
open($fh, '>', 'report.txt');
# Use format with select
select($fh);
write;  # writes to $fh
select(STDOUT);
```

## Examples

```perl
use strict;
use warnings;

format REPORT =
@<<<<<<<<<<<  @>>>>>>  @<<<<<<<<
$name,        $id,     $department
.

my @users = (
    { name => 'Alice', id => 101, dept => 'Engineering' },
    { name => 'Bob',   id => 102, dept => 'Marketing' },
);

my ($name, $id, $department);
foreach my $u (@users) {
    ($name, $id, $department) = @{$u}{qw(name id dept)};
    write;
}
```

## Related Errors

- [Compilation error](/languages/perl/perl-compilation-error)
- [Runtime error](/languages/perl/perl-runtime-error)
- [Undefined value](/languages/perl/undefined-value)
