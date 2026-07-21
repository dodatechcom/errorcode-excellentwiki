---
title: "[Solution] Perl Prototype Error"
description: "Fix Perl subroutine prototype errors when function signatures do not match the declared prototype."
languages: ["perl"]
error-types: ["compile-error"]
severities: ["error"]
---

Prototype errors occur when a Perl subroutine is called with arguments that do not match its declared prototype, causing compile-time or runtime failures.

## Common Causes

- Prototype expects specific types but receives different ones
- Missing prototype declaration on subroutine
- Prototype does not match calling convention
- Using prototypes with method calls

## How to Fix

### 1. Match prototype to usage

```perl
# WRONG: Prototype expects scalar but receives list
sub get_val ($);
get_val(1, 2, 3);  # too many arguments

# CORRECT: Match prototype
sub get_val (@) { return @_ }
my @result = get_val(1, 2, 3);
```

### 2. Remove prototypes for flexible interfaces

```perl
# CORRECT: No prototype, flexible
sub process { return @_ }
```

## Examples

```perl
use strict;
use warnings;

# Example: Prototype mismatch
sub multiply ($$) {
    my ($a, $b) = @_;
    return $a * $b;
}

my $result = multiply(4, 5);  # OK
# multiply(4, 5, 6);  # ERROR: wrong number of arguments
```

## Related Errors

- [Undefined subroutine](/languages/perl/undefined-sub)
- [Compilation error](/languages/perl/perl-compilation-error)
- [Syntax error](/languages/perl/syntax-error6)
